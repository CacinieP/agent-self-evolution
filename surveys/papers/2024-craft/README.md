# CRAFT: Concept Recursive Activation for Task-grounded Fine-tuning

- **作者**: Prithviraj Sen et al.
- **发表**: arXiv:2405.00295 (2024)
- **链接**: https://arxiv.org/abs/2405.00295
- **代码**: —

## 一句话总结
通过概念递归激活机制,LLM Agent 自主生成和精化工具以解决复杂任务。

## 核心方法
Agent 将复杂任务递归分解为可工具化的子概念,自主调用或创建对应工具执行子任务并组合结果。

## 关键贡献
提出概念递归框架让 Agent 自主发现工具需求并精化工具,在复杂推理链上实现自给自足。

## 维度速查 (TAXONOMY)
```
What:   Tool(Iterative refinement) + Context(Prompt)
When:   Intra-test-time × ICL
How:    Reward-based · Online · On-policy · Process
Where:  General
Eval:   Adaptivity, Efficiency
```
