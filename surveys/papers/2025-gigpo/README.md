# GiGPO: Group-in-Group Policy Optimization for LLM Agent Training

- **作者**: Lang Feng, Zhenghai Xue, Tingcong Liu, Bo An
- **发表**: NeurIPS 2025 / arXiv:2505.10978
- **链接**: https://arxiv.org/abs/2505.10978
- **代码**: —

## 一句话总结
Group-in-Group 策略优化框架,通过分层组内竞争和组间协作训练多 Agent 策略。

## 核心方法
将多 Agent 训练分解为组内竞争(同组 Agent 间)和组间协作(不同组 Agent 间)的两级优化。

## 关键贡献
分层策略优化在 LLM Agent 任务上提升协作效率和策略质量。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Multi-Agent) + Model(Policy)
When:   Inter-test-time × RL
How:    Reward-based(Policy Optimization) · Online · On-policy · Hybrid
Where:  General
Eval:   Adaptivity, Generalization
```
