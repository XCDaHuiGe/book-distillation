# Tasks — V4.0 Skill 与工具集完整升级

---

## Task 1: 新建杂志风 CSS 主题 editorial-magazine.css

创建 `ppt-assets/themes/editorial-magazine.css`，实现完整的杂志风设计系统。

**内容要求：**
- 字体体系：衬线标题（Noto Serif SC / Playfair Display）+ 非衬线正文（Noto Sans SC / Inter）+ 等宽元数据（IBM Plex Mono / JetBrains Mono）
- 5 套预设主题色 CSS 变量（墨水经典、靛蓝瓷、森林墨、牛皮纸、沙丘），由 `:root` 的 `data-theme` 属性切换
- light / dark / hero light / hero dark 四种页面类型样式
- 10 种布局组件类（hero-cover / act-divider / big-numbers / text-image-split / image-grid / pipeline / question-page / big-quote / before-after / mixed-layout）
- 图片比例类（.r-16x9 / .r-16x10 / .r-4x3 / .r-3x2 / .r-1x1）及裁切规则
- 导航系统（deck-footer / slide-number / nav 圆点）
- CSS transition 入场动效（data-anim 属性驱动）
- 移动端 @media 响应式规则
- 所有自定义属性以 `--ed-` 前缀命名，避免与 base.css 冲突
- 无圆角、无阴影、无渐变定义
- 被 base.css 或 theme 系统自动发现，T 键可切换

---

## Task 2: 重写 SKILL.md 到 V4.0

完全重写 `SKILL.md`，保留 V3.2 全部工具链能力，融合 V4.0 Karpathy Wiki 底层优化 + 杂志风设计哲学。

**内容要求（五大部分）：**

### Phase 0（增强）
- 保留原有逻辑种子提取 + 文本分级 + Python 图谱构建
- 新增：Wiki INDEX.md 生成器（面向 AI 的路由文件）
- 新增：Wiki 目录骨架创建（concepts/ / actions/ / boundaries/ / entities/）

### Phase 1（3-Agent Prompt 升级）
- **Agent Alpha**：产出面向 Markdown 知识库，使用 `[[双链]]`，每个支柱含本质/推导/逻辑串联/关联实体
- **Agent Beta**：产出结构化行动清单 + 场景模拟对话体 + 踩坑点关联 `[[边界约束X]]`
- **Agent Gamma**：新增模块8「边界约束与避坑指南」（红线清单 / 致命误区 / 适用边界）
- **新增"设计约束"**：3 个 Agent 输出时需标记内容适合哪种布局类型

### Phase 2（新增 Wiki 一致性守护）
- 跨 Wiki 一致性检查（双链指向核实、矛盾标记、术语统一）
- 图谱校验（验证关键概念间在图谱中存在有效路径）

### Phase 3（双轨产出）
- **路径A**：合并生成 Markdown 知识库 `{书名}_精华内参.md`
- **路径B**：基于布局模板库生成杂志风 HTML PPT（引用 editorial-magazine.css 类名）
- 保留原有复杂 HTML PPT 的生成能力作为可选输出

### Phase 4（质量检查）
- P0 级检查项（字体分工、主题交替、emoji 禁用、图片规范、色系管控）
- 提供 grep 自检命令

### 新增「设计哲学」章节
- 克制优于炫技
- 结构优于装饰（不用阴影、不用浮动卡片、靠字号+字体对比+留白）
- 字体分工法则（衬线=标题/数字、非衬线=正文、等宽=元数据）
- 图片第一公民（只裁底部、标准比例、无圆角）
- 节奏靠 hero 页（hero / non-hero 交替）

### 保留内容
- 全部 Python 工具链（build_index.py / search.py / graph.py / multihop.py 等）
- GraphRAG 路径（FAISS + NetworkX + Agent 检索）
- 文本分级策略（≤10万 / 10-30万 / 30-60万 / >60万）
- 降级策略
- 质量标准

---

## Task 3: 更新 index.html

GitHub Pages 入口页新增 V4.0 内容，不破坏现有 cyberpunk/glassmorphism 风格。

**变更内容：**
- Hero 区 "V3.2" 标记更新为 "V4.0"
- Hero 区描述文字增加 V4.0 特性描述（知识库 + 杂志风）
- Stats 面板更新（例如主题数 36→37 或新增杂志风主题指标）
- Feature 卡片区域新增两个卡片："杂志风主题"和"知识库 AI 问答"
- 所有现有 class 名、样式、布局结构完全不变
- 保持时间倒序的交付物列表

---

## Task Dependencies
- Task 2 (SKILL.md) 需要引用 Task 1 (editorial-magazine.css) 中定义的类名
- Task 3 (index.html) 独立于 Task 1 和 Task 2
- Task 1 可独立先行
- 执行顺序：Task 1 → Task 2 → Task 3（但 Task 3 可与 Task 1 并行）
