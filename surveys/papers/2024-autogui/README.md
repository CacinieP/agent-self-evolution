# AutoGUI: Grounding GUI Agents in Natural Language

- **作者**: Li et al. (2025)
- **发表**: arXiv:2502.01977 (2025)
- **链接**: https://arxiv.org/abs/2502.01977
- **代码**: —

## 一句话总结
GUI Agent 通过自然语言理解自动分解任务为 GUI 操作序列,并在执行中自我修正。

## 核心方法
将 GUI 操作建模为语言可解释动作,Agent 根据视觉观察和语言指令生成/修正操作计划。

## 关键贡献
实现 GUI 任务的自解释执行,通过自我纠正显著提升复杂 GUI 操作成功率。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Single-agent) + Tool
When:   Intra-test-time × ICL
How:    Reward-based(任务完成) · Online · On-policy · Process
Where:  GUI/Web
Eval:   Adaptivity, Generalization
```
