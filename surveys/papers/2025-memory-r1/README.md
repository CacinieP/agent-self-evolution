# Memory-R1: Enhancing LLM Agents to Manage and Utilize Memories via Reinforcement Learning

- **作者**: Sikuan Yan, Xuyang Yang et al.
- **发表**: arXiv:2508.19828 (2025)
- **链接**: https://arxiv.org/abs/2508.19828
- **代码**: —

## 一句话总结
用 RL 训练 LLM 主动"管理"外部记忆——学会何时读、何时写、写什么,而非被动检索。

## 核心方法
给 LLM 配外部记忆库 + 可学习的记忆操作动作(读/写/更新),用 RL(任务奖励)训练它主动管理记忆,支持长程持久推理。

## 关键贡献
把"记忆管理"本身变成 RL 可学的技能,而非固定规则,是 Memory + RL 自进化的新范式。

## 维度速查 (TAXONOMY)
```
What:   Context(Memory) + Model(Policy)
When:   Inter-test-time × RL
How:    Reward-based(任务奖励) · Online · On-policy · Outcome
Where:  General(长程任务)
Eval:   Retention, Adaptivity, Efficiency
```

> 个人点评 / 启发 待补充。
