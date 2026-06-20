# Self-Supervised Prompt Optimization (SPO)

- **作者**: Xiang et al.
- **发表**: arXiv:2502.06855 (2025)
- **链接**: https://arxiv.org/abs/2502.06855
- **代码**: —

## 一句话总结
仅靠模型自身反馈(无需真值标签)即可在开放与封闭任务上发现有效 prompt,兼顾成本效率。

## 核心方法
用进化搜索 + 元学习发现 prompt;以模型自身反馈作为(自监督)信号评估 prompt 质量,避开对人工标注或昂贵评估的依赖,适配开放式生成任务。

## 关键贡献
解决传统 prompt 优化依赖真值/昂贵评估的痛点,把"自监督"引入 prompt 优化,降低自进化的门槛。

## 维度速查 (TAXONOMY)
```
What:   Context(Prompt Optimization)
When:   Inter-test-time
How:    Reward-based(自监督/模型反馈) + Population · Offline-Online · Mixed · Outcome
Where:  General(开放 + 封闭任务)
Eval:   Adaptivity, Efficiency
```

> 个人点评 / 启发 待补充。
