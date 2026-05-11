# Book Distillation 项目规则

## 项目定位
将长文本（书籍、报告、文档）通过 GraphRAG + 3-Agent 蒸馏为 HTML PPT 精华内参。

## 交付物清单

每处理一本书/文档，产出以下文件：

### 最终交付物
| 文件 | 说明 |
|:---|:---|
| `{书名}_精华内参.html` | HTML PPT（可在线预览） |

### 可复用资源
| 文件 | 说明 |
|:---|:---|
| `distillation_output/逻辑种子_{书名}.md` | 逻辑种子（可增量更新复用） |

### 入口页面
| 文件 | 说明 |
|:---|:---|
| `index.html` | 项目首页，列出所有交付物 |

### 当前交付物清单
- 关键对话_精华内参.html
- 不要挑战人性_精华内参.html
- 155规划纲要_精华内参.html

## 更新流程

当有新内容产出时，必须执行以下操作：

### Step 1: 更新 index.html
- 在"精华内参"区域添加新条目卡片
- 按时间倒序排列（最新的排前面）
- 卡片包含：书名、页数、主题风格、一句话描述

### Step 2: 提交到 Git
```bash
cd d:\vibe_coding\zhengliu\book-distillation
git add .
git commit -m "feat: 新增{书名}精华内参"
git push origin main
```

## 代码规范

### HTML PPT 生成规范
- 每页 slide 必须设置 `data-title` 属性（用于目录和概览）
- 每页 slide 必须包含 `deck-footer` + `slide-number`
- 按 S 键开启演讲者模式
- 按 T 键切换主题

### .gitignore 规则
- 不上传 EPUB/DOCX/PDF 源文件
- 不上传 Python 缓存
- 不上传 IDE 配置

## 维护原则
1. 每次有新交付物，必须更新 index.html
2. 每次更新后必须推送到 GitHub
3. index.html 不是 skill 内容，是项目入口页面
4. 产物清理规则：保留最终 HTML + 逻辑种子，删除中间过程文件
