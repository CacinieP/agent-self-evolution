# Self-Rewarding Language Models

- **作者**: Weizhe Yuan et al. (Meta)
- **发表**: ICML 2024 / arXiv:2401.10020
- **链接**: https://arxiv.org/abs/2401.10020
- **代码**: https://github.com/lucidrains/self-rewarding-lm-pytorch

## 一句话总结
用 LLM-as-a-Judge 让模型给自己生成偏好奖励,迭代进行 DPO 训练,无需外部奖励模型。

## 核心方法
每轮:模型对 prompt 生成多候选 → 自身作为裁判打分 → 构造偏好对 → DPO 微调;判断与生成能力同步提升。

## 关键贡献
提出"自我奖励"闭环,实证判断(judge)能力随迭代持续提升,展示出走向自我改进对齐的潜在线索。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × RL(DPO)
How:    Reward-based(LLM-as-Judge 自奖励) · Offline · Mixed · Outcome
Where:  General
Eval:   Adaptivity, Generalization(AlpacaEval 2 / MT-Bench / LLM-as-Judge)
```

> 💡 **点评 / 启发**:最妙的点是 judge 能力随迭代**同步**提升——模型越练,自评越准,形成正向循环。这暗示"判断力"和"生成力"可以互相喂养。
>
> ⚠️ **局限 / 可质疑**:**自我强化偏差**是结构性风险——自己评自己易陷入"互相吹捧"的回音室,长程后 reward 可能与真实质量脱钩。Meta 后续 Meta-Rewarding(2407.19594)正是在补这个洞。
>
> 📚 **来源**:基于原文摘要 + 方法节精读 + 社区复现讨论。
