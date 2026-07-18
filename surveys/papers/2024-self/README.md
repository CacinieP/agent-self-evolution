# SELF: Self-Evolution with Language Feedback

- **作者**: Lu et al. (2023)
- **发表**: arXiv:2310.00533 (2023)
- **链接**: https://arxiv.org/abs/2310.00533
- **代码**: —

## 一句话总结
Agent 通过语言反馈驱动自进化,任务间累积改进。

## 核心方法
自生成语言反馈信号→SFT→任务间持续改进,无需外部标注。

## 关键贡献
语言反馈驱动的自进化流水线,验证语言作为进化信号的可行性。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × SFT
How:    Reward-based(语言反馈) · Offline · On-policy · Outcome
Where:  General
Eval:   Retention, Generalization
```
