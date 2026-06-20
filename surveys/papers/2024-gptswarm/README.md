# GPTSwarm: Language Agents as Optimizable Graphs

- **作者**: Mingchen Zhuge et al.
- **发表**: ICML 2024 / arXiv:2402.16823
- **链接**: https://arxiv.org/abs/2402.16823
- **代码**: https://github.com/metauto-ai/GPTSwarm

## 一句话总结
把多 Agent 系统建模成"可优化计算图":节点是 LLM 推理/工具调用,边是协作,自动优化图结构让它自我改进。

## 核心方法
两类自动优化器:① 节点级 — 优化各节点 LLM 的 prompt;② 边级 — 调整 Agent 间连接(增删边)优化编排;联合优化让多 Agent swarm 性能持续提升。

## 关键贡献
用"图优化"统一并自动化多 Agent 系统设计,自我标榜"The First Self-Improving agents",多 Agent 架构进化的代表作。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Multi-Agent)
When:   Inter-test-time
How:    Population(Search-based) + Reward-based · Online · On-policy · Outcome
Where:  General
Eval:   Adaptivity, Generalization
```

> 个人点评 / 启发 待补充。
