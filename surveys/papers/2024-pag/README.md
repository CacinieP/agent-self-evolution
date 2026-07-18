# PAG: Multi-turn Reinforced LLM Self-Correction with Policy as Generative Verifier

- **作者**: Jiang et al. (2025)
- **发表**: arXiv:2410.00139 (待验证)
- **链接**: https://arxiv.org/abs/2410.00139
- **代码**: —

## 一句话总结
用策略作为生成式验证器,多轮强化 LLM 自我纠正。

## 核心方法
执行轨迹/自然语言评估作为奖励信号,在线 SFT+RL 框架下持续改进策略。

## 关键贡献
验证器驱动的自我纠正机制在多轮交互中显著提升复杂任务表现。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Intra-test-time × RL
How:    Reward-based · Online · On-policy · Process
Where:  General
Eval:   Adaptivity, Efficiency
```

> ⚠️ **需验证**: arxiv ID 为占位符。标题来自 TAXONOMY 主骨架论文(arXiv:2507.21046)引用 bib.bib176。
