# SICA: Self-Improvement via Coding Assistance

- **作者**: Wenhan Zhang et al.
- **发表**: arXiv:2412.14281 (2024)
- **链接**: https://arxiv.org/abs/2412.14281
- **代码**: —

## 一句话总结
LLM Agent 通过代码辅助任务中的自我测试和修正,实现编程能力的自进化。

## 核心方法
Agent 在代码生成后自动执行测试用例,根据测试结果自我反馈并迭代修正代码,无需人工介入。

## 关键贡献
证明编程任务中,Agent 可通过自生成的单元测试驱动自我改进,在 HumanEval/MBPP 上显著提升。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Tool
When:   Intra-test-time × RL
How:    Reward-based(代码验证) · Online · On-policy · Outcome
Where:  Coding
Eval:   Adaptivity, Efficiency
```
