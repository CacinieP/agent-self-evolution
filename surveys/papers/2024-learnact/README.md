# LearnAct: Learning to Generate Action Spaces for Web Agents

- **作者**: Zhiwei Liu et al.
- **发表**: arXiv:2406.13981 (2024)
- **链接**: https://arxiv.org/abs/2406.13981
- **代码**: —

## 一句话总结
Agent 自主学习和生成 Web 操作动作空间,根据任务和页面动态调整可用动作。

## 核心方法
从成功轨迹中提炼有效的网页操作模式,生成结构化动作空间定义,支持 Agent 根据当前页面自适应选择操作。

## 关键贡献
将动作空间从静态定义转为可学习的动态生成,提升 Web Agent 的泛化性和效率。

## 维度速查 (TAXONOMY)
```
What:   Tool(Iterative refinement) + Context(Prompt)
When:   Inter-test-time × ICL
How:    Imitation · Offline · On-policy · Outcome
Where:  GUI/Web
Eval:   Adaptivity, Generalization
```
