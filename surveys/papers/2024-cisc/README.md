# CISC: Confidence Improves Self-Consistency in LLMs

- **作者**: Taubenfeld et al. (2025)
- **发表**: arXiv:2502.06233 (2025)
- **链接**: https://arxiv.org/abs/2502.06233
- **代码**: —

## 一句话总结
置信度驱动的自一致推理,提升 LLM 推理的可靠性和一致性。

## 核心方法
在自一致采样中加入置信度评估,筛选高置信推理路径提高最终答案准确率。

## 关键贡献
置信度引导的自一致方法在数学推理上显著优于朴素自一致。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Intra-test-time × ICL
How:    Reward-based(置信度) · Online · On-policy · Process
Where:  General(推理)
Eval:   Adaptivity, Efficiency
```
