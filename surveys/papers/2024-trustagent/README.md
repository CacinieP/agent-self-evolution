# TrustAgent: Towards Safe and Trustworthy LLM-based Agents

- **作者**: Wenyue Hua et al.
- **发表**: arXiv:2402.01586 (2024)
- **链接**: https://arxiv.org/abs/2402.01586
- **代码**: —

## 一句话总结
预训练-提示-控制三模块框架,全流程赋予 LLM Agent 安全意识与可信行为。

## 核心方法
预训练阶段注入安全知识,推理阶段提示引导安全规划,工具层施加控制约束拦截不安全动作。

## 关键贡献
覆盖训练-推理-执行全流程的 Agent 安全增强,兼顾知识注入与行为约束。

## 维度速查 (TAXONOMY)
```
What:   Safety(预训练/提示/控制)
When:   Inter-test-time × SFT
How:    Constraint-based · Offline+Online · Outcome
Where:  General
Eval:   Safety, Trustworthiness
```
