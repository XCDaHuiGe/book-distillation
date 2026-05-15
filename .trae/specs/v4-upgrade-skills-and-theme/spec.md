# Book Distillation V4.0 — Skill 与工具集完整升级 Spec

## Why

项目从 V3.2 升级到 V4.0，需要完成三个独立层面的升级：

1. **底层优化**：参考 `code.html`（Karpathy Wiki 模式），从"PPT 唯一终点"升级为"知识库驱动 + 双轨产出"
2. **html-ppt生成优化**：参考 guizang-ppt-skill，引入"电子杂志 × 电子墨水"风格，解决输出 PPT 不好看的问题
3. **index.html 更新**：GitHub Pages 入口页新增 V4.0 内容卡片，不破坏现有风格

这三个部分彼此独立，可并行实施。

---

## Part 1: 底层优化（Karpathy Wiki 知识库驱动）

### 变更内容

#### 1.1 SKILL.md 架构升级
- 产出模型从"PPT HTML 唯一终点"改为"双轨产出"
- **第一产出物**：Markdown 知识库（Wiki.md）— 面向 AI 问答的完整推导
- **第二产出物**：杂志风 HTML PPT — 面向人类阅读的视觉精华

#### 1.2 新增 Phase 0 Wiki 骨架生成
在原有逻辑种子生成后，增加 Wiki INDEX.md 生成：
- INDEX.md 是面向 AI 的路由文件，包含 🎯核心支柱 / 💡颠覆认知 / 🪜落地行动 / 🚫边界约束
- 使用 Markdown 内部链接指向具体 wiki 文件
- 每个条目包含一句话摘要

#### 1.3 升级 3-Agent Prompt（Phase 1）

**Agent Alpha（架构师）升级：**
- 产出不再面向 PPT 排版，而是面向 Markdown 知识库
- 每个知识点建立独立 Markdown 页面逻辑
- 使用 `[[双链]]` 指向其他概念
- 每个支柱：本质 + 推导过程（引用原文） + 逻辑串联 + 关联实体
- 每个洞见：观点陈述 + 常见误解 + 书中真相 + 推导路径

**Agent Beta（实战派）升级：**
- 产出沉淀为结构化行动清单和场景脚本
- 准备-执行-复盘指南：步骤拆解 + 踩坑点关联 `[[边界约束X]]`
- 应用场景：Markdown 对话体 + 错误 vs 理想路径对比

**Agent Gamma（策展人）升级：**
- **新增模块8：边界约束与避坑指南**
  - 🚫 红线清单（不可逾越的底线）
  - ⚠️ 致命误区（常见错误操作）
  - 🛡️ 适用边界（理论/方法的适用条件）

#### 1.4 新增 Phase 3 双轨产出
- **产出1**：合并生成 `{书名}_精华内参.md`（保持所有 [[双链]] + 术语字典）
- **产出2**：基于仓库生成的 magazine 风格 HTML PPT

#### 1.5 Phase 4 交付检查
- 确认输出目录包含 `{书名}_精华内参.md`，文件大小合理，包含完整推导细节
- 确认 `{书名}_精华内参.html` 打开即呈现内容
- 保留 `wiki/` 目录结构以支持增量更新

### 保留部分
- V3.2 的全部 Python 工具链（build_index.py、search.py、graph.py、multihop.py 等）
- GraphRAG 路径（FAISS + NetworkX + Agent 检索）
- 文本分级与处理路径（≤10万 / 10-30万 / 30-60万 / >60万）

---

## Part 2: html-ppt生成优化（杂志风主题）

### 变更内容

#### 2.1 新增 editorial-magazine.css 主题
在 `ppt-assets/themes/` 下创建新主题文件，引入 guizang-ppt-skill 的设计系统。

**字体体系：**
- 衬线（Noto Serif SC / Playfair Display）→ 标题、重点金句、数字（视觉重音）
- 非衬线（Noto Sans SC / Inter）→ 正文、描述（信息密度）
- 等宽（IBM Plex Mono / JetBrains Mono）→ kicker、meta、foot（装饰节奏）

**5 套预设主题色（不允许自定义）：**
- 🖋 墨水经典：墨黑 + 暖米白（通用/商业/默认）
- 🌊 靛蓝瓷：深靛蓝 + 瓷白（科技/研究/数据）
- 🌿 森林墨：森林绿 + 象牙（自然/文化/非虚构）
- 🍂 牛皮纸：深棕 + 暖米（怀旧/人文/文学）
- 🌙 沙丘：炭灰 + 沙色（艺术/设计/创意）

