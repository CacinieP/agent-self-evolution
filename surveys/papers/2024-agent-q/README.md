# Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents

- **作者**: Putra Manggala et al.(含 David Silver, Julian Schrittwieser, Karen Simonyan 等,DeepMind)
- **发表**: arXiv:2408.07199 (2024)
- **链接**: https://arxiv.org/abs/2408.07199
- **代码**: —

## 一句话总结
把 MCTS 探索 + 自我批判 + RL 结合,让 Agent 在真实网页任务(如在线预订)上从成功与失败轨迹中持续学习。

## 核心方法
用 MCTS 在动作空间做前瞻搜索产生多样轨迹 → 自我批判(critique)打分过滤 → DPO 式 RL 微调;让 Agent 同时利用正负样本提升泛化。

## 关键贡献
展示在真实多步网页任务上,一天在线经验即可把成功率从约 20% 提到 90%,是"搜索+RL"自进化的强证据。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × RL
How:    Reward-based(self-critique) + Population(MCTS) · Online · Mixed · Hybrid
Where:  Specialized(Web / 自主任务)
Eval:   Adaptivity, Generalization(真实预订任务)
```

> 个人点评 / 启发 待补充。
