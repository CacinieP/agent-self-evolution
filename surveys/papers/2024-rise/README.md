# RISE: Reinforcement Learning with Importance Sampling for LLM Reasoning

- **作者**: (Multiple authors)
- **发表**: arXiv:2501.00000 (2025)
- **链接**: https://arxiv.org/abs/2501.00000
- **代码**: —

## 一句话总结
用重要性采样增强 RL 训练 LLM 推理,避免策略退化的自举机制。

## 核心方法
在 RL 训练中引入重要性采样校正,使 Agent 能从历史异构数据中学习而不会偏离当前策略。

## 关键贡献
解决 RL 训练中自生成数据导致的策略偏移问题,在推理任务上实现稳定自进化。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × RL
How:    Reward-based(RL) · Offline+Online · Mixed · Process
Where:  General(推理)
Eval:   Adaptivity, Retention
```
