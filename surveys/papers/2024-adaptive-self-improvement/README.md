# Adaptive Self-Improvement LLM Agentic System for ML Library Development

- **作者**: Zhang et al. (2025)
- **发表**: arXiv:2502.02534 (2025)
- **链接**: https://arxiv.org/abs/2502.02534
- **代码**: —

## 一句话总结
SWE Agent 根据环境反馈自适应调整行为策略,在 ML 库开发中持续自改进。

## 核心方法
构建反馈感知自调整模块,Agent 在执行中根据任务成功/失败信号动态调整策略参数。

## 关键贡献
环境驱动的自适应自改进在 ML 库开发任务上减少人工调参需求。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Tool
When:   Inter-test-time × RL
How:    Reward-based · Online · On-policy · Outcome
Where:  Coding
Eval:   Adaptivity, Efficiency
```
