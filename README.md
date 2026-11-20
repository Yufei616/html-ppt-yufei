# HTML PPT — Editorial

把已有 PPT / 大纲重新设计成 16:9 的 HTML 演示文稿：**保留主题色与内容，重做版式**。

不是把 PPT 导出成网页，而是用一套编辑设计语言重新排页面，并内置完整的演示交互：

- 单页显示，16:9 等比缩放
- 单击 / 滚轮 / 键盘 / 触屏翻页
- 左侧缩略图栏：真实页面缩略图、悬浮放大预览、点击跳转
- 总览模式：全部页面网格，点击进入
- 演讲者全屏模式（自动隐藏侧栏与控件）
- 打印导出为 13.333in × 7.5in 的 PDF，一页一张
- 纯静态单文件，离线可用，无 CDN

## 快速开始

把整个目录复制到你的 skills 目录：

```bash
# Claude Code
git clone https://github.com/Yufei616/html-ppt.git ~/.claude/skills/html-ppt

# opencode
git clone https://github.com/Yufei616/html-ppt.git ~/.config/opencode/skills/html-ppt
```

> 如果你已经装过同名的 `html-ppt` skill，请先备份或移除旧版，否则会冲突。

然后在对话里说：

> 用 html-ppt 把这份 PPT 的第 12–17 页做成 HTML 演示文稿，保留主题色，重新设计版式。

Skill 会先提取「标题 + 内容」Markdown，再按页面意图选择版式，最后基于 `assets/deck-template.html` 生成单文件 HTML。

## 手动使用模板

直接用浏览器打开：

```bash
open assets/deck-template.html
```

模板本身是一份 6 页示例（ACME 虚构数据），可以直接：

1. 修改 `:root` 中的主题 token
2. 替换每个 `<section class="slide">` 里的内容
3. 保留 `.frame`、`.deck-ui`、缩略图脚本、打印样式

## 功能与快捷键

| 操作 | 行为 |
| --- | --- |
| 单击页面 | 下一页 |
| 滚轮下 / 上 | 下一页 / 上一页 |
| `← → ↑ ↓` / 空格 / PageUp / PageDown | 翻页 |
| `Home` / `End` | 首页 / 末页 |
| `F` | 全屏（演讲者模式） |
| `O` | 所有页面总览 |
| `Esc` | 退出总览 / 全屏 |
| 触屏左右滑 | 翻页 |

缩略图栏：

- 只在普通窗口显示，全屏、总览、打印时自动隐藏
- 悬浮缩略图 → 右侧放大预览
- 点击 → 跳转
- 在侧栏上滚轮只滚动缩略图，不翻页
- 窗口宽度 < 980px 自动隐藏

## 提取 PPT 内容

```bash
pip install python-pptx
python scripts/extract_pptx.py your-deck.pptx --pages 12-17 --out content.md
```

支持 `12-17`、`12,14,16`、`all`，可选 `--include-notes`。

脚本按 top/left 顺序读取形状，输出标题与正文，并对重复文本去重。表格会转成 Markdown 表格。

## 目录

```
html-ppt/
├── SKILL.md                    # 技能主文件
├── assets/deck-template.html   # 可运行的 6 页模板
├── references/
│   ├── design-system.md        # 主题提取、字号、版式配方
│   └── viewer-spec.md          # 交互、缩略图、总览、打印、性能
├── scripts/extract_pptx.py     # PPTX → Markdown
├── examples/demo-content.md    # 示例内容提取结果
└── docs/requirements.md        # 原始需求记录
```

## 设计原则

- **只借鉴主题色和内容，不照搬 PPT 布局**
- 每页一个视觉重心，整份 deck 至少 4 种不同版式
- 深色整版页用来调节节奏，不超过约 1/3
- 数据必须来自源文件；示意数据标注 `UI Preview · 示意界面`
- 单文件、离线、系统字体

详细规范见 `references/design-system.md` 和 `references/viewer-spec.md`。

## 自定义

常见调整位置：

- 主题色：`assets/deck-template.html` 顶部 `:root`
- 侧栏宽度：`.rail`、`.thumb`、`body.rail-on .stage`，以及 `fit()` 中的 `160`
- 放大预览尺寸：`.preview` 与 `fit()/openPreview()` 中的 `472 / 265.5`
- 翻页防抖：`wheelTimer` 的 `520`
- 打印尺寸：`@media print` 中的 `@page`

## License

未附带许可证。发布到 GitHub 前请自行选择（如 MIT）。
