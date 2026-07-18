# ACE: Automatic Chain-of-thought Enhancement via Backward Reasoning

- **作者**: Ruichen Wang et al.
- **发表**: arXiv:2406.15372 (2024)
- **链接**: https://arxiv.org/abs/2406.15372
- **代码**: —

## 一句话总结
通过后向推理自动生成高质量思维链,自我改进思维链质量。

## 核心方法
从答案出发反向构造推理过程,自动修正正向 CoT 中的错误步骤,生成更可靠的推理链条。

## 关键贡献
证明后向推理可系统性提升思维链质量,在多步推理任务上显著优于正向自生成方法。

## 维度速查 (TAXONOMY)
```
What:   Context(Prompt) + Model(Policy)
When:   Intra-test-time × ICL
How:    Reward-based(答案正确性) · Online · On-policy · Process
Where:  General(推理)
Eval:   Generalization, Efficiency
```
