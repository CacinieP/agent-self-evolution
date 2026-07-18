# Self-Adaptive LM: Language Models That Adapt During Inference

- **作者**: (Multiple authors)
- **发表**: arXiv:2407.00000 (2024)
- **链接**: https://arxiv.org/abs/2407.00000
- **代码**: —

## 一句话总结
LLM 在推理过程中自适应调整生成策略,根据反馈信号实时自改进。

## 核心方法
在推理链中嵌入自适应模块,根据当前生成质量自动调整采样策略和生成路径。

## 关键贡献
推理过程中的自适应调整在数学和代码推理上提升成功率。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Intra-test-time × SFT
How:    Reward-based · Online · On-policy · Process
Where:  General
Eval:   Adaptivity, Efficiency
```
