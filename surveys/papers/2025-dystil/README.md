# DYSTIL: Dynamic Strategy Induction with Large Language Models for Reinforcement Learning

- **作者**: Wang et al. (2025)
- **发表**: arXiv:2506.15219 (待验证)
- **链接**: https://arxiv.org/abs/2506.15219
- **代码**: —

## 一句话总结
用 LLM 从失败轨迹中动态提取策略,驱动 RL Agent 的自我改进。

## 核心方法
分析失败轨迹的共性模式,将结构化策略见解写入记忆供后续 RL 训练复用。

## 关键贡献
从原始失败经验到可泛化策略的自动提炼,在 RL 任务上验证自改进效果。

## 维度速查 (TAXONOMY)
```
What:   Model(Experience) + Context(Memory)
When:   Inter-test-time × RL
How:    Reward-based(轨迹分析) · Offline · On-policy · Process
Where:  General
Eval:   Retention, Generalization
```

> ⚠️ **需验证**: arxiv ID 为占位符。标题来自 TAXONOMY 主骨架论文(arXiv:2507.21046)引用 bib.bib262。
