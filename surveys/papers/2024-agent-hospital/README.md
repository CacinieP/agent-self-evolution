# A Simulacrum of Hospital with Evolvable Medical Agents (Agent Hospital)

- **作者**: Li, Wang, et al.
- **发表**: arXiv:2405.02957 (2024)
- **链接**: https://arxiv.org/abs/2405.02957
- **代码**: —

## 一句话总结
虚拟医院 simulacrum:病人/护士/医生都是 LLM Agent,医生 Agent 可从诊疗经验中自主进化、提升医术,无需人工干预。

## 核心方法
构建完整诊疗流程的模拟环境 → 医生 Agent 在大量病例交互中积累经验 → 自主进化治疗能力;体现"专属域 + 经验驱动进化"。

## 关键贡献
医疗域自进化 Agent 的代表作,展示 Agent 在垂直领域通过模拟经验持续成长的可能。

## 维度速查 (TAXONOMY)
```
What:   Context(Memory / 经验) + Model
When:   Inter-test-time × ICL(+ 可微调)
How:    Imitation(经验沉淀) · Online · On-policy · Outcome
Where:  Specialized(Medical)
Eval:   Adaptivity, Retention(诊疗准确率)
```

> 💡 **点评 / 启发**:虚拟环境 + 可进化 Agent 的组合很巧妙——医生 Agent 在大量模拟病例中"行医"积累经验自主进化,绕过了真实医疗数据隐私与伦理的红线。是垂直域自进化的优秀范式。
>
> ⚠️ **局限 / 可质疑**:模拟病例与真实病例的分布差距直接限制进化上限;"进化"的医学有效性需专业评估,而非仅看模拟指标。医疗域误诊代价极高,模拟进化的迁移风险大。
>
> 📚 **来源**:基于摘要 + HF 讨论(未精读全文)。
