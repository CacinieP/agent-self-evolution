# Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents

- **作者**: Jenny Zhang, Sam Greydanus, Sakana AI et al.
- **发表**: arXiv:2505.22954 (2025)
- **链接**: https://arxiv.org/abs/2505.22954
- **代码**: https://github.com/jennyzzt/dgm
- **项目页**: https://sakana.ai/dgm/

## 一句话总结
在冻结基座模型之上,Agent 用开放式进化重写自己的代码(工具/工作流),靠基准成绩实证"改得更好",持续自我改进。

## 核心方法
自指系统:Agent 把自身当前代码版本作为起点,提出变异(改代码)→ 在基准上运行评估 → 保留改进并归档 → 维护一个进化"岛屿"archive 做开放式探索,胜出者成为新基线,形成达尔文式自我进化。

## 关键贡献
把"自我改写代码 + 经验式实证验证 + 开放式进化"结合,是系统级自进化的代表作;展示从零开始涌现出超越人工设计的 Agent。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Single Agent, self-modifying)
When:   Inter-test-time
How:    Population(Evolutionary, open-ended) · Online · On-policy
Where:  Coding(SWE-bench 等)
Eval:   Adaptivity, Generalization(跨基准迁移)
```

> 💡 **点评 / 启发**:自指系统的极致——Agent 重写自己的代码,开放式进化。最接近"自我改进 AI"科幻叙事的工作。关键设计:用基准成绩做实证验证(而非自评),保留进化 archive 做开放式探索。
>
> ⚠️ **局限 / 可质疑**:**最危险也最难验证**的一类。"改得更好"还是"改得自我感觉更好",区分极难。开放式进化无收敛保证,可能跑飞。生产环境绝对不该裸跑,需强审计/沙箱。
>
> 📚 **来源**:基于摘要 + Sakana 项目页(未精读全文)。详见 [`docs/SURVEY.md`](../../../docs/SURVEY.md) 架构章节的判断。
