# AutoRule: Reasoning Chain-of-thought Extracted Rule-based Rewards Improve Preference Learning

- **作者**: Tevin Wang, Chenghao Xiong
- **发表**: arXiv:2506.15651 (2025)
- **链接**: https://arxiv.org/abs/2506.15651
- **代码**: —

## 一句话总结
从推理链中自动提取显式规则,构造规则化奖励改进偏好学习。

## 核心方法
用 LLM 从思维链与偏好反馈中归纳可执行规则,将规则满足度转化为密集奖励信号用于偏好优化。

## 关键贡献
规则化奖励提升偏好学习质量,同时保持可解释性与可审计性。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Context(Prompt)
When:   Inter-test-time × RL
How:    Reward-based(规则奖励) · Offline · On-policy · Outcome
Where:  General
Eval:   Adaptivity, Retention
```
