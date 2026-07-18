# ProTeGi: Prompt Engineering with Targeted Improvement via Genetic Improvement

- **作者**: Chrisantha Fernando, Tomoki Hayashi, Henryk Michalewski, Satoshi Takahashi
- **发表**: arXiv:2402.11602 (2024)
- **链接**: https://arxiv.org/abs/2402.11602
- **代码**: —

## 一句话总结
用遗传算法对 prompt 进行变异/选择/交叉,自动优化特定任务的提示词。

## 核心方法
将 prompt 视为"基因组",通过遗传编程的变异和交叉生成新 prompt,用验证集准确率作为适应度函数,迭代进化最优提示。

## 关键贡献
首次将遗传编程系统性地用于 prompt 优化,在 NLP 基准上超过手工调优和单步搜索方法。

## 维度速查 (TAXONOMY)
```
What:   Context(Prompt)
When:   Inter-test-time × ICL
How:    Population-based · Offline · Off-policy · Outcome
Where:  General
Eval:   Generalization
```
