# Training Language Models to Self-Correct via Reinforcement Learning (SCoRe)

- **作者**: Avanika Narayan Senthil Kumar et al. (Google DeepMind)
- **发表**: ICLR 2025 / arXiv:2409.12917
- **链接**: https://arxiv.org/abs/2409.12917
- **代码**: —

## 一句话总结
用多轮在线 RL(纯自生成数据)教单个模型"先产出答案、再自我纠正",无需外部反馈模型或纠正数据。

## 核心方法
两阶段训练:① 初始化 + 奖励塑形,锁定第一轮分布 → ② 多轮在线 RL,在自生成轨迹上同时优化"产出"与"纠正";克服直接 RL 导致的分布坍缩。

## 关键贡献
实证自纠正可被 RL 显式训练获得(Gemini 1.0/1.5 在 MATH/GSM8K 上 SOTA),回应"LLM 能否真正自我纠正"的长期争论。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Intra/Inter-test-time × RL
How:    Reward-based · Online · On-policy · Outcome
Where:  General(推理)
Eval:   Adaptivity(MATH, GSM8K)
```

> 💡 **点评 / 启发**:直接回应"LLM 能否真正自我纠正"的长期争论——结论是"能,但必须显式 RL 训练"。两阶段(初始化锁定 + 多轮 RL)是工程上绕过分布坍缩的精巧设计。
>
> ⚠️ **局限 / 可质疑**:自纠正的收益依赖任务有可验证答案(数学/代码),开放任务上"纠正"无客观标准。训练成本高(在线 RL)。
>
> 📚 **来源**:精读原文 + ICLR 2025。
