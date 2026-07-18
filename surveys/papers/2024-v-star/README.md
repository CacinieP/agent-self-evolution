# V-STaR: Verifiable Self-Taught Reasoner

- **作者**: (Multiple authors)
- **发表**: arXiv:2502.02566 (2025)
- **链接**: https://arxiv.org/abs/2502.02566
- **代码**: —

## 一句话总结
通过可验证自示范实现推理能力的自举,用验证模块筛选高质量推理范例。

## 核心方法
Agent 自生成推理轨迹,用内置验证模块标注正确性,将高置信推理作为自示范数据微调自身。

## 关键贡献
引入验证步骤筛选自示范质量,解决 STaR 系列中"错误示范污染"的核心问题。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × SFT
How:    Imitation · Offline · On-policy · Outcome
Where:  General(推理)
Eval:   Generalization
```
