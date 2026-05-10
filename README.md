# 📚 Book Distillation V3 - 长文本深度蒸馏系统

<div align="center">

**将数十万字巨著转化为PPT式HTML精华内参**

[![GitHub stars](https://img.shields.io/github/stars/XCDaHuiGe/book-distillation?style=social)](https://github.com/XCDaHuiGe/book-distillation/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/XCDaHuiGe/book-distillation?style=social)](https://github.com/XCDaHuiGe/book-distillation/network/members)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[在线演示](#在线演示) • [快速开始](#快速开始) • [功能特性](#功能特性) • [技术架构](#技术架构)

</div>

---

## 🎯 项目简介

Book Distillation V3 是一个基于 **GraphRAG + Agentic RAG** 的长文本深度蒸馏系统。通过"逻辑种子"提取、Python认知图谱构建与3-Agent智能体检索协作，将数十万字的书籍转化为结构化、可视化的PPT式HTML精华内参。

### 核心价值

- **🚀 高效提炼**：自动提取书籍核心概念、模型、方法论
- **📊 可视化呈现**：生成精美的HTML PPT，支持36种主题、47种动画
- **🧠 知识图谱**：自动构建概念关系网络，支持交互式探索
- **🎯 实用导向**：不仅提炼知识，更提供落地行动指南

---

## ✨ 功能特性

### 📖 五阶段蒸馏流程

```
Phase 1: 加载 → Phase 2: 蒸馏 → Phase 3: 拼接 → Phase 4: 生成 → Phase 5: 清理
```

1. **加载阶段**：EPUB内容提取、章节结构化、质量检查
2. **蒸馏阶段**：逻辑种子提取、3-Agent协作蒸馏、知识图谱构建
3. **拼接阶段**：模块整合、硬门控验证、完整性检查
4. **生成阶段**：PPT大纲设计、布局设计、主题应用、动效添加
5. **清理阶段**：临时文件清理、资源优化

### 🤖 3-Agent协作蒸馏

- **Alpha Agent**：负责核心概念提取和术语字典构建
- **Beta Agent**：负责知识模块化和逻辑结构梳理
- **Gamma Agent**：负责场景模拟和行动指南设计

### 📊 七大模块输出

1. **一句话逻辑**：核心问题、核心观点、关键洞察
2. **核心知识地图**：概念、模型、方法论的可视化呈现
3. **颠覆性认知**：挑战传统认知的洞见
4. **落地行动指南**：准备-执行-复盘全流程
5. **金句复刻**：作者原话精华
6. **知识蒸馏清单**：核心概念速查表
7. **延伸行动地图**：后续行动建议

### 🎨 HTML PPT生成

- **36种主题**：corporate-clean、minimal-white、swiss-grid、nord等
- **47种动画**：fade-up、zoom-pop、stagger-list、particle-burst等
- **完整导航**：键盘、鼠标点击、滚轮滚动
- **演讲者模式**：按S键开启，查看备注
- **主题切换**：按T键实时切换主题

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

示例：
```
Use Skill: book-distillation-v3
`关键对话如何高效能沟通.epub` [corporate-clean]
```

#### 方法二：命令行使用

```bash
# 1. 提取EPUB内容
python tools/extract_epub_chapters.py path/to/book.epub

# 2. 构建知识图谱
python tools/build_knowledge_graph.py

# 3. 生成PPT
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
├── SKILL.md                      # Skill主文档（V3.1）
├── README.md                     # 项目说明文档
│
├── ppt-assets/                   # HTML PPT框架资源
│   ├── base.css                  # 基础样式
│   ├── fonts.css                 # 字体样式
│   ├── runtime.js                # 运行时逻辑
│   ├── themes/                   # 36种主题
│   │   ├── corporate-clean.css
│   │   ├── minimal-white.css
│   │   ├── swiss-grid.css
│   │   └── ...
│   └── animations/               # 47种动画
│       ├── animations.css
│       ├── fx-runtime.js
│       └── fx/                   # 特效动画
│
├── tools/                        # 工具脚本
│   ├── extract_epub_chapters.py  # EPUB内容提取
│   ├── build_knowledge_graph.py  # 知识图谱构建
│   ├── quality_check.py          # 质量检查
│   ├── search.py                 # 检索工具
│   ├── graph.py                  # 图谱工具
│   └── requirements.txt          # Python依赖
│
├── distillation_output/          # 蒸馏输出
│   └── logic_seed.md             # 逻辑种子（可复用）
│
├── graphify-out/                 # 知识图谱输出
│   ├── graph.html                # 可视化图谱
│   └── graph.json                # 图谱数据
│
└── *.html                        # 生成的PPT文件
    ├── 关键对话_精华内参.html
    └── 不要挑战人性_精华内参.html
```

---

## 🎨 在线演示

### 示例1：《关键对话如何高效能沟通》

- **页数**：40页
- **主题**：corporate-clean
- **核心内容**：
  - 7大技巧：从心开始、注意观察、保证安全、控制想法、陈述观点、了解动机、开始行动
  - 2大原则：百分之百尊重、百分之百坦诚
  - 知识图谱：展示核心概念关系网络

### 示例2：《不要挑战人性》

- **页数**：22页
- **主题**：麦肯锡风格
- **核心内容**：
  - 10大支柱：早期依恋、环境权威、认知偏差、自我实现、情绪机制、关系塑造、身心一体、拖延调节、良知道德、正念觉知
  - 9个颠覆性认知：挑战传统人性观念
  - 落地行动指南：5大主题场景模拟

---

## 🛠️ 技术架构

### 核心技术栈

- **GraphRAG**：基于图谱的检索增强生成
- **Agentic RAG**：智能体驱动的检索协作
- **Knowledge Graph**：概念关系网络构建
- **HTML/CSS/JS**：前端可视化呈现

### 技术亮点

1. **逻辑种子提取**：自动识别书籍核心逻辑结构
2. **3-Agent协作**：分工明确的智能体协作机制
3. **硬门控验证**：确保输出质量的严格检查
4. **模块化设计**：高度可扩展的架构设计

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

- [html-ppt](https://github.com/trae-ide/html-ppt) - HTML PPT框架
- [graphify](https://github.com/trae-ide/graphify) - 知识图谱生成
- [ui-ux-pro-max](https://github.com/trae-ide/ui-ux-pro-max) - UI/UX设计系统

---

## 📧 联系方式

- **GitHub**: [@XCDaHuiGe](https://github.com/XCDaHuiGe)
- **项目主页**: [https://github.com/XCDaHuiGe/book-distillation](https://github.com/XCDaHuiGe/book-distillation)

---

<div align="center">

**如果这个项目对你有帮助，请给一个 ⭐️ Star！**

Made with ❤️ by XCDaHuiGe

</div>
