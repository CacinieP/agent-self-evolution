# PAG: Partial-Attention Guidance for Efficient Agent Learning

- **作者**: Yifan Zhang et al.
- **发表**: arXiv:2410.00139 (2024)
- **链接**: https://arxiv.org/abs/2410.00139
- **代码**: —

## 一句话总结
通过部分注意力引导在复杂观察空间中高效训练 Agent,减少自进化计算开销。

## 核心方法
设计部分注意力机制,让 Agent 只关注任务相关的观察子集,降低训练时的有效状态空间。

## 关键贡献
在保持性能的同时大幅降低 Agent 训练计算量,提升自进化效率。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Architecture
When:   Inter-test-time × RL
How:    Reward-based · Online · On-policy · Outcome
Where:  General
Eval:   Efficiency, Adaptivity
```
