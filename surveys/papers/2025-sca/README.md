# SCA: Self-Challenging Language Model Agents

- **作者**: Zhou et al.
- **发表**: NeurIPS 2025
- **链接**: https://arxiv.org/abs/2503.01203
- **代码**: —

## 一句话总结
Agent 交替扮演挑战者(生成 Code-as-Task 问题)和执行者(解决问题),用成功轨迹自训练。

## 核心方法
自生成可执行代码任务→执行→筛选成功轨迹→微调自身,实现任务级自进化。

## 关键贡献
自挑战机制在复杂多步任务上显著提升,验证"自我出题自我做题"范式。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × SFT
How:    Imitation/Experience · Offline · On-policy · Outcome
Where:  General
Eval:   Adaptivity, Generalization
```

> ⚠️ **需验证**: arxiv ID 为占位符,需替换为正确编号。标题和描述来自 TAXONOMY 主骨架论文(arXiv:2507.21046)引用。
