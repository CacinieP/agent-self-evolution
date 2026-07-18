# MemGen: Weaving Generative Latent Memory for Self-Evolving Agents

- **作者**: Guibin Zhang, Muxin Fu, Shuicheng Yan
- **发表**: arXiv:2509.24704 (2025)
- **链接**: https://arxiv.org/abs/2509.24704
- **代码**: —

## 一句话总结
动态生成式记忆框架,Agent 在推理全过程中主动回忆和增强记忆。

## 核心方法
Memory Trigger 监控推理状态 → Memory Weaver 构建隐式 token 序列作为机器原生记忆 → 在推理中自发回忆增强。

## 关键贡献
无需显式监督,Agent 自发发展类人记忆能力(规划/程序/工作记忆),超越 ExpeL 38.22%。

## 维度速查 (TAXONOMY)
```
What:   Context(Memory)
When:   Inter-test-time × ICL
How:    Reward-based · Offline+Online · On-policy · Outcome
Where:  General
Eval:   Adaptivity, Retention
```
