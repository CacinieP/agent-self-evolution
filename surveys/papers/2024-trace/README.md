# Trace Is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs (OptoPrime)

- **作者**: Ching-An Cheng et al.
- **发表**: arXiv:2406.16218 (2024)
- **链接**: https://arxiv.org/abs/2406.16218
- **代码**: https://github.com/microsoft/Trace

## 一句话总结
把 Agent 工作流视为可优化计算图,用执行轨迹与丰富反馈做"文字版自动微分"。

## 核心方法
将工作流参数(提示/代码)与执行轨迹统一建模为优化问题,LLM 优化器 OptoPrime 依据执行反馈联合更新。

## 关键贡献
统一 prompt 优化与工作流优化,为复合 Agent 系统提供通用优化框架。

## 维度速查 (TAXONOMY)
```
What:   Context(Prompt) + Architecture(Workflow)
When:   Inter-test-time × 反馈优化
How:    Feedback-based(文字梯度) · Offline · Outcome
Where:  General
Eval:   Adaptivity, Generalization
```
