# SCA: Self-Challenging Language Model Agents

- **作者**: Yifei Zhou, Sergey Levine, Jason Weston, Xian Li, Sainbayar Sukhbaatar
- **发表**: arXiv:2506.01716 (2025)
- **链接**: https://arxiv.org/abs/2506.01716
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
