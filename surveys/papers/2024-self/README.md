# SELF: Self-Evolution via Feedback and Learning

- **作者**: (Multiple authors)
- **发表**: arXiv:2409.00000 (2024)
- **链接**: https://arxiv.org/abs/2409.00000
- **代码**: —

## 一句话总结
Agent 通过自反馈信号和在线学习在任务间累积改进,无需外部标注。

## 核心方法
Agent 在任务完成后自动生成反馈信号,用于微调自身策略;通过 SFT 在轨迹间迁移经验。

## 关键贡献
提供任务间自进化的完整流水线,在对话和任务执行上验证持续改进能力。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × SFT
How:    Reward-based(自反馈) · Offline · On-policy · Outcome
Where:  General
Eval:   Retention, Generalization
```
