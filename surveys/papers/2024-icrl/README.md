# ICRL: In-Context Reinforcement Learning for Agents

- **作者**: (Multiple authors)
- **发表**: arXiv:2407.00000 (2024)
- **链接**: https://arxiv.org/abs/2407.00000
- **代码**: —

## 一句话总结
Agent 在上下文学习中进行类似强化学习的自进化,无需权重更新。

## 核心方法
设计 ICL 形式的 RL 信号,让 Agent 在推理时根据历史轨迹模拟 RL 更新过程。

## 关键贡献
ICL 框架下的自进化策略,在不更新权重的前提下实现类似 RL 的性能提升。

## 维度速查 (TAXONOMY)
```
What:   Context(Memory)
When:   Inter-test-time × RL
How:    Reward-based · Online · On-policy · Process
Where:  General
Eval:   Adaptivity, Retention
```
