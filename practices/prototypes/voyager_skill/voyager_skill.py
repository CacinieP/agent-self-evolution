"""
Voyager 技能库简化原型(Skill Library Flywheel)

对应论文:Voyager (Wang et al., 2023)。
本原型聚焦 Voyager 三大组件中最具自进化意味的【技能库飞轮】,
把 Minecraft 的"代码技能"抽象为"文本任务技能",便于在本地无依赖地观察:

  遇到任务
    -> 检索技能库:有相关可复用技能?
        -> 有: 把技能作为提示注入,据此解决
        -> 无: 从零生成解决方案
    -> 执行验证(这里用"自评通过判定"模拟环境)
    -> 成功: 把本次解法抽象成技能存进库
    -> 失败: 带反馈重新生成

  随库增长,越来越多任务能被"复用旧技能"秒解 → 正反馈飞轮。

用法:
    python voyager_skill.py --mock --tasks "写一首关于春天的短诗" "创作一首春天的诗" "写秋天主题的诗"
    python voyager_skill.py --task "写一封会议邀请邮件"   # 单任务
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass, field
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
            model=model, messages=[{"role": "user", "content": prompt}], temperature=0.5
        )
        if not r.choices:  # pragma: no cover
            sys.exit("API 返回空响应(可能被安全过滤或限流),请重试或换模型。")
        return (r.choices[0].message.content or "").strip()

    return _fn


def _build_mock_fn() -> LLMFn:
    """mock:简单回显,便于观察技能库增长与复用逻辑(而非内容质量)。"""
    state = {"n": 0}

    def _fn(prompt: str) -> str:
        state["n"] += 1
        if prompt.startswith("ABSTRACT"):
            return "技能:按 [主题] 用 [四行] 押韵结构快速成诗。"
        if prompt.startswith("VERIFY"):
            return "PASS"
        # 求解:若有复用技能提示,标注"复用";否则"从零"
        reused = "[复用技能]" if "可复用技能" in prompt and "无" not in prompt else "[从零生成]"
        return f"{reused} 针对[{prompt.split('任务:')[-1].split(chr(10))[0]}]的方案 v{state['n']}"

    return _fn


# ---------------------------------------------------------------------------
# 2. 技能库 + 语义检索(用最简字符重叠近似语义相似度,零依赖)
# ---------------------------------------------------------------------------


@dataclass
class Skill:
    name: str
    description: str            # 触发条件 / 适用场景描述
    solution: str               # 可复用的解决方案模板
    uses: int = 0               # 被复用次数


@dataclass
class SkillLibrary:
    skills: list[Skill] = field(default_factory=list)

    def retrieve(self, task: str, topk: int = 1) -> list[Skill]:
        """最简检索:按 task 与 description 的字符重叠排序。"""
        def overlap(s: Skill) -> int:
            return len(set(task) & set(s.description))
        ranked = sorted(self.skills, key=overlap, reverse=True)
        return [s for s in ranked[:topk] if overlap(s) > 0]

    def add(self, skill: Skill) -> None:
        self.skills.append(skill)


# ---------------------------------------------------------------------------
# 3. 主循环:retrieve -> (reuse | create) -> verify -> store
# ---------------------------------------------------------------------------


@dataclass
class Run:
    task: str
    solution: str
    reused: bool
    passed: bool
    attempts: int
    new_skill: str = ""


def _verify(llm: LLMFn, task: str, solution: str) -> tuple[bool, str]:
    response = llm(
        f"VERIFY\n任务: {task}\n方案: {solution}\n"
        "该方案是否基本可用?第一行只回 PASS 或 FAIL;若为 FAIL,可在后续说明原因。"
    ).strip()
    match = re.match(r"^(PASS|FAIL)\b", response, re.IGNORECASE)
    return bool(match and match.group(1).upper() == "PASS"), response


def _abstract(llm: LLMFn, task: str, solution: str) -> tuple[str, str]:
    """把一次成功解法抽象成可复用技能(name, description)。"""
    out = llm(f"ABSTRACT\n任务: {task}\n解法: {solution}\n请用一句话总结这个可复用技能(含适用场景关键词)。")
    # 简单切分:取冒号后为 name,整句为 description
    name = out.split(":", 1)[-1].strip().split("。")[0][:30] if ":" in out else out[:30]
    return name, out


def solve_task(task: str, llm: LLMFn, lib: SkillLibrary, retries: int = 1) -> Run:
    if retries < 0:
        raise ValueError("retries must be non-negative")

    hits = lib.retrieve(task)
    reused = bool(hits)
    skill_hint = hits[0].solution if hits else "无"

    solution = ""
    verdict = ""
    passed = False
    attempts = 0
    for attempts in range(1, retries + 2):
        if attempts == 1:
            prompt = (
                f"任务: {task}\n"
                f"可复用技能: {skill_hint}\n\n"
                "请给出解决方案。若有可复用技能,请基于它适配。"
            )
        else:
            prompt = (
                f"任务: {task}\n"
                f"可复用技能: {skill_hint}\n"
                f"上次方案: {solution}\n"
                f"验证反馈: {verdict}\n\n"
                "请根据验证反馈修正方案,不要重复同一错误。"
            )
        solution = llm(prompt)
        passed, verdict = _verify(llm, task, solution)
        if passed:
            break

    run = Run(
        task=task,
        solution=solution,
        reused=reused,
        passed=passed,
        attempts=attempts,
    )

    if passed:
        # 成功 -> 抽象成技能存库(无论是否复用,新解法也可沉淀)
        name, desc = _abstract(llm, task, solution)
        lib.add(Skill(name=name, description=desc, solution=solution))
        run.new_skill = name
        if hits:
            hits[0].uses += 1
    return run


# ---------------------------------------------------------------------------
# 4. CLI
# ---------------------------------------------------------------------------


def main() -> None:
    p = argparse.ArgumentParser(description="Voyager 技能库简化原型")
    g = p.add_mutually_exclusive_group(required=False)
    g.add_argument("--task", help="单个任务")
    g.add_argument("--tasks", nargs="+", help="多个任务(顺序执行,共享技能库)")
    p.add_argument("--model", default="gpt-4o-mini")
    p.add_argument("--retries", type=int, default=1, help="验证失败后的最大重试次数(默认 1)")
    p.add_argument("--mock", action="store_true")
    p.add_argument("--selftest", action="store_true", help="内置示例自测(强制 mock)")
    args = p.parse_args()

    if args.retries < 0:
        p.error("--retries 不能为负数")

    if args.selftest:
        args.mock = True
        args.tasks = args.tasks or ["写一首关于春天的短诗", "创作一首春天的诗", "写一首秋天的诗"]
    elif not args.task and not args.tasks:
        p.error("需提供 --task 或 --tasks(或使用 --selftest 自测)")

    llm = _build_mock_fn() if args.mock else _build_openai_fn(args.model)
    tasks = args.tasks if args.tasks else [args.task]
    lib = SkillLibrary()

    print(f"=== Voyager 技能库原型 | {len(tasks)} 个任务 ===\n")
    for i, task in enumerate(tasks, 1):
        r = solve_task(task, llm, lib, retries=args.retries)
        mode = "♻️ 复用" if r.reused else "✨ 新建"
        res = "✅" if r.passed else "❌"
        print(f"[{i}] {res} {mode}  任务: {task}")
        print(f"     方案: {r.solution[:80]}")
        print(f"     尝试次数: {r.attempts}")
        if r.new_skill:
            print(f"     + 入库技能: {r.new_skill}")
        print(f"     技能库规模: {len(lib.skills)}")
        print()


if __name__ == "__main__":
    main()
