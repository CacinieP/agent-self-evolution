# TextGrad: Automatic "Differentiation" via Text

- **作者**: Mert Yuksekgonul et al. (Stanford / CZ Biohub)
- **发表**: NeurIPS 2024 / arXiv:2406.07496
- **链接**: https://arxiv.org/abs/2406.07496
- **代码**: https://github.com/zou-group/textgrad

## 一句话总结
把 LLM 生成的文字反馈当成"梯度",在复合 AI 系统上做类似反向传播的优化,自动改进各组件(含 prompt/参数/代码)。

## 核心方法
PyTorch 风格 API:定义计算图(LLM 调用为节点)→ 损失转为文字"梯度"反馈 → 自顶向下反向传播文本建议 → 各节点据反馈更新;可优化 prompt、代码乃至触发微调。

## 关键贡献
把"自动微分"思想引入文本/LLM 域,是"统一自改进框架"的代表(横跨 Model/Context/Arch),工程可用性强。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Context(Prompt) + Architecture
When:   Inter-test-time
How:    Reward-based(文字梯度) · Offline-Online · Mixed · Outcome
Where:  General
Eval:   Adaptivity, Efficiency, Generalization
```

> 💡 **点评 / 启发**:把反向传播的思想移植到文本——损失变文字反馈,沿计算图回传。统一了 prompt/代码/参数的优化为一个框架,PyTorch 风格 API 让上手成本低。是"自改进基础设施"的有力候选。
>
> ⚠️ **局限 / 可质疑**:文字"梯度"不如数值梯度精确,收敛性无保证;反馈质量依赖 critic 模型。复杂计算图上回传成本高。
>
> 📚 **来源**:基于摘要 + 官方文档(未精读全文)。
