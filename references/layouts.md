# 页面布局库（Layouts）

本文档收录 10 种最常用的页面布局骨架。每种都是一个完整可粘贴的 `<section class="slide ...">...</section>` 代码块，直接替换文案/图片即可使用。

---

## 生成前必读（Pre-flight）

### A. 类名必须来自 template.html

layouts.md 使用的所有类都在 `assets/template.html` 的 `<style>` 块里预定义。

**不要发明新类名**。如果必须自定义，用 `style="..."` inline 写。

### B. 图片比例规范

| 场景 | 推荐比例 | 写法 |
|------|---------|------|
| 左文右图 主图 | 16:10 或 4:3 | `.frame-img.r-16x10` 或 `.frame-img.r-4x3` |
| 图片网格（多图对比） | 统一高度 | `.frame-img.h-22` / `.frame-img.h-26` |
| 全屏主视觉 | 16:9 | `.frame-img.r-16x9` |
| 信息图 / 截图再设计 | 16:9 或 16:10 | `.frame-img.r-16x9` |

### C. 主题节奏规划（必读）

**核心机制**：每页 `<section>` 必须带 `light` / `dark` / `hero light` / `hero dark` 之一。

**节奏硬规则**：
- 禁止连续 3 页以上相同主题
- 8 页以上必须有 ≥1 个 `hero dark` + ≥1 个 `hero light`
- 每 3-4 页插入 1 个 hero（封面/幕封/问题/大引用）

---

## Layout 1: 开场封面（Hero Cover）

```html
<section class="slide hero dark">
  <div class="chrome">
    <div>栏目标签 · 2026.05</div>
    <div>Vol.01</div>
  </div>
  <div class="frame" style="display:grid;gap:3vh;align-content:center;min-height:80vh">
    <div class="kicker" data-anim>私享会 · 作者名</div>
    <h1 class="h-hero" data-anim>书名或核心标题</h1>
    <h2 class="h-sub" data-anim>副标题或一句话概括</h2>
    <p class="lead" style="max-width:60vw" data-anim>
      核心引言或开场白，用于建立全书基调。
    </p>
    <div class="meta-row" data-anim>
      <span>作者名</span><span>·</span><span>身份/标签</span>
    </div>
  </div>
  <div class="foot">
    <div>一场关于主题的分享</div>
    <div>— 2026 —</div>
  </div>
</section>
```

**要点**：
- 用 `hero dark` 让粒子背景在大部分区域透出
- `h-hero` 是最大字号（10vw），作标题主视觉
- 用 `min-height:80vh + align-content:center` 让内容整体垂直居中

---

## Layout 2: 章节幕封（Act Divider）

```html
<section class="slide hero light">
  <div class="chrome">
    <div>第一幕 · 章节名</div>
    <div>Act I · 01 / 25</div>
  </div>
  <div class="frame" style="display:grid;gap:5vh;align-content:center;min-height:80vh">
    <div class="kicker" data-anim>Act I</div>
    <h1 class="h-hero" style="font-size:8.5vw" data-anim>章节标题</h1>
    <p class="lead" style="max-width:55vw" data-anim>
      章节引言，一句话概括本章节核心内容。
    </p>
  </div>
  <div class="foot">
    <div>章节引子</div>
    <div>— · —</div>
  </div>
</section>
```

**要点**：
- 极简，只需要 kicker + 大标题 + 一行引语
- 两个幕的封面可以交替 `hero light` / `hero dark`，制造节奏

---

## Layout 3: 数据大字报（Big Numbers Grid）

```html
<section class="slide light">
  <div class="chrome">
    <div>数据标签 · Data</div>
    <div>Act I · 02 / 25</div>
  </div>
  <div class="frame" style="padding-top:6vh">
    <div class="kicker" data-anim>DATA · 关键数据</div>
    <h2 class="h-xl" data-anim>数据主题标题</h2>
    <p class="lead" style="margin-bottom:4vh" data-anim>数据说明或背景。</p>

    <div class="grid-6" style="margin-top:4vh">
      <div class="stat-card" data-anim>
        <div class="stat-label">指标名称</div>
        <div class="stat-nb">42 <span class="stat-unit">单位</span></div>
        <div class="stat-note">指标说明</div>
      </div>
      <div class="stat-card" data-anim>
        <div class="stat-label">指标名称</div>
        <div class="stat-nb">100K+</div>
        <div class="stat-note">指标说明</div>
      </div>
      <div class="stat-card" data-anim>
        <div class="stat-label">指标名称</div>
        <div class="stat-nb">89%</div>
        <div class="stat-note">指标说明</div>
      </div>
      <div class="stat-card" data-anim>
        <div class="stat-label">指标名称</div>
        <div class="stat-nb">5.2</div>
        <div class="stat-note">指标说明</div>
      </div>
      <div class="stat-card" data-anim>
        <div class="stat-label">指标名称</div>
        <div class="stat-nb">19</div>
        <div class="stat-note">指标说明</div>
      </div>
      <div class="stat-card" data-anim>
        <div class="stat-label">指标名称</div>
        <div class="stat-nb">608+</div>
        <div class="stat-note">指标说明</div>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>数据来源说明</div>
    <div>Page · 数据页</div>
  </div>
</section>
```

