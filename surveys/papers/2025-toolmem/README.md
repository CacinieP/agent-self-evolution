# ToolMem: Enhancing Multimodal Agents with Learnable Tool Capability Memory

- **作者**: Xiao et al. (2025)
- **发表**: arXiv:2510.06664 (2025)
- **链接**: https://arxiv.org/abs/2510.06664
- **代码**: —

## 一句话总结
工具能力编码为可学习记忆,Agent 检索和利用过去工具使用的经验。

## 核心方法
将工具调用编码为可检索记忆条目,Agent 根据任务上下文检索相关工具经验。

## 关键贡献
工具记忆作为独立记忆维度,减少重复工具调用失败。

## 维度速查 (TAXONOMY)
```
What:   Tool(Scale management & selection) + Context(Memory)
When:   Inter-test-time × ICL
How:    Reward-based · Offline · On-policy · Outcome
Where:  General
Eval:   Retention, Efficiency
```
