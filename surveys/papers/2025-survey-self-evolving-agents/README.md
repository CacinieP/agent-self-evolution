# A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve

- **作者**: Huan-ang Gao, Jiayi Geng, Wenyue Hua, Mengkang Hu, et al.
- **发表**: arXiv:2507.21046 (2025)
- **链接**: https://arxiv.org/abs/2507.21046
- **代码**: https://github.com/CharlesQ9/Self-Evolving-Agents

## 一句话总结
本仓库 TAXONOMY 的主骨架:首个系统化、覆盖 What/When/How/Where 四维的 Agent 自进化综述。

## 核心方法
用四维框架组织:What(Model/Context/Tool/Arch)× When(intra/inter)× How(方法族 + 横切维度)× Where(应用域),并给形式化定义与开放问题。

## 关键贡献
建立领域共识级分类法,整合记忆 / Prompt / 工具 / 架构进化,并系统讨论评测缺口与安全风险(ATP、奖励黑客、漂移)。

## 维度速查 (TAXONOMY)
```
What:   (综述:Model/Context/Tool/Arch 全覆盖)
When:   (综述:Intra/Inter × ICL/SFT/RL)
How:    (综述:Reward/Imitation/Population + 横切维度)
Where:  (综述:General + 各专属域)
Eval:   (综述:5 目标 × 3 范式)
```

> 💡 **点评 / 启发**:本仓库 TAXONOMY 的主骨架。最大贡献是把散乱的 self-X 统一进 What/When/How/Where 四维,并给出形式化定义与三条判据。安全章节(ATP/奖励黑客/漂移)是同类综述里最系统的。
>
> ⚠️ **局限 / 可质疑**:四维框架组织力强但也"框住"了视角——某些工作(如开放式进化)难以干净归入某格。评测章节点出 episical 盲区,但未给出解法。
>
> 📚 **来源**:精读 HTML 版 + 本仓库 TAXONOMY 即基于其重建。强烈建议作为该领域的入门第一篇。
