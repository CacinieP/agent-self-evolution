# AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation

- **作者**: Dong Huang, Jie M. Zhang, Michael Luck, Qingwen Bu, Yuhao Qing, Heming Cui
- **发表**: arXiv:2312.13010 (2023)
- **链接**: https://arxiv.org/abs/2312.13010
- **代码**: —

## 一句话总结
三个协作 Agent 迭代生成、测试、精化代码,在 HumanEval 上达到 96.3%。

## 核心方法
Programmer/Test Designer/Test Executor 三个 Agent 协作,通过测试反馈循环驱动代码自修正。

## 关键贡献
多 Agent 协作+测试驱动在 HumanEval/MBPP 上超越单 Agent 方法。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Multi-Agent)
When:   Intra-test-time × ICL
How:    Reward-based(测试结果) · Online · On-policy · Process
Where:  Coding
Eval:   Adaptivity, Efficiency
```
