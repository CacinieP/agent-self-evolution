# ReasoningBank: Scaling LLM Reasoning through Collaborative Learning and Verification

- **作者**: Jiaqi Liu et al.
- **发表**: arXiv:2410.01311 (2024)
- **链接**: https://arxiv.org/abs/2410.01311
- **代码**: —

## 一句话总结
构建"推理银行"机制,通过协作学习与验证系统化提升 LLM 推理能力。

## 核心方法
Agent 将推理经验存入结构化"银行",通过验证模块筛选高质量推理路径,多 Agent 协作共同优化推理策略。

## 关键贡献
提出协作式推理增强框架,在数学和逻辑推理上验证多轮自改进的累积效果。

## 维度速查 (TAXONOMY)
```
What:   Context(Memory) + Architecture(Multi-Agent)
When:   Inter-test-time × SFT
How:    Reward-based(验证器) + Imitation · Offline+Online · Mixed · Hybrid
Where:  General
Eval:   Generalization, Efficiency
```
