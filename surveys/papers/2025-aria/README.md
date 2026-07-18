# ARIA: Autoregressive Iterative Alignment for Reasoning

- **作者**: (Multiple authors)
- **发表**: arXiv:2501.11591 (2025)
- **链接**: https://arxiv.org/abs/2501.11591
- **代码**: —

## 一句话总结
通过迭代式自对齐机制让 LLM 自主优化推理过程,无需外部验证信号。

## 核心方法
模型在推理时迭代对比自身输出,利用内部一致性信号区分正确与错误推理步骤。

## 关键贡献
在零人工标注场景下实现推理链的自动对齐和优化,验证 LLM 内部的自我校准能力。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Intra-test-time × ICL
How:    Reward-based(内部一致性) · Online · On-policy · Process
Where:  General(推理)
Eval:   Adaptivity
```
