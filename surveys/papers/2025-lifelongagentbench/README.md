# LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners

- **作者**: Junhao Zheng, Xiudan Cai, Qiang Li, et al.
- **发表**: arXiv:2505.11942 (2025)
- **链接**: https://arxiv.org/abs/2505.11942
- **项目页**: https://caixd-220529.github.io/LifelongAgentBench/

## 一句话总结
首个统一评测 LLM Agent 终身学习能力的基准:衡量跨任务持续学习中的技能累积、保持与迁移。

## 核心方法
跨多领域(Database / OS 等)设计连续任务序列,系统评估 Agent 在长程任务流中累积技能、抗遗忘、迁移的能力,补足现有 episodic 评测的盲区。

## 关键贡献
填补"终身学习"评测空白,对应 TAXONOMY §5 的 Long-horizon Lifelong Learning 评测范式。

## 维度速查 (TAXONOMY)
```
What:   (Benchmark)
When:   — (跨任务长程)
How:    —
Where:  General(多领域)
Eval:   Retention(FGT/BWT), Generalization, Adaptivity
```

> 💡 **点评 / 启发**:直接补 episical 评测的最大盲区——用跨领域(Database/OS)的连续任务流,评 Agent 的技能累积、抗遗忘、迁移。少数真正测"持续进化"而非"单点成绩"的基准。
>
> ⚠️ **局限 / 可质疑**:终身学习的"正确行为"定义本身模糊(何时该迁移、何时该遗忘),评分设计主观性高。领域覆盖仍有限。
>
> 📚 **来源**:基于摘要 + 项目页(未精读全文)。
