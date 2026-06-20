# PromptAgent: Strategic Planning with Language Models Enables Expert-Level Prompt Optimization

- **作者**: Xinyuan Wang et al.
- **发表**: ICLR 2024 / arXiv:2310.16427
- **链接**: https://arxiv.org/abs/2310.16427
- **代码**: https://github.com/xinyuanwangcs/promptagent

## 一句话总结
把 prompt 优化建模为"策略规划"问题,用 MCTS 系统化探索提示空间,自动得到专家级 prompt。

## 核心方法
将 prompt 优化视为 MCTS:沿错误反馈回溯、扩展候选 prompt 节点、用模拟评估 → 逐步收敛到高质量专家级指令;利用错误样本驱动探索。

## 关键贡献
证明 MCTS 式战略规划能产出优于 APE/OPRO 的专家级 prompt,是搜索式 prompt 优化的代表。

## 维度速查 (TAXONOMY)
```
What:   Context(Prompt Optimization)
When:   Inter-test-time
How:    Population(Search-based, MCTS) · Offline · On-policy · Outcome
Where:  General
Eval:   Adaptivity, Generalization
```

> 💡 **点评 / 启发**:把 prompt 优化建模成博弈树搜索,用错误信号驱动探索——比 APE 的离散打分更有方向性。MCTS 在 prompt 空间的成功复用,说明"搜索"是自进化的通用骨架。
>
> ⚠️ **局限 / 可质疑**:MCTS 每次模拟都要调模型,成本高;树深度受限于预算。专家级 prompt 的"专家"标准仍来自任务集,泛化性存疑。
>
> 📚 **来源**:基于摘要 + ICLR 2024 转述(未精读全文)。
