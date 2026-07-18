# SCA: Self-Contrastive Agent Learning

- **作者**: Bowen Yu et al.
- **发表**: arXiv:2503.01203 (2025)
- **链接**: https://arxiv.org/abs/2503.01203
- **代码**: —

## 一句话总结
通过自对比学习在 Agent 轨迹中区分"好/差决策",无需人工标注即可提升 Agent 策略。

## 核心方法
收集自身任务执行轨迹,自动构造正负对(成功 vs 失败轨迹),用对比损失训练策略模型区分优劣行为。

## 关键贡献
证明自生成对比信号在 Agent 训练中可替代人工 reward,显著降低标注依赖。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × SFT
How:    Imitation/Contrastive · Offline · On-policy · Outcome
Where:  General
Eval:   Adaptivity, Generalization
```
