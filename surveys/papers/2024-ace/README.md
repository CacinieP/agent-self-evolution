# ACE: Agentic Context Engineering for Self-Improving Language Models

- **作者**: Zhang et al. (2025)
- **发表**: arXiv:2510.04618 (2025)
- **链接**: https://arxiv.org/abs/2510.04618
- **代码**: —

## 一句话总结
将上下文作为可进化的"游戏手册",Agent 通过模块化增量更新持续优化上下文。

## 核心方法
模块化 Agent 过程,上下文作为策略手册随时间累积和演化,支持离线 prompt 优化和在线记忆适配。

## 关键贡献
解决上下文 brevity bias 和 context collapse 问题,实现上下文驱动的自进化。

## 维度速查 (TAXONOMY)
```
What:   Context(Prompt)
When:   Inter-test-time × ICL
How:    Reward-based · Offline+Online · Mixed · Hybrid
Where:  General
Eval:   Generalization, Adaptivity
```
