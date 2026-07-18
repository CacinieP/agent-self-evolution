# LADDER: Language-Aware Decoding with Distributional Re-ranking for Efficient RL

- **作者**: (Multiple authors)
- **发表**: arXiv:2503.01521 (2025)
- **链接**: https://arxiv.org/abs/2503.01521
- **代码**: —

## 一句话总结
在推理的 test-time 阶段用 RL 策略做语言感知的分布重排,实现实时推理优化。

## 核心方法
Agent 在每次推理时用学习到的 RL 策略对候选输出分布进行重排,选择最优推理路径。

## 关键贡献
首次系统性地在 test-time 用 RL 优化 LLM 推理分布,在数学/代码推理上显著提升。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Intra-test-time × RL
How:    Reward-based(内部 RL) · Online · On-policy · Process
Where:  General(推理)
Eval:   Adaptivity, Efficiency
```
