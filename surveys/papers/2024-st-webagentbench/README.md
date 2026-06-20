# ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents

- **作者**: Ido Levy, Segev Shlomov et al. (IBM Research)
- **发表**: ICML 2025 / arXiv:2410.06703
- **链接**: https://arxiv.org/abs/2410.06703
- **代码**: https://github.com/segev-shlomov/ST-WebAgentBench
- **项目页**: https://sites.google.com/view/st-webagentbench/home

## 一句话总结
面向 Web Agent 的安全与可信评测:375 个真实企业任务 + 3057 条策略,覆盖六大安全维度。

## 核心方法
构造可配置、可扩展的企业级任务套件,为每个任务配多条安全/合规策略,衡量 Agent 在完成任务时是否违反策略(而非只看完成率)。

## 关键贡献
把 Web Agent 评测从"能完成"推进到"安全可信地完成",对应 TAXONOMY §5 安全评测目标,自进化 Agent 必备的护栏式基准。

## 维度速查 (TAXONOMY)
```
What:   (Benchmark — Safety)
When:   —
How:    —
Where:  Specialized(Web) + Safety
Eval:   Safety(策略违反率), Reliability
```

> 💡 **点评 / 启发**:把 Web Agent 评测从"能完成"推进到"安全可信地完成"——375 真实企业任务 + 3057 策略,衡量完成任务时是否违规。这种"完成 vs 合规"的双轴评测,比单一成功率更接近生产要求。
>
> ⚠️ **局限 / 可质疑**:策略实例的人工编写可能带入编写者偏差;Web 场景的安全结论能否迁移到其他域(代码/工具)未明。
>
> 📚 **来源**:基于摘要 + ICML 2025 转述(未精读全文)。
