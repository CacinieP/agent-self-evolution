# ProTeGi: Automatic Prompt Optimization with Textual Gradients

- **作者**: Reid Pryzant, Dan Iter, Zhiting Hu
- **发表**: arXiv:2305.03495 (2023)
- **链接**: https://arxiv.org/abs/2305.03495
- **代码**: —

## 一句话总结
用语言"梯度"(文本修正)自动优化 prompt,形成文本梯度下降。

## 核心方法
模型生成自然语言"修正"作为 prompt 编辑,迭代优化直到验证集性能最佳。

## 关键贡献
文本梯度下降在 prompt 优化上超越手工调优和离散搜索方法。

## 维度速查 (TAXONOMY)
```
What:   Context(Prompt)
When:   Inter-test-time × ICL
How:    Reward-based(文本梯度) · Offline · Off-policy · Outcome
Where:  General
Eval:   Generalization
```
