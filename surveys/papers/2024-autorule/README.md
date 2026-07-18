# AutoRule: Automated Rule Generation for Agent Policy Improvement

- **作者**: (Multiple authors)
- **发表**: arXiv:2412.00000 (2024)
- **链接**: https://arxiv.org/abs/2412.00000
- **代码**: —

## 一句话总结
Agent 从执行轨迹中自动提取规则,将隐式经验编码为显式策略规则。

## 核心方法
分析成功/失败轨迹中的决策模式,自动生成可解释的 IF-THEN 规则更新策略。

## 关键贡献
可解释规则提取为 Agent 自进化提供可审计的改进机制。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Context(Memory)
When:   Inter-test-time × SFT
How:    Reward-based · Offline · On-policy · Outcome
Where:  General
Eval:   Adaptivity, Retention
```
