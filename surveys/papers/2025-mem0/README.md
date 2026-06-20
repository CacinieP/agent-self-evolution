# Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

- **作者**: Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav 等 (Mem0)
- **发表**: arXiv:2504.19413 (2025)
- **链接**: https://arxiv.org/abs/2504.19413
- **代码**: https://github.com/mem0ai/mem0

## 一句话总结
面向生产的可扩展长期记忆架构:动态抽取、合并、检索关键信息,给 Agent 持久化记忆层。

## 核心方法
记忆中心架构:从交互中抽取 salient facts → 去重/合并/更新进入记忆库 → 按相关性检索注入上下文;可选图记忆(Mem0g)捕捉实体关系。相比把全量历史塞进上下文,显著降低 token 成本并提升一致性。

## 关键贡献
提供 production-ready 的记忆层(相对 OpenAI 基线在 LLM-as-Judge 上约 +26%,Mem0g 再 +2%),是记忆进化方向工程化的代表。

## 维度速查 (TAXONOMY)
```
What:   Context(Memory)
When:   Inter-test-time × ICL
How:    Reward-based(相关性/一致性) · Online · On-policy · Outcome
Where:  General(长期对话 / 个性化)
Eval:   Adaptivity, Retention, Efficiency
```

> 个人点评 / 启发 待补充。
