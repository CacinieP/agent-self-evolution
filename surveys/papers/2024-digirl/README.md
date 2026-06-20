# DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning

- **作者**: Hao Bai et al. (Berkeley / Google 等)
- **发表**: NeurIPS 2024 / arXiv:2406.11896
- **链接**: https://arxiv.org/abs/2406.11896
- **代码**: https://github.com/DigiRL-agent/digirl
- **项目页**: https://digirl-agent.github.io/

## 一句话总结
在真实安卓环境里用自主 RL 训练设备控制 Agent:先离线 RL 初始化,再 offline-to-online RL 持续进化。

## 核心方法
两阶段:① 离线 RL 在专家轨迹上初始化 VLM 策略 → ② offline-to-online RL,在真实环境自主采集 + 过滤 + 训练;用自主过滤的奖励信号闭环提升。

## 关键贡献
首批在"真实在野"设备环境做自主 RL 训练的工作,展示真实任务大幅提升,是 GUI 域 RL 训练的代表。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × RL
How:    Reward-based(自主/过滤奖励) · Offline→Online · Mixed · Outcome
Where:  Specialized(GUI / Device Control)
Eval:   Adaptivity, Generalization(真实安卓)
```

> 个人点评 / 启发 待补充。
