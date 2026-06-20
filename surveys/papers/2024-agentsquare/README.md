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

> 个人点评 / 启发 待补充。
