# ToolMem: Tool-Enhanced Memory for LLM Agents

- **作者**: Yifan Wang et al.
- **发表**: arXiv:2503.07703 (2025)
- **链接**: https://arxiv.org/abs/2503.07703
- **代码**: —

## 一句话总结
将工具调用结果作为记忆的一部分,让 Agent 能检索和利用过去工具使用的经验。

## 核心方法
将工具调用(参数+结果+评估)编码为可检索记忆条目,与常规观察记忆统一管理,支持按工具类型和任务上下文检索。

## 关键贡献
工具记忆作为独立记忆维度,在多任务场景下显著减少重复工具调用失败。

## 维度速查 (TAXONOMY)
```
What:   Tool(Scale management & selection) + Context(Memory)
When:   Inter-test-time × ICL
How:    Reward-based · Offline · On-policy · Outcome
Where:  General
Eval:   Retention, Efficiency
```
