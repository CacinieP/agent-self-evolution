# AgentSquare: Automatic LLM Agent Search in Modular Design Space

- **作者**: Shang et al. (Tsinghua FIB Lab)
- **发表**: ICLR 2025 / arXiv:2410.06153
- **链接**: https://arxiv.org/abs/2410.06153
- **代码**: https://github.com/tsinghua-fib-lab/agentsquare

## 一句话总结
把 Agent 设计拆成模块(规划/记忆/工具/动作),通过模块进化 + 模块重组自动搜索高性能 Agent。

## 核心方法
模块化设计空间(MoLAS):每个 Agent = 多模块组合 → 模块进化(迭代改进单模块)+ 模块重组(跨 Agent 交换模块)→ 按表现选择,高效搜出新颖且强的配置。

## 关键贡献
把"Agent 架构搜索"落到模块级,比整体搜索更高效,是 Architecture 自进化的代表性方法。

## 维度速查 (TAXONOMY)
```
What:   Architecture(模块化搜索)
When:   Inter-test-time
How:    Population(Evolutionary, 模块进化+重组) · Online · On-policy
Where:  General
Eval:   Adaptivity, Generalization, Efficiency
```

> 💡 **点评 / 启发**:把架构搜索落到"模块"粒度,比 ADAS 整体搜索更高效——进化单模块 + 重组跨 Agent,组合空间远小于整体搜索。工程上更可控。
>
> ⚠️ **局限 / 可质疑**:模块边界是预设的(规划/记忆/工具/动作),搜索不到预设之外的结构。仍是"已知模块的新组合",真正新颖机制难以涌现。
>
> 📚 **来源**:基于摘要 + ICLR 2025 转述(未精读全文)。
