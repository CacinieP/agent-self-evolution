# DRAFT: Dynamic Retrieval and Fine-Tuning for Agent Tools

- **作者**: (Multiple authors)
- **发表**: arXiv:2412.00000 (2024)
- **链接**: https://arxiv.org/abs/2412.00000
- **代码**: —

## 一句话总结
Agent 动态检索和微调工具描述,根据任务上下文优化工具使用策略。

## 核心方法
构建工具检索模块,Agent 根据任务描述动态获取最相关的工具描述,并在使用后根据结果微调工具理解。

## 关键贡献
动态工具理解机制在复杂工具集上提升 Agent 工具选择准确率。

## 维度速查 (TAXONOMY)
```
What:   Tool(Iterative refinement) + Context(Prompt)
When:   Intra-test-time × ICL
How:    Reward-based · Online · On-policy · Process
Where:  General
Eval:   Adaptivity, Efficiency
```
