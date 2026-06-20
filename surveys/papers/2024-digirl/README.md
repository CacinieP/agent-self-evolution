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

> 💡 **点评 / 启发**:首批在"真实在野"安卓环境做自主 RL 的工作。offline→online 两阶段是务实设计:先离线学到能起步,再在线持续进化。证明了 GUI 域 RL 训练的可行性。
>
> ⚠️ **局限 / 可质疑**:真实设备执行慢且不可逆,数据采集成本高;奖励来自任务完成,稀疏。泛化到未见 App 存疑。
>
> 📚 **来源**:基于摘要 + NeurIPS 2024 转述(未精读全文)。
