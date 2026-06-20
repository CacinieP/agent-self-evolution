# Prototype: Self-Refine(最小可运行原型)

> 对应论文:[Self-Refine: Iterative Refinement with Self-Feedback](../../../surveys/papers/2023-self-refine)(NeurIPS 2023)
> TAXONOMY 定位:`What: Context(Prompt) · When: Intra-test-time × ICL · How: Reward-based(自评)`

## 🎯 这个原型做什么

复现 Self-Refine 的核心三步飞轮,直观演示**"自反馈驱动的迭代改进"**这一 Agent 自进化最基础的能力:

```
generate(生成) → feedback(自评反馈) → refine(据反馈改写) → 回到 feedback ...
```

全程**零额外训练、零外部监督**——同一个模型既是作者,又是审稿人,又是改写者。

## 📁 文件

| 文件 | 说明 |
|---|---|
| [`self_refine.py`](./self_refine.py) | 主程序,单文件,无框架依赖 |
| `requirements.txt` | 仅在真实模型模式下需要 `openai` |

## 🚀 快速开始

### 方式一:离线 Mock(无需 API,先看懂循环)
```bash
python self_refine.py --mock --task "给一个关于回收利用的简短公益标语" --iters 3
```

### 方式二:接真实模型(OpenAI 兼容)
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...        # 必填
# export OPENAI_BASE_URL=...        # 可选:指向任意 OpenAI 兼容端点
python self_refine.py --task "用一句话解释什么是 RLHF" --iters 3 --model gpt-4o-mini
```

## 🧠 实现要点

- **统一 LLM 抽象**:`LLMFn = Callable[[str], str]`,真实 / mock 后端可互换。
- **三步解耦**:`generate / feedback / refine` 各自独立,便于替换或扩展。
- **早停启发式**:当反馈被判定为"已满意"(无实质建议)时提前终止,避免无谓迭代。
- **迭代轨迹可追溯**:返回 `list[Step]`,记录每轮的输出与反馈。

## 🔧 可玩的扩展方向

1. **对比评测**:对同一任务,比较 `iters=0/1/3` 的输出质量(用 LLM-as-Judge 打分)。
2. **接 Reflexion**:把 `feedback` 换成"环境执行反馈"(如代码运行结果),即演化为 Reflexion。
3. **多 Agent**:让 generate/feedback/refine 用不同模型或 persona。
4. **奖励信号**:引入打分函数,把"是否继续 refine"从启发式升级为奖励驱动。

## 📐 维度速查(TAXONOMY)

```
What:   Context(Prompt / in-context)
When:   Intra-test-time × ICL
How:    Reward-based(自评语言反馈) · Online · On-policy · Outcome
Where:  General
Eval:   Adaptivity(可加 LLM-as-Judge)
```
