# Self-Refine: Iterative Refinement with Self-Feedback

- **作者**: Aman Madaan et al. (CMU / AllenAI)
- **发表**: NeurIPS 2023 / arXiv:2303.17651
- **链接**: https://arxiv.org/abs/2303.17651
- **代码**: https://github.com/madaan/self-refine

## 一句话总结
模型对自己的输出给反馈,再据此迭代改进,全程零额外训练 / 零外部监督。

## 核心方法
同一模型三步循环:生成 → 自评(产生具体可执行反馈)→ 据反馈重新生成,直到满意或达到上限。

## 关键贡献
证明仅靠 in-context 的自反馈即可在多类任务提升输出质量,是 self-refinement 范式的代表性工作。

## 维度速查 (TAXONOMY)
```
What:   Context(Prompt / in-context)
When:   Intra-test-time × ICL
How:    Reward-based(自评语言反馈) · Online · On-policy · Outcome
Where:  General
Eval:   Adaptivity
```

> 个人点评 / 启发 待补充。
