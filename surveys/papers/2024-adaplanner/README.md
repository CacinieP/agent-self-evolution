# AdaPlanner: Adaptive Planning from Feedback with Language Models

- **作者**: Haotian Sun et al.
- **发表**: arXiv:2305.16653 (2023, NeurIPS 2023)
- **链接**: https://arxiv.org/abs/2305.16653
- **代码**: —

## 一句话总结
Agent 在执行过程中根据语言反馈自适应调整规划,实现实时计划自进化。

## 核心方法
闭环规划:先粗规划再执行,依据环境反馈与自我评估动态重规划,自适应调整行动策略。

## 关键贡献
在线自适应规划在多步任务中显著优于静态预规划。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Single-agent)
When:   Intra-test-time × ICL
How:    Reward-based(语言反馈) · Online · On-policy · Process
Where:  General
Eval:   Adaptivity
```
