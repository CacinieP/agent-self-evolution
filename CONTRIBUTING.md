# Contributing to Agent Self-Evolution

感谢你愿意为这个仓库贡献!🎉 无论是补充论文、提交笔记、复现实验还是修正错别字,都非常欢迎。

## 📋 我可以贡献什么?

| 类型 | 位置 | 示例 |
|---|---|---|
| 新论文 / 综述 | `surveys/papers/` | 一篇刚发布的 self-evolution 综述 |
| 阅读笔记 | `surveys/notes/` | 对某篇论文的中文/英文解读 |
| 技术博客 / 文章 | `surveys/articles/` | 某团队发布的技术博客链接与摘要 |
| 复现实验 | `practices/experiments/` | 复现 SPIN / Reflexion 的实验记录 |
| 最小原型 | `practices/prototypes/` | 可运行的 demo |
| 代码片段 / 工具 | `practices/snippets/` | 有用的 prompt、评测脚本 |
| 评测基准信息 | `benchmarks/` | 新基准的说明与排行榜快照 |
| 演讲 / 视频 | `resources/` | 某会议 talk 的 slides/视频链接 |

## 🛠️ 贡献流程

1. **Fork** 本仓库并 clone 到本地。
2. 创建分支:`git checkout -b feat/add-spin-paper`。
3. 按下面的**命名与目录规范**添加内容。
4. 提交:`git commit -m "docs: add SPIN paper note"`。
5. 推送并开启 **Pull Request**。
6. 等待 review,合并后即出现在仓库中。

## 📐 命名与目录规范

### 论文 (`surveys/papers/`)

```
surveys/papers/
└── 2024-sp-self-rewarding-lms/
    ├── README.md          # 标题/作者/链接/摘要/贡献点
    ├── notes.md           # (可选)你的阅读笔记
    └── paper.pdf          # (可选)PDF,注意版权
```

**`README.md` 模板**:
```markdown
# 论文标题

- **作者**:Author A, Author B
- **机构**:Institution
- **发表**:NeurIPS 2024 / arXiv 2024
- **链接**:arXiv `<id>` 或会议/项目页 URL
- **代码**:GitHub 仓库 URL(若有)

## 一句话总结
...

## 核心方法
...

## 关键贡献
...

## 个人点评 / 启发
...
```

### 实验 (`practices/experiments/`)

每个实验一个目录,需包含:
- `README.md`:目的、方法、环境、结果
- 可复现脚本
- 结果数据 / 日志(大文件用 git-lfs 或外部链接)

### 提交信息 (Commit Message)

参考 [Conventional Commits](https://www.conventionalcommits.org/):
- `docs: add survey on agent self-evolution`
- `feat: add reflexion prototype`
- `fix: correct typo in taxonomy`
- `exp: reproduce SPIN on llama-3`

## ✅ PR 检查清单

- [ ] 内容放置在正确目录
- [ ] 文件命名清晰、无中文空格问题
- [ ] 引用的链接有效
- [ ] 若为复现,标注使用的模型、环境、随机种子
- [ ] 不提交受版权限制的大文件(论文 PDF 请谨慎)

## 💬 讨论

- 大方向讨论 → [GitHub Discussions](https://github.com/CacinieP/agent-self-evolution/discussions)(如已开启)
- 具体 bug / 建议 → [Issues](https://github.com/CacinieP/agent-self-evolution/issues)

再次感谢你的贡献!❤️
