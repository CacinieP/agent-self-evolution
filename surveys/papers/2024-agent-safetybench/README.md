# Agent-SafetyBench: Evaluating the Safety of LLM Agents

- **作者**: Zhang, Cui et al. (THU-CoAI / 清华)
- **发表**: arXiv:2412.14470 (2024)
- **链接**: https://arxiv.org/abs/2412.14470
- **代码**: https://github.com/thu-coai/Agent-SafetyBench

## 一句话总结
全面的 LLM Agent 安全评测基准:覆盖约 349 个交互环境,从两大基本安全维度系统评估 Agent 安全性。

## 核心方法
定义两大安全维度(如指令遵循安全性、有害行为边界),构造约 349 个多样化交互环境对 Agent 施压测试,提供标准化安全评分。

## 关键贡献
填补 Agent 安全评测空白,对应 TAXONOMY §5 安全评测目标(Safety Score / Harm Score / Risk Ratio)。

## 维度速查 (TAXONOMY)
```
What:   (Benchmark — Safety)
When:   —
How:    —
Where:  General
Eval:   Safety(Safety Score, Harm Score, Risk Ratio, Refusal Rate)
```

> 💡 **点评 / 启发**:349 个交互环境覆盖两大安全维度,是 Agent 安全评测的扎实基线。把"安全"从抽象口号变成可量化的多环境施压,本身就有价值。
>
> ⚠️ **局限 / 可质疑**:仍是 episodic 评测,测不出"持续自进化后的安全退化"(那正是 ATP 揭示的真风险)。与自进化的结合评测是空白。
>
> 📚 **来源**:基于摘要 + THU-CoAI repo(未精读全文)。
