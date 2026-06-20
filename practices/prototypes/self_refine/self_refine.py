"""
Self-Refine 最小可运行原型

复现 Self-Refine (Madaan et al., NeurIPS 2023) 的核心三步循环:
    generate -> feedback -> refine
全程零额外训练、零外部监督,仅靠模型自身的自反馈迭代改进输出。

用法:
    # 真实模型(需 OPENAI_API_KEY,可选 OPENAI_BASE_URL 指向兼容端点)
    export OPENAI_API_KEY=sk-...
    python self_refine.py --task "给一个关于回收利用的简短公益标语" --iters 3

    # 离线 mock(无需 API,用于自测/演示)
    python self_refine.py --mock --task "..." --iters 3

详见同目录 README.md。
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from typing import Callable, Optional

# ---------------------------------------------------------------------------
# 1. 推理后端:统一抽象 + OpenAI 兼容实现 + 离线 Mock
# ---------------------------------------------------------------------------

LLMFn = Callable[[str], str]


def _build_openai_fn(model: str) -> LLMFn:
    """构造一个 OpenAI 兼容的 LLM 调用函数。"""
    try:
        from openai import OpenAI  # 延迟导入,避免 mock 模式强制依赖
    except ImportError as e:  # pragma: no cover
        sys.exit("缺少依赖:请 `pip install openai`,或用 --mock 模式自测。")

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=os.environ.get("OPENAI_BASE_URL"),  # 可指向任意兼容端点
    )

    def _fn(prompt: str) -> str:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return resp.choices[0].message.content.strip()

    return _fn


def _build_mock_fn() -> LLMFn:
    """离线 mock:每次在输出后追加改进标记,用于无 API 时自测迭代逻辑。"""
    state = {"n": 0}

    def _fn(prompt: str) -> str:
        state["n"] += 1
        tag = f"[v{state['n']}]"
        if prompt.startswith("FEEDBACK"):
            return f"{tag} 建议加入具体行动号召与简短数字。"
        return f"{tag} 保护地球,从回收开始。"

    return _fn


# ---------------------------------------------------------------------------
# 2. Self-Refine 三步:generate / feedback / refine
# ---------------------------------------------------------------------------


@dataclass
class Step:
    iteration: int
    output: str
    feedback: Optional[str] = None


def generate(llm: LLMFn, task: str) -> str:
    return llm(f"任务: {task}\n\n请直接给出你的回答,不要多余解释。")


def feedback(llm: LLMFn, task: str, output: str) -> str:
    prompt = (
        "FEEDBACK\n"
        f"任务: {task}\n"
        f"当前回答: {output}\n\n"
        "你是严格的审稿人。请只给出【具体、可执行】的改进建议(不超过 3 条),"
        "不要直接给出改写后的完整答案。"
    )
    return llm(prompt)


def refine(llm: LLMFn, task: str, output: str, fb: str) -> str:
    prompt = (
        f"任务: {task}\n"
        f"当前回答: {output}\n"
        f"改进建议: {fb}\n\n"
        "请根据建议改写出一个更好的回答,直接输出改写结果。"
    )
    return llm(prompt)


# ---------------------------------------------------------------------------
# 3. 主循环
# ---------------------------------------------------------------------------


def self_refine(
    task: str,
    llm: LLMFn,
    iters: int = 3,
    stop_on_no_feedback: bool = True,
) -> list[Step]:
    history: list[Step] = []
    cur = generate(llm, task)
    history.append(Step(0, cur))

    for i in range(1, iters + 1):
        fb = feedback(llm, task, cur)
        # 简单的早停:若无实质建议则终止
        if stop_on_no_feedback and _looks_satisfied(fb):
            history.append(Step(i, cur, fb))
            break
        cur = refine(llm, task, cur, fb)
        history.append(Step(i, cur, fb))

    return history


_NO_CHANGE_HINTS = ("很好", "无需", "no change", "looks good", "无需修改", "已经很")


def _looks_satisfied(fb: str) -> bool:
    low = fb.lower()
    return any(h.lower() in low for h in _NO_CHANGE_HINTS) and len(fb) < 40


# ---------------------------------------------------------------------------
# 4. CLI
# ---------------------------------------------------------------------------


def main() -> None:
    p = argparse.ArgumentParser(description="Self-Refine 最小可运行原型")
    p.add_argument("--task", required=True, help="要完成的任务/问题")
    p.add_argument("--iters", type=int, default=3, help="最多迭代次数(默认 3)")
    p.add_argument("--model", default="gpt-4o-mini", help="模型名(OpenAI 兼容)")
    p.add_argument("--mock", action="store_true", help="离线 mock 模式,无需 API")
    args = p.parse_args()

    llm = _build_mock_fn() if args.mock else _build_openai_fn(args.model)

    print(f"=== Task ===\n{args.task}\n")
    history = self_refine(args.task, llm, iters=args.iters)

    for step in history:
        label = "初稿" if step.iteration == 0 else f"第 {step.iteration} 轮"
        print(f"--- {label} ---")
        if step.feedback:
            print(f"反馈: {step.feedback}")
        print(step.output + "\n")


if __name__ == "__main__":
    main()
