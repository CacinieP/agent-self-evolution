# Web Agents can Self-Improve by Discovering and Honing Skills (SkillWeaver)

- **作者**: Boyuan Zheng et al. (OSU NLP Group)
- **发表**: arXiv:2504.07079 (2025)
- **链接**: https://arxiv.org/abs/2504.07079
- **代码**: https://osu-nlp-group.github.io/SkillWeaver/

## 一句话总结
以技能为中心的框架:Web Agent 自主把重复操作合成为可复用的 API 技能,通过练习不断打磨,构建自我成长的技能库。

## 核心方法
探索中发现重复模式 → 合成为 API 形态技能存入技能库 → 通过练习(honing)迭代改进技能实现;技能可跨任务复用,形成技能驱动的自我提升。

## 关键贡献
把"工具创造"与"技能打磨"统一到 API 化技能库,是 Tool/Create + Master 方向的代表性新工作。

## 维度速查 (TAXONOMY)
```
What:   Tool(Create + Master) + Context(技能库)
When:   Inter-test-time × ICL
How:    Imitation(自合成) + Reward-based(练习反馈) · Online · On-policy · Outcome
Where:  Specialized(Web)
Eval:   Adaptivity, Retention, Generalization
```

> 💡 **点评 / 启发**:把技能 API 化 + 练习打磨,工业化了 Voyager 的技能库思想。"发现重复模式→合成 API→练习改进"的闭环,让技能库不只会增长还会变精。
>
> ⚠️ **局限 / 可质疑**:API 技能的泛化性(换网站是否还适用)是 Web 域特有问题;练习改进若无正确性验证,可能把错误技能练得更"自信"。
>
> 📚 **来源**:基于摘要 + OSU 项目页(未精读全文)。
