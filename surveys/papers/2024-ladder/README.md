# LADDER: Self-Improving LLMs through Recursive Problem Decomposition

- **作者**: Simonds et al. (2025)
- **发表**: arXiv:2503.00735 (2025)
- **链接**: https://arxiv.org/abs/2503.00735
- **代码**: —

## 一句话总结
LLM 通过递归问题分解自我改进,在遇到超出能力的问题时自主发展新能力。

## 核心方法
Agent 将复杂问题递归分解为子问题,通过解决子问题积累能力,在能力边界外自发展新技能。

## 关键贡献
递归分解驱动的自进化使 LLM 能在遇到新问题时自主发展解决能力。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Intra-test-time × RL
How:    Reward-based · Online · On-policy · Process
Where:  General(推理)
Eval:   Adaptivity, Generalization
```
