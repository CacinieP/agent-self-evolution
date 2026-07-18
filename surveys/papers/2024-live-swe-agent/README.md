# Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?

- **作者**: Xia et al. (2025)
- **发表**: arXiv:2511.13646 (2025)
- **链接**: https://arxiv.org/abs/2511.13646
- **代码**: —

## 一句话总结
SWE Agent 在真实代码库中实时自我进化,通过代码审查和测试反馈持续改进。

## 核心方法
Agent 自主提交代码变更,通过 CI/CD 测试和代码审查反馈驱动代码策略自改进。

## 关键贡献
真实环境下的持续自进化 SWE Agent。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Single-agent) + Model(Policy)
When:   Inter-test-time × RL
How:    Reward-based(测试+审查) · Online · On-policy · Hybrid
Where:  Coding
Eval:   Adaptivity, Retention
```
