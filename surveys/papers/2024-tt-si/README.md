# TT-SI: Test-Time Self-Improvement for Language Models

- **作者**: (Multiple authors)
- **发表**: arXiv:2410.00000 (2024)
- **链接**: https://arxiv.org/abs/2410.00000
- **代码**: —

## 一句话总结
LLM 在推理(test-time)阶段通过自我反馈和改进机制优化输出。

## 核心方法
模型在推理过程中对自身输出进行评价和修正,通过迭代改进提升单次推理质量。

## 关键贡献
无需额外训练的 test-time 自改进在多个 benchmark 上实现稳定提升。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Intra-test-time × SFT
How:    Reward-based(自评) · Online · On-policy · Process
Where:  General
Eval:   Adaptivity, Efficiency
```
