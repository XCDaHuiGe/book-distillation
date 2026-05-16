# 科技风配色系统

> 从站酷优秀设计作品中学习的科技风配色方案

---

## 配色方案

### 方案1：霓虹赛博朋克（适合科技/游戏/创意）

```css
:root {
  --bg: #0a0a0f;           /* 深黑 */
  --bg-elevated: #12121a;
  --fg: #e5e7eb;
  --fg-muted: #6b7280;
  --accent: #00ffff;       /* 霓虹青 */
  --accent-alt: #ff00ff;   /* 霓虹粉 */
  --neon-blue: #00ffff;
  --neon-pink: #ff00ff;
  --neon-purple: #8b5cf6;
  --glow-cyan: rgba(0, 255, 255, 0.5);
  --glow-pink: rgba(255, 0, 255, 0.5);
}
```

**来源**：站酷 - 跳跃的小鱼《2025-2026作品集》

**适合场景**：科技、游戏、未来主题、创意内容

---

### 方案2：HMI科技风（适合汽车/工业/技术）

```css
:root {
  --bg: #0a0e14;           /* 深黑带蓝 */
  --bg-elevated: #111827;
  --fg: #e5e7eb;
  --fg-muted: #6b7280;
  --accent: #00d4aa;       /* 青色强调 */
  --accent-alt: #3b82f6;   /* 蓝色辅助 */
  --glow: rgba(0, 212, 170, 0.3);
}
```

**来源**：站酷 - CodeWolf《Toyota23概念设计》

**适合场景**：汽车、工业、技术分享、硬件产品

---

### 方案3：数据可视化（适合数据报告/分析）

```css
:root {
  --bg: #0a1628;           /* 深靛蓝 */
  --bg-elevated: #0f1f35;
  --fg: #e5e7eb;
  --fg-muted: #6b7280;
  --data-1: #3b82f6;       /* 蓝色数据 */
  --data-2: #10b981;       /* 绿色数据 */
  --data-3: #f59e0b;       /* 橙色数据 */
  --data-4: #ef4444;       /* 红色数据 */
  --data-5: #8b5cf6;       /* 紫色数据 */
}
```

**来源**：站酷 - 三鱼先生《AI全链路设计》

**适合场景**：数据报告、分析类、统计展示

---

## 霓虹发光效果

### 霓虹边框

```css
.neon-border {
  border: 1px solid var(--neon-blue);
  box-shadow: 
    0 0 5px var(--glow-cyan),
    0 0 10px var(--glow-cyan),
    0 0 20px var(--glow-cyan);
}

.neon-border-pink {
  border: 1px solid var(--neon-pink);
  box-shadow: 
    0 0 5px var(--glow-pink),
    0 0 10px var(--glow-pink),
    0 0 20px var(--glow-pink);
}
```

### 霓虹文字

```css
.neon-text {
  color: var(--neon-blue);
  text-shadow: 
    0 0 5px var(--glow-cyan),
    0 0 10px var(--glow-cyan),
    0 0 20px var(--glow-cyan);
}
```

### 渐变背景

```css
.cyber-gradient {
  background: linear-gradient(
    135deg,
    #0a0a0f 0%,
    #1a0a2e 50%,
    #0a0a0f 100%
  );
}
```

---

## 使用建议

| 内容类型 | 推荐配色 | 理由 |
|:---|:---|:---|
| 科技/AI内容 | 霓虹赛博朋克 | 视觉冲击力强，符合科技感 |
| 汽车/硬件 | HMI科技风 | 专业感强，青色强调醒目 |
| 数据报告 | 数据可视化 | 多色区分不同数据类型 |
| 游戏/创意 | 霓虹赛博朋克 | 发光效果增加趣味性 |
| 商业/企业 | 天道金/墨水经典 | 稳重专业 |

---

## 禁止事项

- ❌ 禁止在浅色背景使用霓虹效果（效果差）
- ❌ 禁止同时使用超过3种霓虹色（视觉混乱）
- ❌ 禁止在正文使用发光效果（可读性差）
