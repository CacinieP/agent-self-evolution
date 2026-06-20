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

> 💡 **点评 / 启发**:去真值依赖是实用突破口——多数真实场景没有 ground truth,SPO 用模型自反馈填补,降低了 prompt 优化的落地门槛。
>
> ⚠️ **局限 / 可质疑**:自反馈在开放式任务上不可靠(与 Self-Refine 同病);"无真值"宣称需谨慎,进化方向仍可能漂移。需更多独立复现验证。
>
> 📚 **来源**:基于摘要(未精读,论文较新,独立复现少)。
