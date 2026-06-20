"""
A-MEM 自组织记忆网络 简化原型(Agentic Memory)

对应论文:A-MEM: Agentic Memory for LLM Agents (Xu et al., NeurIPS 2025)。
受 Zettelkasten 启发:记忆不是平铺列表,而是一张【会生长、会自我整理】的知识网络。

与 Voyager 技能库的关键区别:
  - 技能库:平铺条目 + 检索(独立的资产)
  - A-MEM :每条记忆是【笔记节点】,节点间有【语义链接】,
           且会【演化】(精炼/合并/重连),形成关联网络

三步:
  note construction :把一次交互沉淀为结构化笔记节点
  link generation  :在节点间建立语义链接(本原型用字符重叠近似)
  memory evolution :随新节点加入,演化网络(更新链接强度 / 合并近义节点)

本原型用最简结构演示这套机制,零依赖。

用法:
    python amem.py --mock --inputs "猫是肉食动物" "狗是常见的宠物" "老虎属于猫科" "橘猫也是一种猫"
    python amem.py --inputs "Python 是解释型语言" ...
"""

from __future__ import annotations

import argparse
import os
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
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_BASE_URL"))

    def _fn(prompt: str) -> str:
        r = client.chat.completions.create(
            model=model, messages=[{"role": "user", "content": prompt}], temperature=0.3
        )
        return r.choices[0].message.content.strip()

    return _fn


def _build_mock_fn() -> LLMFn:
    """mock:把输入浓缩为关键词短语,便于观察链接与演化。"""
    def _fn(prompt: str) -> str:
        if prompt.startswith("EXTRACT"):
            # EXTRACT\n{原文}\n\n请把... —— 只取第一行后的原文
            lines = prompt.split("\n")
            return lines[1].strip()[:24] if len(lines) > 1 else lines[0][:24]
        return prompt[:24]
    return _fn


# ---------------------------------------------------------------------------
# 2. 记忆网络:节点 + 链接 + 演化
# ---------------------------------------------------------------------------


@dataclass
class Note:
    id: int
    content: str                       # 笔记内容
    links: dict[int, float] = field(default_factory=dict)   # 邻居id -> 链接强度
    merges: int = 0                    # 被合并演化次数


class MemoryNetwork:
    def __init__(self, link_threshold: float = 0.2, merge_threshold: float = 0.45):
        self.nodes: dict[int, Note] = {}
        self._next = 0
        self.link_threshold = link_threshold
        self.merge_threshold = merge_threshold

    # --- note construction ---
    def add_note(self, content: str) -> Note:
        nid = self._next
        self._next += 1
        note = Note(id=nid, content=content)
        self.nodes[nid] = note
        self._link_and_evolve(note)
        return note

    # --- similarity(零依赖:字符集合的 Jaccard)---
    @staticmethod
    def _sim(a: str, b: str) -> float:
        sa, sb = set(a), set(b)
        if not sa or not sb:
            return 0.0
        return len(sa & sb) / len(sa | sb)

    # --- link generation + memory evolution ---
    def _link_and_evolve(self, new: Note) -> None:
        # 取快照,避免演化合并删节点时并发修改
        others = [o for o in self.nodes.values() if o.id != new.id]
        for other in others:
            if other.id not in self.nodes:          # 可能已被合并删除
                continue
            sim = self._sim(new.content, other.content)
            if sim >= self.link_threshold:
                # 建双向链接
                new.links[other.id] = sim
                other.links[new.id] = sim
                # 演化:高相似度触发"合并"启发式(标记,真实场景可由 LLM 精炼)
                if sim >= self.merge_threshold and other.merges < 1:
                    self._evolve_merge(new, other)

    def _evolve_merge(self, a: Note, b: Note) -> None:
        """演化:把两个高度相似节点合并为一个更精炼的笔记,保留链接。"""
        merged_content = f"{a.content} ≈ {b.content}"
        a.content = merged_content
        a.merges += 1
        # b 的链接并入 a
        for nid, w in b.links.items():
            if nid == a.id:
                continue
            a.links[nid] = max(a.links.get(nid, 0.0), w)
            if nid in self.nodes:
                self.nodes[nid].links[a.id] = a.links[nid]
                self.nodes[nid].links.pop(b.id, None)
        a.links.pop(b.id, None)
        del self.nodes[b.id]

    # --- 检索:沿链接召回关联网络(BFS)---
    def recall(self, query: str, hops: int = 1) -> list[Note]:
        if not self.nodes:
            return []
        scored = [(self._sim(query, n.content), n) for n in self.nodes.values()]
        scored.sort(key=lambda x: x[0], reverse=True)
        if not scored or scored[0][0] < self.link_threshold:
            return []
        seed = scored[0][1]
        visited = {seed.id}
        frontier = [seed]
        for _ in range(hops):
            nxt = []
            for n in frontier:
                for nid in n.links:
                    if nid not in visited and nid in self.nodes:
                        visited.add(nid)
                        nxt.append(self.nodes[nid])
            frontier = nxt
        return [self.nodes[i] for i in sorted(visited)]

    def stats(self) -> dict:
        edges = sum(len(n.links) for n in self.nodes.values()) // 2
        return {"nodes": len(self.nodes), "edges": edges, "merges": sum(n.merges for n in self.nodes.values())}


# ---------------------------------------------------------------------------
# 3. 记忆沉淀:把原始交互抽取为笔记
# ---------------------------------------------------------------------------


def construct_note(llm: LLMFn, raw: str) -> str:
    return llm(f"EXTRACT\n{raw}\n\n请把上面这段内容浓缩为一句可作为记忆笔记的关键信息。")


def run(llm: LLMFn, inputs: list[str], net: MemoryNetwork) -> None:
    print(f"=== A-MEM 自组织记忆网络 | {len(inputs)} 条输入 ===\n")
    for i, raw in enumerate(inputs, 1):
        note = construct_note(llm, raw)
        n = net.add_note(note)
        s = net.stats()
        print(f"[{i}] + 笔记 #{n.id}: {n.content}")
        print(f"     网络: 节点 {s['nodes']} · 链接 {s['edges']} · 演化合并 {s['merges']}")
        if n.links:
            peers = ", ".join(f"#{k}({v:.2f})" for k, v in sorted(n.links.items(), key=lambda x: -x[1])[:3])
            print(f"     链接到: {peers}")
        print()

    # 演示检索
    q = inputs[0][:12] if inputs else "猫"
    print(f"=== 检索演示:沿链接召回(1跳)===\n查询: {q!r}")
    for hit in net.recall(q, hops=1):
        peers = list(hit.links.keys())
        print(f"  #{hit.id}: {hit.content}  [链接 {len(peers)} 个]")


def main() -> None:
    p = argparse.ArgumentParser(description="A-MEM 自组织记忆网络 简化原型")
    p.add_argument("--inputs", nargs="+", help="若干条交互/事实(--selftest 时可省)")
    p.add_argument("--model", default="gpt-4o-mini")
    p.add_argument("--mock", action="store_true")
    p.add_argument("--selftest", action="store_true", help="内置示例自测(强制 mock)")
    args = p.parse_args()

    if args.selftest:
        args.mock = True
        args.inputs = args.inputs or ["猫是肉食动物", "猫科动物包括老虎", "老虎是大型猫科", "Python是编程语言"]
    elif not args.inputs:
        p.error("需提供 --inputs(或使用 --selftest 自测)")

    llm = _build_mock_fn() if args.mock else _build_openai_fn(args.model)
    run(llm, args.inputs, MemoryNetwork())


if __name__ == "__main__":
    main()
