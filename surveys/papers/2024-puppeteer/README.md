# Multi-Agent Collaboration via Evolving Orchestration (Puppeteer)

- **作者**: Yufan Dang et al.
- **发表**: arXiv:2505.19591 (2025)
- **链接**: https://arxiv.org/abs/2505.19591
- **代码**: —

## 一句话总结
"提线木偶"范式:中央编排器(puppeteer)随任务状态动态指挥多 Agent(puppets),编排策略可进化。

## 核心方法
集中式编排器按任务状态调度各 Agent,通过强化学习(含步级成本惩罚)训练编排策略。

## 关键贡献
在协作层面实现架构进化,随任务复杂度与 Agent 数量增长仍保持可扩展性。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Multi-Agent)
When:   Inter-test-time × RL
How:    Reward-based(RL) · Online · On-policy · Outcome
Where:  General
Eval:   Adaptivity, Efficiency
```
