# A-MEM: Agentic Memory for LLM Agents

- **作者**: Wujiang Xu et al. (agiresearch)
- **发表**: NeurIPS 2025 / arXiv:2502.12110
- **链接**: https://arxiv.org/abs/2502.12110
- **代码**: https://github.com/agiresearch/A-mem

## 一句话总结
受 Zettelkasten 启发的代理式记忆:Agent 主动构造笔记、生成链接、让记忆库自我进化与重组织。

## 核心方法
三步:① note construction(把交互沉淀为结构化笔记)→ ② link generation(笔记间建立语义链接)→ ③ memory evolution(随新记忆持续重组、精炼、进化整体记忆网络)。

## 关键贡献
把记忆从"被动存储"升级为"主动自组织的知识网络",是记忆进化方向的新范式。

## 维度速查 (TAXONOMY)
```
What:   Context(Memory / 自组织网络)
When:   Inter-test-time × ICL
How:    Imitation(归纳) + Reward-based(相关性) · Online · On-policy · Hybrid
Where:  General
Eval:   Retention, Adaptivity, Efficiency
```

> 个人点评 / 启发 待补充。
