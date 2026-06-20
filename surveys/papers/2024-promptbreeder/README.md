# Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution

- **作者**: Chris Fernando et al. (Google DeepMind)
- **发表**: ICML 2024 / arXiv:2309.16797
- **链接**: https://arxiv.org/abs/2309.16797
- **代码**: —

## 一句话总结
用进化算法同时进化"任务提示"和"变异提示"本身:LLM 既是被优化的对象,也是变异算子,实现自我指涉的提示进化。

## 核心方法
种群 = (任务提示, 变异提示) 对;每代用 LLM 按变异提示对任务提示做变异 → 在训练集上评估适应度 → 优胜劣汰;变异提示自身也参与进化,故"自我指涉"。

## 关键贡献
提出提示空间的自我指涉进化,把 prompt 优化推向"自动化发现"高度,在推理/指令跟随上超越手工 prompt。

## 维度速查 (TAXONOMY)
```
What:   Context(Prompt Optimization)
When:   Inter-test-time
How:    Population(Evolutionary) · Online · On-policy · Outcome
Where:  General
Eval:   Adaptivity, Generalization
```

> 💡 **点评 / 启发**:"自我指涉"是精髓——变异 prompt 本身也在进化,所以系统会越变越"会变"。这是少数把进化算法的元层级做到位的 prompt 工作。
>
> ⚠️ **局限 / 可质疑**:进化方向完全由适应度函数(任务表现)驱动,若任务集窄,种群会收敛到过拟合的 prompt。算力成本高(每代多次模型调用)。
>
> 📚 **来源**:基于摘要 + ICML 2024 转述(未精读全文)。
