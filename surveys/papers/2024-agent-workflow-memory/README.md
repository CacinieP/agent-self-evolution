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

> 个人点评 / 启发 待补充。
