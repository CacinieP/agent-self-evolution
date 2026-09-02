# Prototype: Voyager 技能库简化原型(Skill Library Flywheel)

> 对应论文:[Voyager: An Open-Ended Embodied Agent with LLMs](../../../surveys/papers/2023-voyager)(2023)
> TAXONOMY 定位:`What: Tool(Create/Master) + Context(技能库) · When: Inter-test-time × ICL`

## 🎯 这个原型做什么

聚焦 Voyager 三大组件中最具自进化意味的**技能库飞轮**,把 Minecraft 的"代码技能"抽象为"文本任务技能",便于本地零依赖观察:

```
遇到任务
  → 检索技能库:有相关可复用技能?
      → 有:把技能作为提示注入,据此解决(复用)
      → 无:从零生成
  → 验证通过?
      → 成功:把本次解法抽象成技能,存进库
      → 失败:带反馈重新生成
```

**正反馈飞轮**:技能库越大,越多任务能被"复用旧技能"秒解。

## 与其余三个原型的关系

本仓库的四个最小原型分别覆盖反馈迭代、反思记忆、技能积累与网络记忆:

| 原型 | 反馈来源 | 记忆 | 本原型新意 |
|---|---|---|---|
| [Self-Refine](../self_refine) | 模型自评 | 单轮内 | — |
| [Reflexion](../reflexion) | 环境执行 | 跨试验 | — |
| **Voyager(本原型)** | 自评验证 | **跨任务持久 + 检索复用 + 技能抽象** | 技能从"一次性"变"可复用资产" |
| [A-MEM](../amem) | 相关性建链 | 自组织记忆网络 | 记忆从平铺条目变成可演化图结构 |

## 📁 文件

| 文件 | 说明 |
|---|---|
| [`voyager_skill.py`](./voyager_skill.py) | 主程序,单文件 |
| `requirements.txt` | 真实模型模式需要 `openai` |

## 🚀 快速开始

```bash
# 离线 mock:观察"建库 → 复用 → 库增长"的飞轮
python voyager_skill.py --mock --tasks "写一首关于春天的短诗" "创作一首春天的诗" "写一首秋天的诗"

# 真实模型(多任务共享一个技能库,体会积累)
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
python voyager_skill.py --tasks "写会议邀请邮件" "写一封会议邀请" "写周报" --model gpt-4o-mini
```

## 🧠 实现要点

- **零依赖语义检索**:`SkillLibrary.retrieve()` 用字符集合重叠近似语义相似度,避免引入向量库,保持单文件可读。
- **技能抽象**:成功解法经 LLM 抽象为 `(name, description, solution)` 存库,而非存原始对话——这是"技能可复用"的关键。
- **失败重试**:验证器第一行必须明确返回 `PASS` 或 `FAIL`;失败时把反馈带入下一次尝试,默认重试 1 次。
- **复用计数**:每个技能记录被复用次数 `uses`,可后续做"热门技能优先/冷门淘汰"。
- **跨任务共享库**:多任务顺序执行复用同一 `SkillLibrary`,直观体现累积。

## 🔧 可玩的扩展方向

1. **换检索**:把字符重叠换成真实 embedding(如 sentence-transformers),观察检索质量提升。
2. **真环境验证**:把 `_verify()` 换成代码运行/网页执行,与 Reflexion 合体。
3. **技能淘汰/合并**:库增长后做去重、合并、低频淘汰,避免膨胀。
4. **自动课程**:让 Agent 自主生成"刚好够学"的新任务(Voyager 第三组件),形成完整三件套。

## 📐 维度速查(TAXONOMY)

```
What:   Tool(Create/Master) + Context(技能库)
When:   Inter-test-time × ICL
How:    Reward-based(自评验证) · Online · On-policy · Outcome
Where:  General(文本任务)
Eval:   Adaptivity(复用率), Retention(技能库增长)
```
