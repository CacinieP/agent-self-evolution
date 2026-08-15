# Reward Is Enough: LLMs Are In-Context Reinforcement Learners (ICRL Prompting)

- **作者**: Kefan Song et al.
- **发表**: arXiv:2506.06303 (2025)
- **链接**: https://arxiv.org/abs/2506.06303
- **代码**: —

## 一句话总结
多轮 ICRL 提示引导 LLM 在推理时执行"上下文内强化学习",无需参数更新即可自我改进。

## 核心方法
每轮生成后用奖励反馈重构下一轮提示,让 LLM 在前向传播中模拟 RL 的策略改进过程。

## 关键贡献
理论与实验论证 LLM 天然具备上下文内 RL 能力,测试时自我改进成为通用范式。

## 维度速查 (TAXONOMY)
```
What:   Context(Prompt)
When:   Intra-test-time × RL
How:    Reward-based · Online · On-policy · Outcome
Where:  General
Eval:   Adaptivity
```
