# Agent Workflow Memory (AWM)

- **作者**: Z. Wang et al.
- **发表**: ICML 2025 / arXiv:2409.07429
- **链接**: https://arxiv.org/abs/2409.07429
- **代码**: —

## 一句话总结
Agent 从过往任务轨迹中归纳出可复用的"工作流(recipe)",新任务时检索匹配的工作流来指导行动。

## 核心方法
归纳常用 routine 为 workflow 存入记忆库 → 新任务时按任务驱动检索相关 workflow 注入提示;支持 offline(预归纳)与 online(部署中学习)两种模式。

## 关键贡献
证明"工作流级记忆"比原子经验更能提升长程任务表现,且可在线持续进化;记忆进化方向的代表作之一。

## 维度速查 (TAXONOMY)
```
What:   Context(Memory / Workflow)
When:   Inter-test-time × ICL
How:    Imitation(自轨迹归纳) · Offline + Online · On-policy · Hybrid
Where:  General(Web/工具任务)
Eval:   Adaptivity, Retention
```

> 💡 **点评 / 启发**:工作流级记忆比原子经验更有用——人也是记"先查后改"这种 routine,而非每次重新推导。offline/online 双模式让它在部署后还能持续学。
>
> ⚠️ **局限 / 可质疑**:工作流归纳可能过拟合到训练任务分布,迁移到新型任务时旧工作流反而是噪声。缺乏工作流的失效检测。
>
> 📚 **来源**:基于摘要 + ICML 2025 转述(未精读全文)。
