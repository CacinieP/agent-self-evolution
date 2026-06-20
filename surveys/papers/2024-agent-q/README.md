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

> 💡 **点评 / 启发**:MCTS 提供探索,self-critique 提供过滤,DPO 做更新——三者组合是"搜索 + RL"的成熟范式。一天内 20%→90% 的真实预订任务提升,是 Agent 自进化在真实场景的有力证据。
>
> ⚠️ **局限 / 可质疑**:MCTS 在网页动作空间分支巨大,搜索成本高;90% 是单一任务类型,泛化性未充分验证。作者含 DeepMind 核心成员,工程资源门槛极高。
>
> 📚 **来源**:基于摘要 + 社区讨论(未精读全文)。
