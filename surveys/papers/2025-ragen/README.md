# RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning

- **作者**: Zhiyuan Hu et al.
- **发表**: arXiv:2504.20073 (2025)
- **链接**: https://arxiv.org/abs/2504.20073
- **代码**: https://github.com/mll-lab-nu/RAGEN

## 一句话总结
提出 StarPO(State-Thinking-Actions-Reward Policy Optimization)做多轮交互式 Agent RL,并基于 verl 复现 DeepSeek-R1 式的 agentic 训练,系统分析自进化中的稳定性/推理坍缩/奖励塑形问题。

## 核心方法
StarPO 框架支持多轮 rollout + 轨迹级奖励分配 + 策略更新;RAGEN 系统在其上做训练与评估,聚焦多轮交互下 Agent RL 的工程挑战(训练稳定性、推理坍缩、奖励塑造)。

## 关键贡献
为"Agent 自进化的多轮 RL"提供统一框架 + 可复现系统(重现 R1 路线),系统刻画了自进化训练中的失效模式。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × RL
How:    Reward-based · Online · On-policy · Hybrid
Where:  General
Eval:   Adaptivity, Generalization
```

> 💡 **点评 / 启发**:把 R1 的 RL 训练范式系统迁移到多轮 Agent 场景,StarPO 是对"轨迹级信用分配"的工程化回答。最实在的贡献是它**诚实地报告失效模式**(推理坍缩、训练不稳)——这对一个宣称"自进化"的方法是稀缺品质。
>
> ⚠️ **局限 / 可质疑**:多轮 RL 的稳定性仍主要靠工程 trick(奖励塑形/clip),理论根基薄弱;复现 R1 路线依赖大算力。泛化到新环境的能力未充分验证。
>
> 📚 **来源**:基于摘要 + GitHub(未精读全文,修正了标题与核心方法 StarPO)。
