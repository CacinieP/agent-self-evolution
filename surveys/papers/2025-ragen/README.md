# RAGEN: Understanding and Evaluating Agent Reinforcement Learning

- **作者**: Zhiyuan Hu et al.
- **发表**: arXiv:2504.20073 (2025)
- **链接**: https://arxiv.org/abs/2504.20073
- **代码**: https://github.com/RAGEN-AI/RAGEN

## 一句话总结
面向多轮、带多 Agent 交互场景的 Agent RL 训练与评估框架,分析轨迹级信用分配难题。

## 核心方法
剖析多轮交互下轨迹 / 子目标的信用分配,提出针对性 RL 训练范式与多 Agent 评估方案。

## 关键贡献
为"Agent RL"提供训练 + 评测一体的框架,推动从单轮走向多轮、多 Agent 的进化训练研究。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Architecture
When:   Inter-test-time × RL
How:    Reward-based · Online · On-policy · Process/Hybrid
Where:  General
Eval:   Adaptivity, Generalization
```

> 💡 **点评 / 启发**:聚焦多轮交互下的"信用分配"难题——单步奖励如何回溯归因到前面若干步,这是 Agent RL 区别于单轮 RL 的核心难点。训练+评测一体,补足了方法论缺口。
>
> ⚠️ **局限 / 可质疑**:提出的方案是否真正解决信用分配,还是用启发式近似,需更多任务验证。框架较重,复现成本高。
>
> 📚 **来源**:基于摘要(未精读全文)。
