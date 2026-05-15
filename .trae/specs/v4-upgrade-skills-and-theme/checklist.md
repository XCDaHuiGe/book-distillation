# Checklist — V4.0 Skill 与工具集完整升级

## Task 1: editorial-magazine.css

### 字体体系
- [ ] 衬线字体类定义完整：`.display` / `.display-zh` / `.h1-zh` / `.h2-zh` / `.h3-zh` / `.lead` / `.big-num` / `.mid-num`
- [ ] 非衬线字体类定义完整：`.body-zh` / `.body-en`
- [ ] 等宽字体类定义完整：`.kicker` / `.meta` / `.mono`
- [ ] 字体文件通过 CDN 加载（Google Fonts 或类似）

### 5 套主题色
- [ ] 🖋 墨水经典（--ed-ink: #0a0a0b; --ed-paper: #f1efea）
- [ ] 🌊 靛蓝瓷（--ed-ink: #0a1f3d; --ed-paper: #f1f3f5）
- [ ] 🌿 森林墨（--ed-ink: #1a2e1f; --ed-paper: #f5f1e8）
- [ ] 🍂 牛皮纸（--ed-ink: #2a1e13; --ed-paper: #eedfc7）
- [ ] 🌙 沙丘（--ed-ink: #1f1a14; --ed-paper: #f0e6d2）
- [ ] 主题色通过 `data-theme="ink"` / `data-theme="indigo"` 等属性切换
- [ ] 所有颜色走 `var(--ed-*)`，无硬编码 hex

### 页面类型
- [ ] `.slide.light` 样式完整（浅色底）
- [ ] `.slide.dark` 样式完整（深色底）
- [ ] `.slide.hero` 样式完整（WebGL 背景透出）
- [ ] `.slide.hero.light` 和 `.slide.hero.dark` 区分

### 10 种布局组件
- [ ] `.hero-cover` — 开场封面
- [ ] `.act-divider` — 章节幕封
- [ ] `.big-numbers` — 数据大字报（含 stat-card 系列）
- [ ] `.text-image-split` — 左文右图（含 grid-2-7-5 等）
- [ ] `.image-grid` — 图片网格
- [ ] `.pipeline` — 流程流水线
- [ ] `.question-page` — 悬念问题页
- [ ] `.big-quote` — 大引用页（含 callout 系列）
- [ ] `.before-after` — 并列对比
- [ ] `.mixed-layout` — 图文混排

### 图片规范
- [ ] 比例类定义：`.r-16x9` / `.r-16x10` / `.r-4x3` / `.r-3x2` / `.r-1x1`
- [ ] `object-position: top` 确保只裁底部
- [ ] 网格图用固定 `height: Nvh`，无 `aspect-ratio` 定义
- [ ] 图片容器无 `border-radius` 和 `box-shadow`

### 导航系统
- [ ] `.deck-footer` 底部栏样式
- [ ] `.slide-number` 页码样式
- [ ] `#nav` 分页圆点样式

### 入场动效
- [ ] `data-anim="fade-up"` 淡入向上
- [ ] `data-anim="fade-right"` 淡入向右
- [ ] `data-anim="fade-left"` 淡入向左
- [ ] `data-anim="rise-in"` 升起
- [ ] `data-anim="zoom-pop"` 弹入
- [ ] `data-anim="stagger-list"` 列表依次出现
- [ ] 翻页过渡 `.slide { transition: opacity .5s, transform .5s }`

### 响应式
- [ ] `@media (max-width: 768px)` 移动适配
- [ ] 字体字号使用 `min(Xvw, Yvh)` 双约束
- [ ] Hero 页面在移动端正常显示

### 通用规范
- [ ] 所有自定义属性以 `--ed-` 前缀命名
- [ ] 无圆角定义（`border-radius: 0`）
- [ ] 无阴影定义（`box-shadow: none`）
- [ ] 无渐变定义（`background: linear-gradient` 不应出现在布局类中）
- [ ] T 键可切换到该主题

---

## Task 2: SKILL.md V4.0

### 设计哲学
- [ ] 新增「设计哲学」章节，清晰阐述 5 条原则
- [ ] 原则1：克制优于炫技
- [ ] 原则2：结构优于装饰
- [ ] 原则3：字体分工法则
- [ ] 原则4：图片第一公民
- [ ] 原则5：节奏靠 hero 页

### Phase 0
- [ ] 保留原逻辑种子 + 文本分级 + Python 图谱构建
- [ ] 新增 Wiki INDEX.md 生成器描述
- [ ] 新增 Wiki 目录骨架创建说明

### Phase 1
- [ ] Agent Alpha Prompt 升级（Markdown 知识库、[[双链]]、完整推导）
- [ ] Agent Beta Prompt 升级（结构化行动清单、对话体、踩坑点关联）
- [ ] Agent Gamma 新增模块8（边界约束与避坑指南）
- [ ] 3 个 Agent 新增"设计约束"（标记内容适合的布局类型）

### Phase 2
- [ ] 跨 Wiki 一致性检查描述
- [ ] 图谱校验描述

### Phase 3
- [ ] 路径A：Markdown 知识库合并生成
- [ ] 路径B：杂志风 HTML PPT 生成（引用 editorial-magazine.css 类名）
- [ ] 保留原复杂 HTML PPT 作为可选输出
- [ ] Phase 3 Prompt 改为"布局模板填充"模式，而非自由写 HTML

### Phase 4
- [ ] P0 级检查清单（字体分工、主题交替、emoji 禁用、图片规范、色系管控）
- [ ] 提供 grep 自检命令

### 保留内容
- [ ] V3.2 Python 工具链完整保留
- [ ] GraphRAG 路径完整保留
- [ ] 文本分级策略完整保留
- [ ] 降级策略完整保留
- [ ] 质量标准完整保留

### 其他
- [ ] 触发指令 `{书名}_精华内参.md` 和 `{书名}_精华内参.html` 已明确定义
- [ ] 产出物清单已更新为双轨模式

---

## Task 3: index.html 更新

### Hero 区
- [ ] "V3.2" 标记已更新为 "V4.0"
- [ ] 描述文字包含 V4.0 新增特性

### Stats 面板
- [ ] 数据已更新以反映 V4.0 变化
- [ ] 所有原有 class 名保持不变

### Feature 卡片
- [ ] 新增"杂志风主题"卡片
- [ ] 新增"知识库 AI 问答"卡片
- [ ] 新卡片使用与现有卡片相同的类名结构

### 风格确认
- [ ] 未修改任何现有 CSS 变量
- [ ] 未修改任何布局结构（grid / flex）
- [ ] 现有交付物卡片顺序和时间格式保持不变
- [ ] 页面在移动端显示正常
