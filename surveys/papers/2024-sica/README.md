# SICA: A Self-Improving Coding Agent

- **作者**: Maxime Robeyns, Martin Szummer, Laurence Aitchison
- **发表**: arXiv:2504.15228 (2025)
- **链接**: https://arxiv.org/abs/2504.15228
- **代码**: —

## 一句话总结
自主编程 Agent 通过自我测试和修正实现编码能力的持续自进化。

## 核心方法
Agent 在代码生成后自动执行测试,根据结果自我反馈并迭代修正,无需人工介入。

## 关键贡献
证明编程任务中,Agent 可通过自生成的测试驱动自我改进。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Tool
When:   Intra-test-time × RL
How:    Reward-based(代码验证) · Online · On-policy · Outcome
Where:  Coding
Eval:   Adaptivity, Efficiency
```
