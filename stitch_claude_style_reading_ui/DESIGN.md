---
name: Obsidian Orbit
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#e3bfb3'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#aa897f'
  outline-variant: '#5b4138'
  surface-tint: '#ffb59c'
  primary: '#ffb59c'
  on-primary: '#5c1900'
  primary-container: '#ff5f1f'
  on-primary-container: '#561700'
  inverse-primary: '#ab3600'
  secondary: '#c9c6c5'
  on-secondary: '#313030'
  secondary-container: '#4a4949'
  on-secondary-container: '#bab8b7'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#959393'
  on-tertiary-container: '#2c2c2c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcf'
  primary-fixed-dim: '#ffb59c'
  on-primary-fixed: '#390c00'
  on-primary-fixed-variant: '#832700'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c9c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-lg:
    fontFamily: Anton
    fontSize: 84px
    fontWeight: '400'
    lineHeight: 90%
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Anton
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 110%
    letterSpacing: 0.01em
  headline-lg-mobile:
    fontFamily: Anton
    fontSize: 36px
    fontWeight: '400'
    lineHeight: 110%
  subheader:
    fontFamily: Space Mono
    fontSize: 18px
    fontWeight: '700'
    lineHeight: 140%
  body-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 160%
  label-sm:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 100%
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 1.5rem
  margin-mobile: 1rem
  margin-desktop: 4rem
  grid-size: 32px
---

## Brand & Style

This design system is built for a high-performance, tech-noir environment where precision meets raw creative energy. It targets a "Prosumer" and developer audience—users who value speed, technical depth, and a distinctive aesthetic edge. 

The visual style is a hybrid of **Cyberpunk Brutalism** and **High-End Glassmorphism**. It rejects the soft, rounded friendliness of modern SaaS in favor of sharp technical edges, high-contrast accents, and "system-under-the-hood" transparency. The emotional response is one of authority and "hacker-elite" sophistication. Key characteristics include:
- **Technical Rigor:** Monospace fonts and grid-aligned elements suggest a code-first mindset.
- **Glassmorphism:** Deep layers of blur simulate advanced heads-up displays (HUDs).
- **High-Energy Accents:** An aggressive orange provides a visual pulse against an obsidian void.

## Colors

The palette is anchored in a monochromatic "Obsidian" base to ensure maximum contrast for functional elements.
- **Backgrounds:** Use `#0A0A0A` for the primary canvas and `#1A1A1A` for elevated surfaces or card containers.
- **Primary Accent:** `#FF5F1F` (Atomic Orange) is reserved for primary actions, critical alerts, and structural framing.
- **Iridescence:** A subtle, multi-color gradient is used sparingly as a "high-tech" highlight on specific interactive states or decorative light-streaks, mimicking lens flares or prismatic glass edges.
- **Overlays:** Dark grid lines should be rendered in `#FFFFFF` at 5% opacity to maintain a subtle "blue-print" feel without distracting from content.

## Typography

The typography system creates a "Terminal-Display" hierarchy. 
- **Headlines:** Utilize **Anton** for a heavy, impactful vertical presence. These should be treated as architectural elements, often using tight leading to feel like a solid block of text.
- **Body & Data:** **JetBrains Mono** provides the technical "code" aesthetic while maintaining high legibility for long-form content. 
- **Metadata & Labels:** **Space Mono** is used for UI labels, tags, and navigation to reinforce the tech-studio vibe.
- **Styling Note:** Headers often incorporate a "glitch" or "scanline" text shadow in advanced implementations, while body text should remain clean and crisp for accessibility.

## Layout & Spacing

This system utilizes a **Fixed-Grid hybrid model**. 
- **The Global Grid:** A background grid of 32px squares serves as the structural guide. Elements should snap to these lines to maintain a "schematic" feel.
- **Column System:** A 12-column grid for desktop with 24px (1.5rem) gutters.
- **Spacing Logic:** All margins and paddings must be multiples of 4px. Use generous outer margins on desktop (64px+) to create a "letterboxed" cinematic focus on the content.
- **Mobile Adaption:** On mobile, the 12-column grid collapses to a 4-column layout, and the background grid lines should be reduced in opacity or hidden to avoid visual clutter on smaller screens.

## Elevation & Depth

Depth is not communicated through soft shadows, but through **Tonal Stacking** and **Glassmorphism**.
- **Surface 0:** The Obsidian base (#0A0A0A) with the grid overlay.
- **Surface 1 (Glass):** Semi-transparent containers with a background blur (backdrop-filter: blur(20px)) and a 1px border in either `#FFFFFF10` or the primary Orange.
- **Surface 2 (Focus):** Fully opaque `#1A1A1A` surfaces for high-interaction areas.
- **Glow Effects:** Instead of drop shadows, use "Outer Glows" for active states. Use the primary orange color with a 10px-20px spread at low opacity (20-30%) to simulate a neon or LED emission.

## Shapes

The shape language is strictly **Sharp (0px radius)**. 
- All buttons, input fields, and card containers must have 90-degree corners to emphasize the industrial, tech-noir aesthetic.
- **Exceptions:** Very small icons or decorative tags may use a 45-degree "clipped corner" (chamfer) to add to the futuristic military/tech vibe, but standard rounding is prohibited.

## Components

### Buttons
- **Primary:** Solid orange (#FF5F1F) with black text. Sharp corners. No border. On hover, add a thin iridescent top-border.
- **Secondary:** Transparent background, 1px orange border, orange text.
- **Ghost:** Monospace text with a leading `//` or `> ` prefix (e.g., `> EXECUTE`).

### Inputs & Text Fields
- Sharp rectangular boxes with a dark charcoal fill and a 1px border (#333). 
- On focus, the border turns primary orange and a subtle orange glow is applied.
- Labels are always positioned above the input in `label-sm` monospace uppercase.

### Cards & Containers
- High-blur glassmorphism is the default state for cards. 
- Use a 1px orange border for the "Active" card and a subtle grey border for inactive ones.
- Include "Tech-bits" in the corners—small 4px x 4px squares or coordinate strings (e.g., `REF_001`) to enhance the UI overlay feel.

### Lists & Navigation
- Navigation items should use a vertical bar indicator on the left when active.
- List items should be separated by thin 1px horizontal lines at 10% opacity, maintaining the "terminal" look.

### Tags / Chips
- Small, sharp-edged blocks. Use the primary orange for high-priority tags and `#1A1A1A` for metadata.