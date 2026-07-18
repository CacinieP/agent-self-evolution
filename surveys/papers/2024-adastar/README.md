# AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners

- **作者**: Woosung Koh, Wonbeen Oh, Jaein Jang, MinHyung Lee et al.
- **发表**: NeurIPS 2025 / arXiv:2505.16322
- **链接**: https://arxiv.org/abs/2505.16322
- **代码**: —

## 一句话总结
自适应采样原则平衡训练分布,动态调整难度匹配模型能力,训练 Self-Taught Reasoner。

## 核心方法
两个自适应采样原则:(1)平衡多样化的训练样本分布;(2)动态调整难度匹配模型当前能力。

## 关键贡献
在 6 个 benchmark 上均获最佳准确率,平均节省 58.6% 训练 FLOPs。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × SFT
How:    Imitation · Offline · On-policy · Outcome
Where:  General(推理)
Eval:   Generalization, Efficiency
```
