# Absolute Zero: Reinforced Self-play Reasoning with Zero Data

- **作者**: Andrew Zhao et al. (Tsinghua / 智谱 等多机构)
- **发表**: arXiv:2505.03335 (2025)
- **链接**: https://arxiv.org/abs/2505.03335
- **代码**: https://github.com/LeapLabTHU/Absolute-Zero-Reasoner
- **项目页**: https://andrewzh112.github.io/absolute-zero-reasoner/

## 一句话总结
单一模型同时"出题"和"做题",用 Python 执行器验证答案作为奖励,零外部数据自对弈训练推理能力。

## 核心方法
Absolute Zero 范式:模型既 propose 任务(自我演化课程),又 solve 任务;用代码执行结果作为可验证奖励(RLVR);TRR++ 在出题/解题两端持续提升。课程按"自身可学习性"自适应演化。

## 关键贡献
提出无需人工数据的 RLVR 自对弈范式,Absolute Zero Reasoner (AZR) 在编码与数学推理上达到 SOTA,验证"零数据自我提升"的可行性。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Context(自演化课程)
When:   Inter-test-time × RL
How:    Population(Self-Play) + Reward-based(代码验证) · Online · Mixed · Outcome
Where:  General(推理)
Eval:   Adaptivity, Generalization(编码 + 数学)
```

> 💡 **点评 / 启发**:最激进的"零数据"主张——单模型自出题自做题,用代码执行器当唯一外部真实。这巧妙绕开了"自生成数据天花板"悖论:代码执行结果是 Agent 无法左右的真实反馈。
>
> ⚠️ **局限 / 可质疑**:能验证的只有"代码能跑通"的推理,泛化到无验证器的领域(写作/对话)则失去锚点。"零数据"是相对的——预训练数据已含大量知识。
>
> 📚 **来源**:基于摘要 + 项目页(未精读全文,较新待更多复现)。
