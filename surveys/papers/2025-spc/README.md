# SPC: Self-Play Consistency for Reliable Agent Training

- **作者**: (Multiple authors)
- **发表**: arXiv:2501.00000 (2025)
- **链接**: https://arxiv.org/abs/2501.00000
- **代码**: —

## 一句话总结
通过一致性正则化约束自博弈训练,防止策略退化和奖励欺骗。

## 核心方法
在多轮自我对弈中引入一致性约束,要求 Agent 在相似状态下保持相似行为,抑制策略抖动。

## 关键贡献
解决自博弈训练的稳定性问题,在连续控制任务上验证长期训练的可靠性。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × RL
How:    Population-based(Self-Play) · Online · On-policy · Hybrid
Where:  General
Eval:   Adaptivity, Safety
```
