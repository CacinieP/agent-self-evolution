"""
Reflexion 最小可运行原型(环境反馈版)

对应论文:Reflexion (Shinn et al., NeurIPS 2023)。
与 Self-Refine 的关键区别:
  - 反馈来自【环境执行结果】(这里用 Python 代码真实运行),而非模型自评;
  - 失败后生成文字"反思",写入记忆,在后续试验中复用,逐步避免重复犯错。

场景:给 Agent 一个编程题,它要写出能通过的代码。
  试验 i: act(写代码) → 环境执行 → 若失败则 reflect(生成反思,存进 memory) → 进入试验 i+1
  每次试验都会把"历史反思"注入上下文。

用法:
    # 真实模型
    export OPENAI_API_KEY=sk-...
    python reflexion.py --task "写函数 is_prime(n): 判断 n 是否为素数" --trials 3 --allow-unsafe-exec

    # 离线 mock(无需 API,可观察"记忆累积"逻辑)
    python reflexion.py --mock --task "写函数 is_prime(n)" --trials 3
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from typing import Callable

LLMFn = Callable[[str], str]


# ---------------------------------------------------------------------------
# 1. LLM 后端(OpenAI 兼容 + 离线 Mock)
# ---------------------------------------------------------------------------


def _build_openai_fn(model: str) -> LLMFn:
    try:
        from openai import OpenAI
    except ImportError:  # pragma: no cover
        sys.exit("缺少依赖:请 `pip install openai`,或用 --mock 模式。")
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:  # pragma: no cover
        sys.exit("缺少 OPENAI_API_KEY:请设置环境变量,或用 --mock 模式。")
    client = OpenAI(api_key=api_key, base_url=os.environ.get("OPENAI_BASE_URL"))

    def _fn(prompt: str) -> str:
        r = client.chat.completions.create(
            model=model, messages=[{"role": "user", "content": prompt}], temperature=0.3
        )
        if not r.choices:  # pragma: no cover
            sys.exit("API 返回空响应(可能被安全过滤或限流),请重试或换模型。")
        return (r.choices[0].message.content or "").strip()

    return _fn


def _build_mock_fn() -> LLMFn:
    """mock:第 1 次给"有 bug 的代码",失败反思后第 2 次给"正确代码"。"""
    state = {"n": 0}

    def _fn(prompt: str) -> str:
        state["n"] += 1
        if prompt.startswith("REFLECT"):
            return "边界条件 n<=1 应返回 False;1 不是素数。"
        # 生成代码:若历史记忆为空→给错的;否则给对的
        if "记忆中的反思" in prompt and "暂无" not in prompt:
            return "```python\ndef is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n```"
        return "```python\ndef is_prime(n):\n    if n < 1:\n        return False\n    for i in range(2, n):\n        if n % i == 0:\n            return False\n    return True\n```"

    return _fn


# ---------------------------------------------------------------------------
# 2. 环境反馈:真实执行 Agent 写的代码,用测试用例判对错
# ---------------------------------------------------------------------------

DEFAULT_TESTS = [
    ("is_prime(2)", True),
    ("is_prime(1)", False),   # 常见 bug 点
    ("is_prime(9)", False),
    ("is_prime(7)", True),
    ("is_prime(-3)", False),
]

_RESULT_PREFIX = "__REFLEXION_RESULT__"
_TEST_RUNNER = r'''
import json
import sys

PREFIX = "__REFLEXION_RESULT__"
payload = json.loads(sys.stdin.read())
namespace = {}

try:
    exec(payload["code"], namespace)
except BaseException as exc:
    result = {
        "ok": False,
        "diag": f"代码执行抛异常: {type(exc).__name__}: {exc}",
    }
else:
    failures = []
    for expression, expected in payload["tests"]:
        try:
            actual = eval(expression, namespace)
        except BaseException as exc:
            failures.append(f"  {expression} -> 抛异常 {type(exc).__name__}")
            continue
        if actual != expected:
            failures.append(f"  {expression} -> 得到 {actual!r},期望 {expected!r}")
    result = {
        "ok": not failures,
        "diag": "全部测试通过 ✅" if not failures else "未通过的用例:\n" + "\n".join(failures),
    }

print(PREFIX + json.dumps(result, ensure_ascii=False))
'''


def _extract_code(text: str) -> str:
    m = re.search(r"```(?:python)?\s*(.*?)```", text, re.S)
    return (m.group(1) if m else text).strip()


def run_tests(
    code: str,
    tests: list[tuple[str, bool]],
    timeout: float = 5.0,
) -> tuple[bool, str]:
    """在独立 Python 子进程中执行 code 并跑 tests。

    子进程与超时可隔离崩溃和死循环，但这不是安全沙箱；调用方仍须只执行
    可信代码，或在容器/受限解释器中运行整个原型。
    """
    payload = json.dumps({"code": code, "tests": tests}, ensure_ascii=False)
    child_env = {"PYTHONIOENCODING": "utf-8"}
    for name in ("SYSTEMROOT", "WINDIR"):
        if name in os.environ:  # Windows 启动 Python 可能需要
            child_env[name] = os.environ[name]
    try:
        proc = subprocess.run(
            [sys.executable, "-I", "-c", _TEST_RUNNER],
            input=payload,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=child_env,
        )
    except subprocess.TimeoutExpired:
        return False, f"代码执行超时(>{timeout:g}s)"

    for line in reversed(proc.stdout.splitlines()):
        if line.startswith(_RESULT_PREFIX):
            try:
                result = json.loads(line[len(_RESULT_PREFIX):])
            except json.JSONDecodeError:
                break
            return bool(result["ok"]), str(result["diag"])

    detail = (proc.stderr or proc.stdout).strip().splitlines()
    tail = detail[-1] if detail else f"子进程退出码 {proc.returncode}"
    return False, f"测试子进程未返回有效结果: {tail}"


# ---------------------------------------------------------------------------
# 3. Reflexion 主循环:act -> env -> (reflect -> memory)
# ---------------------------------------------------------------------------


@dataclass
class Trial:
    idx: int
    code: str
    passed: bool
    diag: str
    reflection: str = ""


def reflexion(
    task: str,
    llm: LLMFn,
    trials: int,
    tests: list[tuple[str, bool]],
    exec_timeout: float = 5.0,
) -> tuple[list[Trial], list[str]]:
    memory: list[str] = []          # 历史反思(持久记忆)
    history: list[Trial] = []

    for i in range(1, trials + 1):
        mem_str = "\n".join(f"- {m}" for m in memory) if memory else "(暂无)"
        # act:带历史反思写代码
        act_prompt = textwrap.dedent(f"""
            任务: {task}
            记忆中的反思(避免重复犯错):
            {mem_str}

            请只输出一个完整的 Python 函数(用 ```python``` 包裹),不要解释。
        """).strip()
        raw = llm(act_prompt)
        code = _extract_code(raw)

        passed, diag = run_tests(code, tests, timeout=exec_timeout)
        t = Trial(i, code, passed, diag)

        if passed:
            history.append(t)
            break
        # reflect:基于失败诊断生成反思,写入记忆
        refl_prompt = textwrap.dedent(f"""
            REFLECT
            任务: {task}
            你上一版代码的诊断信息:
            {diag}

            请用一两句话总结【这次失败的原因和下次应避免的具体错误】,作为给未来自己的提醒。
        """).strip()
        reflection = llm(refl_prompt)
        memory.append(reflection)
        t.reflection = reflection
        history.append(t)

    return history, memory


# ---------------------------------------------------------------------------
# 4. CLI
# ---------------------------------------------------------------------------


def main() -> None:
    p = argparse.ArgumentParser(description="Reflexion 最小可运行原型(环境反馈版)")
    p.add_argument("--task", help="编程任务描述；内置测试要求实现 is_prime(n)(--selftest 时可省)")
    p.add_argument("--trials", type=int, default=3)
    p.add_argument("--exec-timeout", type=float, default=5.0, help="每次候选代码的执行超时秒数(默认 5)")
    p.add_argument("--model", default="gpt-4o-mini")
    p.add_argument("--mock", action="store_true")
    p.add_argument(
        "--allow-unsafe-exec",
        action="store_true",
        help="确认允许执行模型生成的代码；真实模型模式必填(子进程不是安全沙箱)",
    )
    p.add_argument("--selftest", action="store_true", help="内置示例自测(强制 mock)")
    args = p.parse_args()

    if args.trials < 1:
        p.error("--trials 必须至少为 1")
    if args.exec_timeout <= 0:
        p.error("--exec-timeout 必须大于 0")

    if args.selftest:
        args.mock = True
        args.task = args.task or "写函数 is_prime(n): 判断 n 是否为素数"
    elif not args.task:
        p.error("--task 为必填(或使用 --selftest 自测)")
    elif not args.mock and not args.allow_unsafe_exec:
        p.error("真实模型模式会执行模型生成的代码；确认风险后请添加 --allow-unsafe-exec")

    llm = _build_mock_fn() if args.mock else _build_openai_fn(args.model)
    history, memory = reflexion(
        args.task,
        llm,
        args.trials,
        DEFAULT_TESTS,
        exec_timeout=args.exec_timeout,
    )

    print(f"=== Task ===\n{args.task}\n")
    for t in history:
        print(f"--- 试验 {t.idx}({'通过' if t.passed else '失败'}) ---")
        print(t.code)
        print(f"诊断: {t.diag}")
        if t.reflection:
            print(f"反思(已入记忆): {t.reflection}")
        print()
    print("=== 最终记忆 ===")
    for m in memory:
        print(f"- {m}")
    print("\n结果:", "✅ 成功" if history[-1].passed else "❌ 用尽试验仍未通过")


if __name__ == "__main__":
    main()
