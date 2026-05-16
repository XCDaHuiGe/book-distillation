# 入场动画效果库

> 分层入场动画，模拟演讲者的"娓娓道来"

---

## 动画原则

1. **分层延迟**：标签 → 标题 → 正文 → 辅助信息
2. **延迟时间**：每层间隔 0.15-0.25s
3. **动画类型**：淡入上移（fadeInUp）为主，缩放（zoomIn）为辅
4. **尊重用户偏好**：支持 `prefers-reduced-motion`

---

## 动画类定义

### 基础入场动画

```css
/* 淡入上移 */
.anim-fade-up {
  animation: fadeUp 0.6s ease-out forwards;
  opacity: 0;
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 缩放入场 */
.anim-zoom {
  animation: zoomIn 0.5s ease-out forwards;
  opacity: 0;
}

@keyframes zoomIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
```

---

## 分层延迟系统

```css
/* anim-1 到 anim-6 分层入场 */
.anim-1 { animation-delay: 0s; }
.anim-2 { animation-delay: 0.15s; }
.anim-3 { animation-delay: 0.3s; }
.anim-4 { animation-delay: 0.45s; }
.anim-5 { animation-delay: 0.6s; }
.anim-6 { animation-delay: 0.75s; }
```

### 使用示例

```html
<section class="slide dark">
  <div class="frame">
    <div class="kicker anim-fade-up anim-1">CHAPTER 01</div>
    <h1 class="title anim-fade-up anim-2">叙事内核</h1>
    <p class="lead anim-fade-up anim-3">驱动全书的核心冲突</p>
    <div class="content anim-fade-up anim-4">...</div>
  </div>
</section>
```

---

## 特殊动画效果

### 金句页入场

```css
/* 金句页：先出文字，再出作者 */
.slide-quote .quote-text {
  animation: fadeUp 0.8s ease-out forwards;
  animation-delay: 0.2s;
}

.slide-quote .quote-author {
  animation: fadeUp 0.6s ease-out forwards;
  animation-delay: 0.8s;
}
```

### 数据卡片入场

```css
/* 数据卡片：依次入场 */
.stat-card:nth-child(1) { animation-delay: 0.1s; }
.stat-card:nth-child(2) { animation-delay: 0.2s; }
.stat-card:nth-child(3) { animation-delay: 0.3s; }
```

---

## 无障碍处理

```css
/* 尊重用户偏好：减少动画 */
@media (prefers-reduced-motion: reduce) {
  .anim-fade-up,
  .anim-zoom {
    animation: none;
    opacity: 1;
    transform: none;
  }
}
```

---

## 待学习动画效果

请提供动画效果案例链接：

- [ ] ____________
- [ ] ____________
