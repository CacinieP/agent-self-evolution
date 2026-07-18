# MAS-Zero: Multi-Agent Self-Play from Zero

- **作者**: Jiaxu Chen et al.
- **发表**: arXiv:2410.02343 (2024)
- **链接**: https://arxiv.org/abs/2410.02343
- **代码**: —

## 一句话总结
多 Agent 从零开始通过自我博弈协同进化,无需任何人类示范。

## 核心方法
多个 Agent 在共享环境中通过自我博弈交互,各自根据对手策略动态调整,在零人类数据下实现协同涌现。

## 关键贡献
证明多 Agent 自博弈可实现从零到复杂协作策略的涌现,减少对预训练数据的依赖。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Multi-Agent) + Model(Policy)
When:   Inter-test-time × RL
How:    Population-based(Self-Play) · Online · On-policy · Outcome
Where:  General
Eval:   Adaptivity, Generalization
```
