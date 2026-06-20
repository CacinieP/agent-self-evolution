# DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines

- **作者**: Omar Khattab et al. (Stanford)
- **发表**: NeurIPS 2024 / arXiv:2310.03714
- **链接**: https://arxiv.org/abs/2310.03714
- **代码**: https://github.com/stanfordnlp/dspy

## 一句话总结
把 LM 程序声明式化,用编译器式优化(含自动 prompt 优化)在指标驱动下"自我改进"流水线。

## 核心方法
模块化 + 编译:签名(signature)/ 模块 / 优化器,优化器(如 MIPRO / BootstrapFewShot)据自动评估指标自动调提示与示例。

## 关键贡献
把 prompt 工程从手写变成"可优化的程序",是 Prompt 进化 / 程序化优化的代表性基础设施。

## 维度速查 (TAXONOMY)
```
What:   Context(Prompt Optimization)
When:   Inter-test-time
How:    Reward-based(自动指标) · Offline · Mixed · Outcome
Where:  General
Eval:   Adaptivity, Efficiency
```

> 💡 **点评 / 启发**:把 prompt 工程从"手艺"变成"工程"——声明式签名 + 编译器式优化器,让 prompt 可版本化、可回归测试。是 Prompt 进化方向唯一达到"基础设施"级别的工作。
>
> ⚠️ **局限 / 可质疑**:优化器效果依赖评估指标质量;指标若有偏,优化器会忠实地优化到错误方向。学习曲线对新手偏陡。
>
> 📚 **来源**:精读文档 + 实际使用经验。
