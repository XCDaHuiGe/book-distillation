# 设计学习资源库

> 这是一个让我学习优秀设计案例的资源库。每次生成 PPT 前，我会查阅这个库，学习其中的配色、排版、组件、动画等设计元素。

---

## 使用方法

1. 给我一个链接（GitHub 项目 / 设计网站 / 发布会视频）
2. 我会分析并提取设计要点
3. 将学习内容写入对应的 `.md` 文件
4. 生成 PPT 时自动调用这些设计参考

---

## 文件夹结构

```
design-references/
├── README.md                    ← 本文件（使用说明）
├── visual-examples/             ← 视觉案例
│   ├── presentations.md         ← 发布会/演讲 PPT 案例
│   ├── websites.md              ← 优秀网页设计案例
│   └── magazines.md             ← 杂志排版案例
├── color-systems/               ← 配色系统
│   ├── dark-themes.md           ← 深色主题配色
│   ├── light-themes.md          ← 浅色主题配色
│   └── semantic-colors.md       ← 语义色（红/绿/警告等）
├── typography/                  ← 字体排版
│   ├── font-pairing.md          ← 字体搭配
│   ├── type-scale.md            ← 字号层级
│   └── editorial-style.md       ← 编辑风格排版
├── animation-effects/           ← 动画特效
│   ├── entrance-animations.md   ← 入场动画
│   ├── micro-interactions.md    ← 微交互
│   └── page-transitions.md      ← 页面切换
└── layout-patterns/             ← 布局模式
    ├── hero-sections.md         ← 首屏/封面布局
    ├── data-visualization.md    ← 数据可视化布局
    └── quote-sections.md        ← 金句页布局
```

---

## 当前已学习的设计资源

| 来源 | 学到的内容 | 文档位置 |
|:---|:---|:---|
| frontend-slides | 12种风格预设、反AI审美 | `references/style-presets.md` |
| Slidev | 演讲者模式、绘图标注 | `SKILL.md` |
| reveal.js | 键盘导航、主题切换 | `SKILL.md` |
| Marp | Markdown驱动幻灯片 | `SKILL.md` |
| PptxGenJS | Slide Masters 布局系统 | `references/layouts.md` |
| 5维升维法 | 氛围系统、发布会级排版 | `SKILL.md` |
| **站酷设计作品** | 霓虹科技风、赛博朋克、数据可视化配色 | `design-references/visual-examples/zcool-designs.md` |

---

## 待学习资源（请提供链接）

在这里添加你想让我学习的设计资源链接：

### 发布会/演讲类
- [ ] Apple Keynote 风格分析
- [ ] Huawei 发布会风格分析
- [ ] Google I/O 风格分析
- [ ] 其他：____________

### 网页/幻灯片项目
- [ ] ____________
- [ ] ____________

### 设计系统
- [ ] ____________
- [ ] ____________

---

## 如何添加新学习资源

### 方式1：直接给我链接

```
学习这个链接的设计风格：https://xxx.com
```

我会：
1. 访问链接，分析设计元素
2. 提取配色、排版、组件、动画
3. 写入对应的 `.md` 文件
4. 更新"当前已学习"表格

### 方式2：告诉我设计要点

```
我喜欢这种风格：
- 深黑背景 + 金色强调
- 标题超大，正文超小
- 大量留白
```

我会：
1. 将你的偏好写入 `visual-examples/user-preferences.md`
2. 生成 PPT 时优先遵循这些偏好

---

## 设计调用机制

生成 PPT 时，我会按以下顺序查阅设计资源：

1. **用户偏好** → `visual-examples/user-preferences.md`
2. **内容类型匹配** → 根据书籍类型选择对应风格
3. **配色系统** → `color-systems/` 中选择合适的主题
4. **排版参考** → `typography/` 中的字号层级
5. **动画参考** → `animation-effects/` 中的入场动画
6. **布局参考** → `layout-patterns/` 中的页面结构

---

## 快速开始

给我一个链接，让我开始学习：

```
学习这个项目的 PPT 设计：https://github.com/xxx/xxx
```
