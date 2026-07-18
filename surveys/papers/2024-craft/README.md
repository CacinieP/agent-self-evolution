# CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets

- **作者**: Yuan et al.
- **发表**: ICLR 2024 / arXiv:2309.17428
- **链接**: https://arxiv.org/abs/2309.17428
- **代码**: —

## 一句话总结
LLM 自主创建和检索专用工具集,通过工具化定制能力。

## 核心方法
Agent 将复杂任务分解为可工具化的子任务,自动创建对应工具并存储在可检索工具集中。

## 关键贡献
工具创建+检索的双阶段框架,在领域特定任务上显著提升 LLM 性能。

## 维度速查 (TAXONOMY)
```
What:   Tool(Discovery & Creation)
When:   Intra-test-time × ICL
How:    Reward-based · Online · On-policy · Process
Where:  General
Eval:   Adaptivity, Generalization
```
