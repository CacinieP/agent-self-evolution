# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

- **作者**: Carlos E. Jimenez, John Yang, et al. (Princeton)
- **发表**: ICLR 2024 / arXiv:2310.06770
- **链接**: https://arxiv.org/abs/2310.06770
- **代码**: https://github.com/princeton-nlp/SWE-bench

## 一句话总结
从真实 GitHub 仓库构建的代码 Agent 评测基准:给一个 issue,看 Agent 能否提交通过测试的 patch。

## 核心方法
采集真实 PR,把"应用 patch 后能通过测试"作为正确判据,构造任务实例。

## 关键贡献
成为编码 Agent / 自进化 Agent 的事实标准评测之一,推动 SWE-Gym、SWE-agent 等一系列工作。

## 维度速查 (TAXONOMY)
```
What:   (Benchmark)
When:   —
How:    —
Where:  Coding
Eval:   Adaptivity(真实 issue 解决率)
```

> 💡 **点评 / 启发**:用"真实 PR + 测试通过"作为判据,把代码 Agent 评测从"玩具任务"拉到真实工程场景。催生了 SWE-agent/SWE-Gym 一整个生态,是自进化 Agent 最常引用的基准之一。
>
> ⚠️ **局限 / 可质疑**:测试通过 ≠ 正确实现(测试覆盖不全时可能过拟合测试)。任务来源偏 Python 流行库,语言/领域多样性不足。任务间状态重置,测不出 Agent 的跨任务成长。
>
> 📚 **来源**:精读原文(基准构造部分)。
