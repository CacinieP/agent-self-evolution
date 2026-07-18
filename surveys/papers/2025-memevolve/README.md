# MemEvolve: Memory-Driven Architecture Evolution for LLM Agents

- **作者**: (Multiple authors)
- **发表**: arXiv:2502.19251 (2025)
- **链接**: https://arxiv.org/abs/2502.19251
- **代码**: —

## 一句话总结
基于记忆反馈驱动 Agent 架构组件的自进化,动态调整模块配置和连接方式。

## 核心方法
Agent 根据记忆中的历史任务表现,自动调整内部模块(记忆管理器/推理器/工具选择器)的配置与连接。

## 关键贡献
将记忆反馈作为架构进化的信号源,实现"从经验到结构"的自进化闭环。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Single-agent) + Context(Memory)
When:   Inter-test-time × ICL
How:    Reward-based(记忆反馈) · Offline+Online · Mixed · Process
Where:  General
Eval:   Adaptivity, Retention
```
