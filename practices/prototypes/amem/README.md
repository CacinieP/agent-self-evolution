# Prototype: A-MEM 自组织记忆网络(Agentic Memory)

> 对应论文:[A-MEM: Agentic Memory for LLM Agents](../../../surveys/papers/2025-a-mem)(NeurIPS 2025)
> TAXONOMY 定位:`What: Context(Memory) · When: Inter-test-time × ICL`

## 🎯 这个原型做什么

受 Zettelkasten 启发,把记忆从"平铺列表"升级为**会生长、会自我整理的知识网络**。

```
note construction :每次交互沉淀为一个结构化笔记节点
link generation   :节点间自动建立语义链接(本原型用字符 Jaccard 近似)
memory evolution  :高相似节点触发演化 —— 合并/精炼(真实场景由 LLM 精炼内容)
recall            :检索时不只召回单点,而是沿链接召回关联网络(BFS)
```

## 与 Voyager 技能库的本质区别

| | Voyager 技能库 | **A-MEM(本原型)** |
|---|---|---|
| 存储结构 | 平铺条目列表 | **图:节点 + 语义链接** |
| 记忆间关系 | 独立 | **互相关联,可沿链遍历** |
| 自我整理 | 无 | **演化:合并近义、更新链接** |
| 检索 | top-k 相似 | **种子 + 多跳关联召回** |

一句话:技能库把经验存成"孤立资产",A-MEM 把记忆织成"生长的网络"。

## 📁 文件

| 文件 | 说明 |
|---|---|
| [`amem.py`](./amem.py) | 主程序,单文件 |
| `requirements.txt` | 真实模型模式需要 `openai` |

## 🚀 快速开始

```bash
# 离线 mock:观察笔记建链、关联召回(演化需真实 embedding 才频繁触发)
python amem.py --mock --inputs "猫是肉食动物" "猫科动物包括老虎" "老虎是大型猫科" "Python是编程语言"

# 真实模型(LLM 抽取笔记内容,语义更准)
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
python amem.py --inputs "RL 是用奖励信号优化策略的方法" "强化学习依赖环境反馈" "Transformer 是主流架构" --model gpt-4o-mini
```

## 🧠 实现要点

- **零依赖相似度**:用字符集合 Jaccard 近似语义相似度,保持单文件可读;生产可换 embedding。
- **演化安全**:`_link_and_evolve` 取节点快照遍历,避免合并删节点时并发修改(踩过的坑已修)。
- **图式召回**:`recall()` 找到种子节点后做 BFS,返回整个关联子网,而非孤立单点。
- **双阈值分离**:`link_threshold`(建链)低于 `merge_threshold`(合并),避免无关记忆被误合并。

## 🔧 可玩的扩展方向

1. **换相似度**:字符 Jaccard → sentence-transformers embedding 余弦,链接与演化都会更频繁、更准。
2. **LLM 驱动演化**:把 `_evolve_merge` 的"机械拼接"换成 LLM 生成精炼后的统一笔记。
3. **遗忘机制**:给链接加衰减、低频节点淘汰,避免网络无限膨胀。
4. **接入 Agent**:把 A-MEM 作为长程 Agent 的记忆后端,对比"无记忆 vs 平铺记忆 vs 网络记忆"的表现。

## 📐 维度速查(TAXONOMY)

```
What:   Context(Memory / 自组织网络)
When:   Inter-test-time × ICL
How:    Imitation(归纳) + Reward-based(相关性) · Online · On-policy · Hybrid
Where:  General(长程记忆)
Eval:   Retention, Adaptivity, Efficiency
```
