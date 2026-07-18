# ScoreFlow: Mastering LLM Agentic Workflows via Actor-Critic

- **作者**: Wang et al. (2025)
- **发表**: arXiv:2502.04306 (2025)
- **链接**: https://arxiv.org/abs/2502.04306
- **代码**: —

## 一句话总结
用 Actor-Critic 框架优化多步骤 Agent 工作流。

## 核心方法
构建工作流级别的 Actor-Critic,评估每个子步骤的贡献,优化整体执行策略。

## 关键贡献
工作流级 RL 减少冗余步骤提升成功率。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Multi-Agent)
When:   Inter-test-time × RL
How:    Reward-based(Actor-Critic) · Online · On-policy · Hybrid
Where:  General
Eval:   Efficiency, Generalization
```
