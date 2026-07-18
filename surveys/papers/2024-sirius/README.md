# SiriuS: Synergistic Instruction Understanding and Self-Refinement

- **作者**: (Multiple authors)
- **发表**: arXiv:2410.00000 (2024)
- **链接**: https://arxiv.org/abs/2410.00000
- **代码**: —

## 一句话总结
通过协同指令理解与自我精化,LLM 在不依赖外部反馈的情况下自主优化输出质量。

## 核心方法
Agent 并行执行指令理解和自我精化,两个模块协同工作逐步提升输出质量。

## 关键贡献
协同自精化在多个 NLP 任务上验证效果,减少对人工反馈的依赖。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Context(Prompt)
When:   Inter-test-time × SFT
How:    Reward-based(自评估) · Offline · On-policy · Outcome
Where:  General
Eval:   Generalization, Efficiency
```
