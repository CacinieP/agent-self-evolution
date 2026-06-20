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

> 💡 **点评 / 启发**:把"作者/审稿人/改写者"三个角色压进同一个模型,prompt 即程序。最优雅之处是零外部依赖——任何能生成+评分的 LLM 立刻可用。
>
> ⚠️ **局限 / 可质疑**:同一模型既造又评,存在系统性自盲点(自己看不到自己的盲区)。效果高度依赖初始输出"方向对",若初稿南辕北辙,自反馈会强化错误方向。
>
> 📚 **来源**:精读原文 + 仓库 self_refine 原型实践。
