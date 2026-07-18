# TrustAgent: Trustworthy Agent with Self-Verification

- **作者**: (Multiple authors)
- **发表**: arXiv:2410.00000 (2024)
- **链接**: https://arxiv.org/abs/2410.00000
- **代码**: —

## 一句话总结
Agent 在执行中通过自验证机制确保行为可靠性,实时纠正不安全动作。

## 核心方法
Agent 在执行前自检动作安全性,执行后验证结果正确性,在发现问题时主动回退。

## 关键贡献
自验证+自纠正机制在安全关键任务上显著降低有害行为率。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Single-agent) + Model(Policy)
When:   Intra-test-time × ICL
How:    Reward-based(自验证) · Online · On-policy · Process
Where:  General
Eval:   Safety, Adaptivity
```
