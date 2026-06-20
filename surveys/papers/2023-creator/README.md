# CREATOR: Tool Creation for Disentangling Abstract and Concrete Reasoning with Large Language Models

- **作者**: Qian Cheng et al.
- **发表**: Findings of EMNLP 2023 / arXiv:2305.14318
- **链接**: https://arxiv.org/abs/2305.14318
- **代码**: https://github.com/qiancheng0/CREATOR

## 一句话总结
让 LLM 不只是"用工具",而是自己"造工具":先抽象设计工具,再用它执行具体决策。

## 核心方法
解耦两阶段:① 抽象工具创建(生成文档 + 代码实现的工具)→ ② 具体决策执行(调用自创工具求解);相比"创建与执行耦合"的基线更清晰、更强。

## 关键贡献
从"工具使用者"迈向"工具创造者"的代表性工作,是 Tool/Create 子方向的奠基之一。

## 维度速查 (TAXONOMY)
```
What:   Tool(Create)
When:   Intra/Inter-test-time × ICL
How:    Imitation(自生成工具) · Online · On-policy · Outcome
Where:  General(数学 / 知识QA / 具身)
Eval:   Adaptivity, Generalization
```

> 💡 **点评 / 启发**:抽象/具体两阶段解耦是好的工程设计——先想清楚"要个什么工具",再写实现,比边想边调用更可靠。明确点出 Agent 从"工具用户"到"工具创造者"的身份跃迁。
>
> ⚠️ **局限 / 可质疑**:自造工具的正确性无验证机制(造了个有 bug 的工具,后续调用都会错)。任务类型偏数学/知识 QA,工具创造的通用性未充分证明。
>
> 📚 **来源**:基于摘要 + EMNLP 2023 转述(未精读全文)。
