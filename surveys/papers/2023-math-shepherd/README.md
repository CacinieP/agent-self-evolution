# Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations

- **作者**: Wang et al. (DeepSeek / 北大 等)
- **发表**: ACL 2024 / arXiv:2312.08935
- **链接**: https://arxiv.org/abs/2312.08935
- **代码**: —

## 一句话总结
无需人工标注,自动构造逐步监督信号训练过程奖励模型(PRM),对推理的每一步打分并据此强化。

## 核心方法
对每个中间步用"该步之后能否继续解到正确结果"作为隐式标签,自动训练 PRM;PRM 既可做验证(选最优解),也可做强化(逐步奖励)。

## 关键贡献
把过程奖励(PRM)去人工化、规模化,是 process-level RL 自进化的代表作之一。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy / Reward)
When:   Inter-test-time × RL
How:    Reward-based(自动 PRM) · Offline · On-policy · Process
Where:  General(数学推理)
Eval:   Adaptivity(MATH, GSM8K)
```

> 个人点评 / 启发 待补充。
