# AFlow: Automating Agentic Workflow Generation

- **作者**: Jinghan Zhang, Xiang Shu, et al.
- **发表**: ICLR 2025 / arXiv:2410.10762
- **链接**: https://arxiv.org/abs/2410.10762
- **代码**: —

## 一句话总结
把 Agent 工作流表示成代码,用蒙特卡洛树搜索(MCTS)自动探索并迭代出更优的工作流。

## 核心方法
工作流以代码形式表达 → 用 MCTS 在工作流空间高效搜索(选择/扩展/评估/回溯)→ 据评估指标迭代精炼,跨领域自动发现有效 workflow。

## 关键贡献
用 MCTS 把"工作流设计"自动化、可优化,最小化人工设计;架构/工作流进化方向的代表。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Workflow optimization)
When:   Inter-test-time
How:    Population(Search-based, MCTS) · Online · On-policy
Where:  General(多领域)
Eval:   Adaptivity, Efficiency, Generalization
```

> 个人点评 / 启发 待补充。
