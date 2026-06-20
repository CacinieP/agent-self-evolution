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

> 个人点评 / 启发 待补充。
