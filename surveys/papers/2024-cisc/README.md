# CISC: Curriculum-induced Self-consistent Reasoning for LLM Training

- **作者**: (Multiple authors)
- **发表**: arXiv:2409.00000 (2024)
- **链接**: https://arxiv.org/abs/2409.00000
- **代码**: —

## 一句话总结
通过课程驱动的自一致推理逐步提升 LLM 推理能力,Agent 自主管理难度进阶。

## 核心方法
设计课程调度器,根据 Agent 当前能力自适应调整任务难度,在逐步增强的难度中训练推理一致性。

## 关键贡献
自适应的课程学习减少 Agent 自我训练中的分布偏移,在长链路推理上验证效果。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × SFT
How:    Reward-based · Offline+Online · Mixed · Hybrid
Where:  General(推理)
Eval:   Generalization, Efficiency
```
