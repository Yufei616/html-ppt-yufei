# HTML PPT Yufei — Presentation First

把 **PPT 模板、大纲、笔记、截图或零散内容**做成 16:9 的 HTML 演示文稿。

重点在「呈现」：叙事结构、主题气质、版式节奏和演示交互。输入可以是一套模板、一段大纲、一份笔记，甚至只是一个主题。

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
git clone https://github.com/Yufei616/html-ppt-yufei.git ~/.claude/skills/html-ppt-yufei

# opencode
git clone https://github.com/Yufei616/html-ppt-yufei.git ~/.config/opencode/skills/html-ppt-yufei
```

> 如果你已经装过同名的 `html-ppt-yufei` skill，请先备份或移除旧版，否则会冲突。

然后直接说需求，例如：

> 用 html-ppt-yufei 把这份大纲做成 8 页 HTML 演示，偏编辑设计风。

> 用 html-ppt-yufei 按这套 PPT 模板做一份产品发布演示，保留模板的主题色和字体。

> 用 html-ppt-yufei 按这份产品笔记做 6 页演示，偏深色技术风。

Skill 会先确认输入类型和主题来源，再规划叙事与页面节奏，最后基于 `assets/deck-template.html` 生成单文件 HTML。

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

## 输入类型

| 输入 | 内容来源 | 主题来源 |
| --- | --- | --- |
| PPT 模板 / 品牌 | 按模板写内容 | 沿用模板 |
| 大纲 / 笔记 / Markdown | 先结构化为逐页大纲 | 推荐 2–3 套配色，或使用品牌色 |
| 截图 / 现有网页 / PDF | 重建内容 | 参考提炼或推荐 |
| 只有一个主题 | 先起草大纲 | 推荐 |

## 目录

```
html-ppt-yufei/
├── SKILL.md                    # 技能主文件
├── assets/deck-template.html   # 可运行的 6 页模板
├── references/
│   ├── design-system.md        # 主题来源、字号、版式配方
│   ├── presentation-craft.md   # 叙事、节奏、页面角色
│   └── viewer-spec.md          # 交互、缩略图、总览、打印、性能
```

## 设计原则

- **输入不限，呈现优先**：PPT 模板、大纲、笔记、截图都可以是起点
- 主题来源优先级：模板 / 品牌 > 视觉参考 > 默认方案
- 先定叙事，再定版式；每页一个 takeaway
- 每页一个视觉重心，整份 deck 至少 4 种不同版式
- 深色整版页用来调节节奏，不超过约 1/3
- 内容不改事实；自拟数据标注 `UI Preview · 示意界面`
- 单文件、离线、系统字体

详细规范见 `references/design-system.md`、`references/presentation-craft.md` 和 `references/viewer-spec.md`。

## 自定义

常见调整位置：

- 主题色：`assets/deck-template.html` 顶部 `:root`
- 侧栏宽度：`.rail`、`.thumb`、`body.rail-on .stage`，以及 `fit()` 中的 `160`
- 放大预览尺寸：`.preview` 与 `fit()/openPreview()` 中的 `472 / 265.5`
- 翻页防抖：`wheelTimer` 的 `520`
- 打印尺寸：`@media print` 中的 `@page`

## License

未附带许可证。发布到 GitHub 前请自行选择（如 MIT）。