**要点**：
- 3×2 网格最稳（`.grid-6`）
- 每个 `stat-card` 结构固定：label → nb（大字数字）→ note
- 数字建议 2-3 位字符，用 K / M 简写

---

## Layout 4: 左文右图（Quote + Image）

```html
<section class="slide light">
  <div class="chrome">
    <div>内容标签 · Content</div>
    <div>03 / 25</div>
  </div>
  <div class="frame grid-2-7-5" style="padding-top:6vh">
    <div style="display:flex;flex-direction:column;justify-content:space-between;gap:3vh">
      <div>
        <div class="kicker" data-anim>CONTEXT · 背景</div>
        <h2 class="h-xl" style="white-space:nowrap" data-anim>
          标题文字
        </h2>
        <p class="lead" style="margin-top:2vh" data-anim>
          正文内容，解释概念或讲述故事。
        </p>
      </div>
      <div class="callout" data-anim>
        "引用文字，用于强调核心观点。"
        <div class="callout-src">— 引用来源</div>
      </div>
    </div>
    <figure class="frame-img r-16x10" data-anim>
      <img src="images/example.jpg" alt="图片说明">
      <figcaption class="img-cap">图片说明</figcaption>
    </figure>
  </div>
  <div class="foot">
    <div>Page 03 · 页面说明</div>
    <div>— · —</div>
  </div>
</section>
```

**要点**：
- 用 `grid-2-7-5`（左 7 份、右 5 份）
- 左列用 flex column + `justify-content:space-between`：标题贴顶，callout 自然贴底
- 图片必须用标准比例类 `.r-16x10` 或 `.r-4x3`

---

## Layout 5: 图片网格（多图对比）

```html
<section class="slide light">
  <div class="chrome">
    <div>图片标签 · Gallery</div>
    <div>Act I · 05 / 27</div>
  </div>
  <div class="frame" style="padding-top:5vh">
    <div class="kicker" data-anim>GALLERY · 图片展示</div>
    <h2 class="h-xl" data-anim>图片主题标题</h2>

    <div class="grid-3" style="margin-top:4vh">
      <figure class="frame-img h-26" data-anim>
        <img src="images/img1.jpg" alt="图片1">
        <figcaption class="img-cap">图片1说明</figcaption>
      </figure>
      <figure class="frame-img h-26" data-anim>
        <img src="images/img2.jpg" alt="图片2">
        <figcaption class="img-cap">图片2说明</figcaption>
      </figure>
      <figure class="frame-img h-26" data-anim>
        <img src="images/img3.jpg" alt="图片3">
        <figcaption class="img-cap">图片3说明</figcaption>
      </figure>
    </div>
  </div>
  <div class="foot">
    <div>图片来源说明</div>
    <div>Page · 图片页</div>
  </div>
</section>
```

**要点**：
- 每个 `frame-img` 必须写死 `height:NNvh`，否则网格会撑破
- 图片会自动 `object-fit:cover + object-position:top`，只裁底部
- 用 `.grid-3`（3×1）或 `.grid-3` 配合多行

---

## Layout 6: 流水线（Pipeline）

```html
<section class="slide light">
  <div class="chrome">
    <div>流程标签 · Workflow</div>
    <div>Act II · 15 / 27</div>
  </div>
  <div class="frame">
    <div class="kicker">PIPELINE · 流程</div>
    <h2 class="h-xl">流程标题</h2>

    <div class="pipeline-section" style="margin-top:4vh">
      <div class="pipeline-label">阶段一 · 准备</div>
      <div class="pipeline">
        <div class="step" data-anim>
          <div class="step-nb">01</div>
          <div>
            <div class="step-title">步骤标题</div>
            <div class="step-desc">步骤描述文字</div>
          </div>
        </div>
        <div class="step" data-anim>
          <div class="step-nb">02</div>
          <div>
            <div class="step-title">步骤标题</div>
            <div class="step-desc">步骤描述文字</div>
          </div>
        </div>
        <div class="step" data-anim>
          <div class="step-nb">03</div>
          <div>
            <div class="step-title">步骤标题</div>
            <div class="step-desc">步骤描述文字</div>
          </div>
        </div>
      </div>
    </div>

    <div class="pipeline-section" style="margin-top:3vh">
      <div class="pipeline-label">阶段二 · 执行</div>
      <div class="pipeline">
        <div class="step" data-anim>
          <div class="step-nb">04</div>
          <div>
            <div class="step-title">步骤标题</div>
            <div class="step-desc">步骤描述文字</div>
          </div>
        </div>
        <div class="step" data-anim>
          <div class="step-nb">05</div>
          <div>
            <div class="step-title">步骤标题</div>
            <div class="step-desc">步骤描述文字</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>流程说明</div>
    <div>Page · 流程页</div>
  </div>
</section>
```

**要点**：
- 用 `.pipeline-section` 分组不同阶段
- 每个 `.step` 结构固定：编号 + 标题 + 描述

---