**页面类型系统（light/dark/hero）：**
- `light`：浅色底，适合数据、图片网格、pipeline 流程图
- `dark`：深色底，适合正文对比、引用
- `hero light / hero dark`：视觉主导页（封面/幕封/问题/大引用），WebGL 背景透出
- 硬规则：连续 3 页以上相同主题 = 不允许；必须有 light 和 dark 交替

**10 种布局组件类：**
1. `.hero-cover` — 开场封面（大标题 + 副标题 + 引导语 + 元数据）
2. `.act-divider` — 章节幕封（kicker + 巨标题 + 引语）
3. `.big-numbers` — 数据大字报（stat-card 网格，3×2 分布）
4. `.text-image-split` — 左文右图（引用 + 图片，grid-2-7-5 结构）
5. `.image-grid` — 图片网格（多图对比，固定 height 裁切）
6. `.pipeline` — 流程流水线（垂直步骤 + 连线和节点）
7. `.question-page` — 悬念问题页（大问题 + 引语）
8. `.big-quote` — 大引用页（衬线金句 + 作者出处）
9. `.before-after` — 并列对比（旧 vs 新）
10. `.mixed-layout` — 图文混排（信息密集页）

**图片规范：**
- 标准比例类：`.r-16x9` / `.r-16x10` / `.r-4x3` / `.r-3x2` / `.r-1x1`
- 只裁底部，左右和顶部完整（`object-position: top`）
- 网格图用固定 `height: Nvh`，不用 `aspect-ratio`
- 无圆角、无阴影

**导航系统：**
- `deck-footer`：底部信息栏（书名 + 页码）
- `slide-number`：自动页码 `data-current / data-total`
- `nav` 分页圆点

**入场动效：**
- CSS transition 方案（零 JS 依赖）
- 元素级 `data-anim` 属性驱动（fade-up / fade-right / stagger-list 等）
- 翻页过渡 `transition: opacity .5s, transform .5s`

**响应式：**
- `@media (max-width: 768px)` 移动适配
- 字体字号用 `min(Xvw, Yvh)` 双约束

#### 2.2 改造 Phase 3 Prompt
- Agent 从"自由写 HTML + CSS" 改为"从 10 种布局模板中选取 + 填空"
- 先生成内容结构（标记每个模块用哪种布局），再填充到预定义类名中
- 字体类名自动映射（标题→衬线、正文→非衬线、元数据→等宽）
- 每页自动分配 light/dark 主题并生成主题节奏表

#### 2.3 新增 Phase 4 质量检查清单
- P0 级检查（必须通过）：字体分工、主题交替、emoji 禁用、图片规范、色系管控
- P1 级检查（推荐通过）：动画使用、间距一致性、对比度
- 提供 grep 自检命令

---

## Part 3: index.html 更新

### 变更内容
- Hero 区域的 "V3.2" 标记更新为 "V4.0"
- 新增 V4.0 特性的 Feature 卡片（如"杂志风主题"、"知识库 AI 问答"）
- Stats 面板更新：新增 V4.0 指标（如"主题"从 36→37）
- 保持现有 cyberpunk/glassmorphism 风格完全不变
- 不修改任何 CSS 变量或布局结构

---

## 文件变更清单

| 文件 | 操作 | 说明 |
|:---|:---|:---|
| `SKILL.md` | 完全重写 | V3.2 → V4.0，融合 Karpathy Wiki + 杂志风 |
| `ppt-assets/themes/editorial-magazine.css` | 新建 | 杂志风完整主题 |
| `index.html` | 修改 | 更新 V4.0 内容标记 |

## 不涉及的文件
- `tools/` 下的 Python 脚本 — 不变
- `ppt-assets/base.css` — 不变（杂志风主题自行承载所有样式）
- `ppt-assets/runtime.js` — 不变
- `ppt-assets/animations/` — 不变
- `code.html` — 作为设计参考文档保留
- 已有的 `*_精华内参.html` — 不变

## 依赖关系
- Task 2（SKILL.md）中 Phase 3 引用了 Task 1（editorial-magazine.css）中定义的类名
- Task 3（index.html）独立于 Task 1 和 Task 2
