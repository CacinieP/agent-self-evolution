# Nature-Inspired Population-Based Evolution of Large Language Models (GENOME)

- **作者**: Yiqun Zhang et al.
- **发表**: arXiv:2503.01155 (2025)
- **链接**: https://arxiv.org/abs/2503.01155
- **代码**: —

## 一句话总结
用遗传算法等自然启发的群体进化直接在参数空间优化 LLM,无需梯度。

## 核心方法
维护 LLM 权重"种群",施加选择/交叉/变异算子迭代进化;GENOME+ 进一步引入粒子群优化的继承机制与集成方法。

## 关键贡献
证明无梯度群体进化可有效提升模型能力,为参数级自进化开辟新路径。

## 维度速查 (TAXONOMY)
```
What:   Model(参数/权重)
When:   Inter-test-time × 进化算法
How:    Population-based(Evolutionary) · Offline · Outcome
Where:  General
Eval:   Adaptivity, Efficiency
```
