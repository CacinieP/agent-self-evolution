# WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning

- **作者**: Zeyi Qi et al. (THUDM / 清华 KEG)
- **发表**: ICLR 2025 / arXiv:2411.02337
- **链接**: https://arxiv.org/abs/2411.02337
- **代码**: https://github.com/THUDM/WebRL

## 一句话总结
自进化在线课程 RL:自动生成难度递增任务 + 自训练自适应奖励模型,把开源 LLM 训成强 Web Agent。

## 核心方法
① 自动课程:据 Agent 当前能力生成难度匹配的新任务 → ② 自训练奖励模型:在自生成 rollout 上训练,提供反馈 → ③ RL 微调;循环使任务与能力协同进化。

## 关键贡献
显著提升 Llama-3.1-8B / GLM-4 在 WebArena 上的成功率,缩小与闭源模型的差距,Web 域自进化课程 RL 的代表。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Context(自进化课程)
When:   Inter-test-time × RL
How:    Reward-based(自适应奖励) · Online · On-policy · Outcome
Where:  Specialized(Web)
Eval:   Adaptivity, Generalization(WebArena)
```

> 个人点评 / 启发 待补充。
