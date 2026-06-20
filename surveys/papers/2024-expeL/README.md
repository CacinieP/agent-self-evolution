# ExpeL: LLM Agents Are Experiential Learners

- **作者**: Andrew Zhao, Daniel Huang, et al. (CUHK)
- **发表**: AAAI 2024 / arXiv:2308.10144
- **链接**: https://arxiv.org/abs/2308.10144
- **代码**: https://github.com/LeapLabTHU/ExpeL

## 一句话总结
Agent 从大量任务轨迹中抽取可复用的"经验 / 洞察"存进知识库,新任务时检索复用。

## 核心方法
先用 Agent 跑任务收集轨迹 → LLM 自行归纳抽取成功 / 失败的 insights(经验)→ 新任务时检索相关经验注入上下文。

## 关键贡献
把 Agent 从"无记忆重复试错"提升为"经验积累者",是技能 / 记忆进化方向的代表(非权重更新)。

## 维度速查 (TAXONOMY)
```
What:   Context(Memory / 经验库)
When:   Inter-test-time × ICL
How:    Imitation(自轨迹归纳) · Offline-Online · On-policy · Hybrid
Where:  General
Eval:   Adaptivity, Retention
```

> 💡 **点评 / 启发**:把 Agent 从"无状态重复试错"提升为"经验积累者"。insight 抽取这一步很关键——存原始轨迹 vs 存归纳后的经验,后者检索效率与可用性高得多。
>
> ⚠️ **局限 / 可质疑**:insight 抽取靠 LLM 自归纳,可能抽取出错误/过拟合的"经验"。缺乏对经验有效性的验证与淘汰机制。
>
> 📚 **来源**:基于摘要 + 综述转述(未精读全文)。
