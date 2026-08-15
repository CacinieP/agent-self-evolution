# Transformer-Squared: Self-Adaptive LLMs

- **作者**: Qi Sun et al.
- **发表**: arXiv:2501.06252 (2025)
- **链接**: https://arxiv.org/abs/2501.06252
- **代码**: —

## 一句话总结
推理时实时自适配:按任务选择性调整权重的奇异分量,两阶段完成自我进化。

## 核心方法
对权重做 SVD 分解;推理中先提示模型自我识别任务属性,再在线选择/组合 LoRA 专家实时重组权重。

## 关键贡献
无需重新训练的实时任务自适配,在推理与理解任务上同时提升性能与效率。

## 维度速查 (TAXONOMY)
```
What:   Model(参数)
When:   Intra-test-time × 自适配
How:    Self-adaptive(SVD+专家选择) · Online · Process
Where:  General
Eval:   Adaptivity, Efficiency
```