## Layout 7: 问题页（Question Page）

```html
<section class="slide hero dark">
  <div class="chrome">
    <div>问题标签 · Question</div>
    <div>07 / 25</div>
  </div>
  <div class="frame" style="display:grid;gap:4vh;align-content:center;min-height:80vh">
    <div class="kicker" data-anim>QUESTION · 核心问题</div>
    <h1 class="h-hero" style="font-size:7vw" data-anim>
      核心问题是什么？
    </h1>
    <p class="lead" style="max-width:60vw" data-anim>
      问题的背景说明或引导语，用于引出后续内容。
    </p>
  </div>
  <div class="foot">
    <div>问题引出</div>
    <div>— · —</div>
  </div>
</section>
```

**要点**：
- 用 `hero dark` 制造视觉冲击
- 问题用问号结尾，制造悬念

---

## Layout 8: 大引用页（Big Quote）

```html
<section class="slide dark">
  <div class="chrome">
    <div>引用标签 · Quote</div>
    <div>12 / 25</div>
  </div>
  <div class="frame" style="display:grid;gap:4vh;align-content:center;min-height:80vh">
    <div class="kicker" data-anim>QUOTE · 金句</div>
    <blockquote class="q-big" data-anim>
      "这是一句核心引用，用于强调全书最重要的观点或洞见。引用应该简洁有力，能够独立成句。"
    </blockquote>
    <div class="cite" data-anim>— 引用来源，出处</div>
  </div>
  <div class="foot">
    <div>金句来源</div>
    <div>— · —</div>
  </div>
</section>
```

**要点**：
- 用 `dark` 主题，金句仪式感靠暗底
- 引用要简洁有力，不超过 3 行

---

## Layout 9: 前后对比（Before / After）

```html
<section class="slide light">
  <div class="chrome">
    <div>对比标签 · Compare</div>
    <div>18 / 25</div>
  </div>
  <div class="frame" style="padding-top:6vh">
    <div class="kicker" data-anim>COMPARE · 对比</div>
    <h2 class="h-xl" data-anim>对比标题</h2>

    <div class="before-after" style="margin-top:4vh">
      <div class="ba-col wrong" data-anim>
        <div class="ba-label">错误做法</div>
        <ul style="margin:0;padding-left:1.2em;font-size:14px;line-height:1.8">
          <li>错误做法一</li>
          <li>错误做法二</li>
          <li>错误做法三</li>
        </ul>
      </div>
      <div class="ba-col right" data-anim>
        <div class="ba-label">正确做法</div>
        <ul style="margin:0;padding-left:1.2em;font-size:14px;line-height:1.8">
          <li>正确做法一</li>
          <li>正确做法二</li>
          <li>正确做法三</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>对比说明</div>
    <div>Page · 对比页</div>
  </div>
</section>
```

**要点**：
- 用 `.before-after` 双列布局
- 左列用 `.wrong`（红色背景），右列用 `.right`（绿色背景）

---

## Layout 10: 图文混排（Mixed Layout）

```html
<section class="slide light">
  <div class="chrome">
    <div>综合标签 · Mixed</div>
    <div>20 / 25</div>
  </div>
  <div class="frame" style="padding-top:5vh">
    <div class="kicker" data-anim>MIXED · 综合内容</div>
    <h2 class="h-xl" data-anim>综合标题</h2>
    
    <div class="grid-2-6-6" style="margin-top:4vh;gap:3vw">
      <div>
        <p class="lead" style="margin-bottom:2vh" data-anim>
          左侧正文内容，可以是概念解释、背景说明或案例分析。
        </p>
        <div class="callout" data-anim>
          "引用或强调文字"
          <div class="callout-src">— 来源</div>
        </div>
      </div>
      <div>
        <figure class="frame-img r-4x3" style="margin-bottom:2vh" data-anim>
          <img src="images/example1.jpg" alt="图片1">
          <figcaption class="img-cap">图片1说明</figcaption>
        </figure>
        <figure class="frame-img r-4x3" data-anim>
          <img src="images/example2.jpg" alt="图片2">
          <figcaption class="img-cap">图片2说明</figcaption>
        </figure>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>综合内容说明</div>
    <div>Page · 混排页</div>
  </div>
</section>
```

**要点**：
- 用 `.grid-2-6-6` 左右均分布局
- 左侧放正文 + 引用，右侧放图片

---

## 主题节奏模板（8 页示例）

| 页 | 主题 | 布局 | 备注 |
|---|---|---|---|
| 1 | `hero dark` | Layout 1 封面 | 开场 |
| 2 | `light` | Layout 3 大字报 | 数据抛出 |
| 3 | `dark` | Layout 4 左文右图 | 对比/故事 |
| 4 | `light` | Layout 6 Pipeline | 流程 |
| 5 | `hero light` | Layout 2 幕封 | 呼吸 |
| 6 | `dark` | Layout 8 大引用 | 金句 |
| 7 | `hero dark` | Layout 7 问题页 | 悬念收束 |
| 8 | `light` | Layout 10 混排 | 收尾 |

**先画这张表对齐，再动手写 slide**。
