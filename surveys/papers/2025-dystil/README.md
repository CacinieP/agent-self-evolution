# DYSTIL: Dynamic Self-Improvement via Trajectory-Driven Insight Learning

- **作者**: Zhenshuo Zhang et al.
- **发表**: arXiv:2506.15219 (2025)
- **链接**: https://arxiv.org/abs/2506.15219
- **代码**: —

## 一句话总结
从失败轨迹中动态提取可迁移的深层洞察,驱动 Agent 跨任务自我改进。

## 核心方法
构建洞察挖掘模块,分析失败轨迹的共性模式,将结构化洞察写入记忆供后续任务检索复用。

## 关键贡献
实现从原始失败经验到可泛化洞察的自动提炼,在多步推理和规划任务上验证自改进效果。

## 维度速查 (TAXONOMY)
```
What:   Model(Experience) + Context(Memory)
When:   Inter-test-time × SFT
How:    Reward-based(轨迹分析) · Offline · On-policy · Process
Where:  General
Eval:   Retention, Generalization
```
