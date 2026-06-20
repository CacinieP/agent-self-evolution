# AgentTuning: Enabling Generalized Agent Abilities for LLMs

- **作者**: Aohan Zeng, Mingdao Liu, Zehui Chen, et al. (Tsinghua / 智谱)
- **发表**: arXiv:2310.12823
- **链接**: https://arxiv.org/abs/2310.12823
- **代码**: https://github.com/THUDM/AgentTuning

## 一句话总结
用 Agent 通用任务轨迹做 SFT + 通用 NLP 任务做 RL,让模型获得可迁移到未见任务的"Agent 能力"。

## 核心方法
构建多种 Agent 任务轨迹数据集做 SFT,再用 RL 在通用任务上对齐,平衡"Agent 专精"与"通用不退化"。

## 关键贡献
实证 Agent 能力可被训练并迁移到未见 Agent 任务,是 Agent 训练循环方向的早期代表。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × SFT + RL
How:    Reward-based · Offline · Mixed · Outcome
Where:  General
Eval:   Generalization(跨任务迁移)
```

> 个人点评 / 启发 待补充。
