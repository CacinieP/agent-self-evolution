# V-STaR: Training Verifiers for Self-Taught Reasoners

- **作者**: Arian Hosseini, Xingdi Yuan, Nikolay Malkin, Aaron Courville, Alessandro Sordoni, Rishabh Agarwal
- **发表**: arXiv:2402.06457 (2024)
- **链接**: https://arxiv.org/abs/2402.06457
- **代码**: —

## 一句话总结
用正确+错误的自生成解训练验证器(DPO),推理时选最优解,迭代提升推理能力。

## 核心方法
自生成推理轨迹→训练验证器区分正负解→推理时选最优候选→迭代改进。利用错误解的负信号。

## 关键贡献
解决 STaR 丢弃错误解浪费信号的问题,在代码/数学推理上 4-17% 提升。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × SFT
How:    Imitation + Reward-based(DPO验证器) · Offline · On-policy · Outcome
Where:  General(推理)
Eval:   Generalization
```
