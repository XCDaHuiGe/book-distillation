# 📚 Book Distillation V6.0 — 长文本深度蒸馏系统

<div align="center">

**融合 7 大开源项目，将数十万字巨著转化为杂志风 HTML PPT 精华内参**

[![GitHub stars](https://img.shields.io/github/stars/XCDaHuiGe/book-distillation?style=social)](https://github.com/XCDaHuiGe/book-distillation/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/XCDaHuiGe/book-distillation?style=social)](https://github.com/XCDaHuiGe/book-distillation/network/members)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[在线演示](#在线演示) • [快速开始](#快速开始) • [功能特性](#功能特性) • [技术架构](#技术架构)

</div>

---

## 🎯 项目简介

Book Distillation V6.0 是一个融合 **GraphRAG + Agentic RAG + 语义检索** 的长文本深度蒸馏系统。融合 frontend-slides、Slidev、reveal.js、Marp、Magic UI、PptxGenJS 七大开源项目的设计理念，通过三层检索策略与 3-Agent 协作，将数十万字的书籍/文档转化为杂志风 HTML PPT 精华内参。

### 核心价值

- **🚀 高效提炼**：语义向量检索 + 知识图谱验证 + 多跳推理，三层策略确保精度
- **🎨 杂志风设计**：WebGL 粒子背景、演讲者模式、绘图标注、LaTeX 公式、Mermaid 图表
- **🧠 知识图谱**：NetworkX 构建概念关系网络，支持图遍历与多跳推理检索
- **🎯 双轨产出**：路径A → Markdown 知识库（AI 问答）；路径B → 杂志风 HTML PPT
- **📄 多格式输入**：支持 EPUB / PDF（含OCR扫描版） / TXT / MD

---

## ✨ 功能特性

### 📖 五阶段蒸馏流程

```
Phase 0: 索引构建 → Phase 1: 3-Agent 蒸馏 → Phase 2: 一致性验证 → Phase 3: HTML 生成 → Phase 4: 交付
```

1. **Phase 0 — 索引构建**：逻辑种子提取、Wiki 知识库骨架创建、sentence-transformer 语义索引、NetworkX 知识图谱
2. **Phase 1 — 3-Agent 蒸馏**：Alpha 架构师、Beta 实战派、Gamma 策展人协作，支持小说专项模式
3. **Phase 2 — 一致性验证**：逻辑对齐、术语校准、图谱校验、[[双链]] 交叉检查
4. **Phase 3 — HTML 生成**：10 种布局骨架 → 5 套主题色 → WebGL 背景 → 配图填充
5. **Phase 4 — 交付**：质量门控、双轨产出（Markdown + HTML PPT）

### 🤖 3-Agent 协作蒸馏

- **Agent Alpha：架构师** — 一句话逻辑、核心知识地图、颠覆性认知
- **Agent Beta：实战派** — 落地行动指南、场景模拟、自检卡
- **Agent Gamma：策展人** — 金句复刻、蒸馏清单、行动地图、边界约束

### 📊 八大模块输出

1. **一句话逻辑** — 揭示全书核心命题
2. **核心知识地图** — 概念/模型/方法论的可视化呈现
3. **颠覆性认知** — 反常识洞见，原文证据支撑
4. **落地行动指南** — 准备→执行→复盘全流程
5. **金句复刻** — 作者原话精华
6. **知识蒸馏清单** — 被省略但值得留意
7. **延伸行动地图** — 后续行动建议
8. **边界约束** — 红线清单 + 致命误区 + 适用边界

### 🎨 HTML PPT 生成（V6.0 融合升级）

| 特性 | 来源 | 说明 |
|:---|:---|:---|
| **零依赖单 HTML** | frontend-slides | 无需构建，浏览器直接打开 |
| **WebGL 粒子背景** | 自研 | 自动适配 light/dark 主题 |
| **12 种风格预设** | frontend-slides | 反 AI 审美，抽象形状优先 |
| **演讲者模式** | Slidev / reveal.js | S 键开启，独立窗口显示备注 |
| **绘图标注** | Slidev | D 键开启画笔，多色可选 |
| **LaTeX 数学公式** | Slidev | KaTeX 渲染 |
| **Mermaid 图表** | Slidev | 文本描述生成流程图 |
| **Slide Masters 布局** | PptxGenJS | 10种布局骨架 + 5套主题色 |

---

## 🚀 快速开始

### 前置要求

- Python 3.8+
- Node.js 14+（可选，用于本地预览）

### 安装依赖

```bash
cd tools
pip install -r requirements.txt
```

### 使用方法

#### 方法一：使用Skill（推荐）

在Trae IDE中，直接调用skill：

```
Use Skill: book-distillation-v3
`path/to/your/book.epub` [主题名称]
```

支持的文件格式：
- `.epub` - 标准电子书格式
- `.pdf` - 文字版PDF直接处理
- `.txt` / `.md` - 纯文本/标记文件
- `.json` - 预处理后的章节JSON（含OCR结果）

示例：
```
Use Skill: book-distillation-v3
`关键对话如何高效能沟通.epub` [corporate-clean]
```

#### 方法二：命令行使用

```bash
# 1. 提取EPUB内容
python tools/extract_epub_chapters.py path/to/book.epub

# 2. 提取PDF文本（文字版PDF）
python tools/extract_chapters.py path/to/book.pdf

# 3. OCR提取扫描版PDF
python tools/extract_pdf_ocr.py path/to/scanned_book.pdf

# 4. 构建知识图谱
python tools/build_knowledge_graph.py

# 5. 多跳推理检索
python tools/multihop.py

# 6. 文本分割/建索引
python tools/segment_text.py
python tools/build_index.py

# 7. 生成PPT
# （需要调用html-ppt skill）
```

### 查看结果

```bash
# 启动本地服务器
python -m http.server 8000

# 浏览器打开
# http://localhost:8000/书名_精华内参.html
```

---

## 📁 项目结构

```
book-distillation/
├── SKILL.md                      # Skill 主文档（V6.0）
├── README.md                     # 项目说明文档
├── index.html                    # 项目首页（交付物展示）
├── demo.html                     # V6.0 功能演示
│
├── assets/                       # 模板与资源
│   └── template.html             # HTML PPT 模板（含 WebGL/演讲者/绘图）
│
├── references/                   # 设计参考文档
│   ├── layouts.md                # 10 种布局骨架
│   ├── themes.md                 # 5 套主题色预设
│   ├── style-presets.md          # 12 种风格预设
│   ├── animation-patterns.md     # 动画模式指南
│   └── image-prompts.md          # 配图生成指南
│
├── tools/                        # 工具脚本
│   ├── extract_epub_chapters.py  # EPUB 内容提取
│   ├── extract_chapters.py       # PDF 章节提取
│   ├── extract_pdf_ocr.py        # 扫描版 PDF OCR 识别
│   ├── build_index.py            # sentence-transformer 语义索引构建
│   ├── segment_text.py           # 长文本智能分割
│   ├── search.py                 # 语义检索（三层策略第1层）
│   ├── graph.py                  # 图谱操作（三层策略第2层）
│   ├── multihop.py               # 多跳推理（三层策略第3层）
│   ├── build_knowledge_graph.py  # 知识图谱构建
│   ├── quality_check.py          # 质量检查
│   ├── setup.py                  # 依赖安装脚本
│   └── requirements.txt          # Python 依赖
│
├── distillation_output/          # 蒸馏输出
│   ├── 逻辑种子_遥远的救世主.md   # 逻辑种子（可复用）
│   ├── 逻辑种子_申论写作八讲.md   # 逻辑种子（可复用）
│   ├── 逻辑种子_155规划纲要.md    # 逻辑种子（可复用）
│   └── ...
│
└── *.html                        # 生成的 HTML PPT
    ├── 遥远的救世主_精华内参.html
    ├── 申论写作八讲_精华内参.html
    ├── 155规划纲要_精华内参.html
    ├── 关键对话_精华内参.html
    └── 不要挑战人性_精华内参.html
```

---

## 🎨 在线演示

### 示例1：《遥远的救世主》

- **页数**：38页
- **字数**：34.8万字
- **类型**：文学·哲学（小说专项模式）
- **核心内容**：
  - 叙事内核：文化属性决定命运，世上没有救世主
  - 人物谱系：丁元英、芮小丹、韩楚风、林雨峰、刘冰等9人弧线分析
  - 情节线索网：主线起承转合 + 3条支线 + 7个伏笔追踪
  - 关键场景复原：8张场景卡片（天国的女儿/审讯王明阳/五台山问道/退股潮/芮小丹殉道/白纸档案袋等）
  - 金句复刻：12条核心金句 + 场景上下文
  - 叙事边界：5个不可翻译细节 + 5个关键沉默

### 示例2：《十五五规划纲要》

- **页数**：28页
- **篇幅**：18篇、62章
- **类型**：政策文件
- **核心内容**：
  - 18大战略领域：科技创新、产业升级、数字经济等
  - 40余项核心指标：GDP增速、研发投入、绿色转型等
  - 语义级重构：将官方文本转化为可理解的结构化知识

### 示例3：《申论写作八讲》

- **页数**：30页
- **字数**：17.5万字
- **类型**：工具书
- **核心内容**：
  - 8大支柱：从"玄学"到工程化训练
  - 4项基本功：阅读、分析、逻辑、表达
  - 5大题型攻坚：概括、分析、对策、公文、大作文

### 示例4：《关键对话》

- **页数**：40页
- **类型**：商业
- **核心内容**：
  - 7大技巧 + 2大原则
  - 结构化对话决策树 + 心理博弈图谱

### 示例5：《不要挑战人性》

- **页数**：22页
- **类型**：心理学
- **核心内容**：
  - 10大支柱：早期依恋、环境权威、认知偏差、自我实现、情绪机制、关系塑造、身心一体、拖延调节、良知道德、正念觉知
  - 9个颠覆性认知：挑战传统人性观念
  - 落地行动指南：5大主题场景模拟

---

## 🛠️ 技术架构

### 核心技术栈

- **GraphRAG + Agentic RAG**：基于图谱的检索增强生成
- **Sentence-Transformers**：语义向量检索（shibing624/text2vec-base-chinese）
- **NetworkX + FAISS**：知识图谱 + 向量索引
- **HTML/CSS/JS**：零依赖单 HTML PPT 生成

### 三层检索策略

```
第3层：多跳推理（深度）→ multihop.py + graph.py
第2层：图谱关系验证（精度）→ graph.py --entity --depth
第1层：语义向量召回（广度）→ search.py（sentence-transformer）
```

### 技术亮点

1. **语义检索升级**：TF-IDF → sentence-transformer，真正理解中文语义
2. **双轨产出**：Markdown 知识库（AI 问答） + 杂志风 HTML PPT
3. **小说专项模式**：叙事分析、场景复原、伏笔追踪、意象体系
4. **[[双链]] 体系**：概念间可追溯、可交叉引用

### 快捷键

| 按键 | 功能 |
|:---|:---|
| `←` `→` | 翻页 |
| `S` | 演讲者模式 |
| `D` | 绘图标注 |
| `T` | 切换主题 |

---

## 📊 质量保证

### 硬门控检查

- ✅ 章节覆盖率 = 100%
- ✅ 核心支柱 ≥ 3处章节引用
- ✅ 后期章节(>80%)在PPT中有对应页
- ✅ 每个支柱有实验/案例支撑
- ✅ 无"AI味"表述（"综上所述"、"值得注意的是"等）
- ✅ 核心隐喻贯穿全文

### 完整性检查

- ✅ 所有模块都已生成
- ✅ 知识图谱已构建
- ✅ PPT页数符合预期
- ✅ 导航功能完整

---

## 🤝 贡献指南

欢迎贡献代码、提出问题或建议！

### 贡献方式

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 代码规范

- 遵循 PEP 8 Python 代码规范
- 添加必要的注释和文档
- 编写单元测试

---

## 📝 更新日志

### V6.0 (2026-05-16)

- ✨ 融合 7 大开源项目：frontend-slides、Slidev、reveal.js、Marp、Magic UI、PptxGenJS
- ✨ HTML PPT 全面升级：WebGL 粒子背景、演讲者模式、绘图标注
- ✨ LaTeX 数学公式 + Mermaid 图表渲染
- ✨ 10 种布局骨架 + 5 套主题色 + 12 种风格预设
- ✨ 语义检索升级：TF-IDF → sentence-transformer（中文语义理解）
- ✨ 三层检索策略：语义召回 → 图谱验证 → 多跳推理
- ✨ Slide Masters 模板系统：编程式布局组合
- 📦 新增交付物：遥远的救世主（小说专项模式）
- 🎨 demo.html 功能演示页

### V4.0 (2026-05-13)

- ✨ 新增：双轨产出（Markdown 知识库 + 杂志风 HTML PPT）
- ✨ 新增：10 种杂志布局模板
- ✨ 新增：5 套主题色预设
- ✨ 新增：Wiki 知识库骨架（[[双链]] 驱动）
- ✨ 新增：模块8 边界约束与避坑指南
- ✨ 新增：小说专项模式（叙事分析/场景复原/伏笔追踪）
- 🎨 优化：字体分工法则（衬线/非衬线/等宽三级体系）

### V3.1 (2026-05-10)

- ✨ 新增：3-Agent协作蒸馏机制
- ✨ 新增：知识图谱自动构建
- ✨ 新增：36种PPT主题、47种动画
- 🐛 修复：页码显示不一致问题
- 🐛 修复：导航功能缺失问题
- 🎨 优化：清理过程性文件，保持目录整洁

### V3.0 (2026-05-09)

- 🎉 初始版本发布
- ✨ 实现5阶段蒸馏流程
- ✨ 支持EPUB格式输入
- ✨ 生成HTML PPT输出

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

感谢以下开源项目的支持：

| 项目 | 融合内容 |
|:---|:---|
| [frontend-slides](https://github.com/zarazhangrui/frontend-slides) | 零依赖单 HTML、12 种风格预设 |
| [Slidev](https://github.com/slidevjs/slidev) | 演讲者模式、绘图标注、LaTeX、Mermaid |
| [reveal.js](https://github.com/hakimel/reveal.js) | 演讲者模式、触屏翻页 |
| [Marp](https://github.com/marp-team/marp) | Markdown 驱动幻灯片设计理念 |
| [Magic UI](https://github.com/magicuidesign/magicui) | 动画与视觉效果 |
| [PptxGenJS](https://github.com/gitbrent/PptxGenJS) | Slide Masters 布局系统 |
| [Three.js](https://github.com/mrdoob/three.js) | WebGL 粒子背景灵感 |

---

## 📧 联系方式

- **GitHub**: [@XCDaHuiGe](https://github.com/XCDaHuiGe)
- **项目主页**: [https://github.com/XCDaHuiGe/book-distillation](https://github.com/XCDaHuiGe/book-distillation)

---

<div align="center">

**如果这个项目对你有帮助，请给一个 ⭐️ Star！**

Made with ❤️ by XCDaHuiGe

</div>