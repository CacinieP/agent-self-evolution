# MemGen: Memory-Augmented Generation for LLM Agents

- **作者**: Peifeng Wang et al.
- **发表**: arXiv:2409.18409 (2024)
- **链接**: https://arxiv.org/abs/2409.18409
- **代码**: —

## 一句话总结
构建记忆增强生成框架,让 Agent 在生成时主动检索和利用历史经验。

## 核心方法
设计记忆写入(关键经验提取)→记忆检索(语义匹配)→记忆融合(注入生成)的三阶段流水线。

## 关键贡献
将记忆管理从简单检索升级为"写入-检索-融合"完整管线,在开放域任务上验证效果。

## 维度速查 (TAXONOMY)
```
What:   Context(Memory)
When:   Inter-test-time × ICL
How:    Reward-based · Offline+Online · On-policy · Outcome
Where:  General
Eval:   Adaptivity, Retention
```
