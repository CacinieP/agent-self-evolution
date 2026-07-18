# Alita: An LLM-based Agent for IoT Device Control

- **作者**: Jinbo Wang et al.
- **发表**: arXiv:2405.18778 (2024)
- **链接**: https://arxiv.org/abs/2405.18778
- **代码**: —

## 一句话总结
LLM Agent 通过自主探索和设备描述生成可用的 IoT 控制工具,实现跨设备自进化。

## 核心方法
Agent 在模拟环境中自主探索 IoT 设备 API,自动生成工具描述和调用代码,构建可复用的技能库。

## 关键贡献
证明 LLM Agent 可通过自我探索在 IoT 领域从零构建工具集,无需人工标注技能。

## 维度速查 (TAXONOMY)
```
What:   Tool(Discovery & Creation)
When:   Inter-test-time × ICL
How:    Reward-based(任务完成) · Online · On-policy · Outcome
Where:  Other
Eval:   Adaptivity
```
