# Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models (SPIN)

- **作者**: Zixiang Chen, Yihe Deng, Huizhuo Yuan, Kaixuan Ji, Quanquan Gu (UCLA)
- **发表**: NeurIPS 2024 / arXiv:2401.01335
- **链接**: https://arxiv.org/abs/2401.01335
- **代码**: https://github.com/uclaml/SPIN

## 一句话总结
让模型与"上一轮的自己"对弈:区分自生成回答与人类 ground truth,迭代微调直至收敛。

## 核心方法
以 SFT 模型为对手生成响应,训练目标是"判别自身响应 vs 真值",用 DPO 式目标迭代;理论保证收敛到目标分布。

## 关键贡献
不依赖人类标注或更强教师即可显著提升弱模型,部分场景超越带人类偏好的 DPO,是 self-play 训练范式的代表。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × SFT/RL
How:    Population(Self-Play) · Offline · Mixed · Outcome
Where:  General
Eval:   Adaptivity, Generalization(MT-Bench 等)
```

> 个人点评 / 启发 待补充。
