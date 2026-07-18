# AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation

- **作者**: Dong Huang, Jie M. Zhang, Michael Luck, Qingwen Bu, Yuhao Qing, Heming Cui
- **发表**: arXiv:2312.13010 (2023)
- **链接**: https://arxiv.org/abs/2312.13010
- **代码**: —

## 一句话总结
三个协作 Agent(程序员/测试设计器/测试执行器)迭代生成、测试、精化代码,在 HumanEval 上达到 96.3% pass@1。

## 核心方法
Programmer Agent 写代码 → Test Designer 生成测试用例 → Test Executor 运行测试并反馈,迭代直到通过。

## 关键贡献
多 Agent 协作+测试驱动在 HumanEval/MBPP 上超越单 Agent 方法,降低 token 开销。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Multi-Agent)
When:   Intra-test-time × ICL
How:    Reward-based(测试结果) · Online · On-policy · Process
Where:  Coding
Eval:   Adaptivity, Efficiency
```
