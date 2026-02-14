# Bull Run Rocket - Design Specification Document
## ETHDenver 2026 Game Design

**Version:** 1.0  
**Date:** February 14, 2026  
**Target:** Single-file HTML5 game (iOS Safari + Android Chrome)  
**Playtime:** 2-5 minutes per session  
**Baseline Resolution:** 375×812 (iPhone X portrait, mobile-first)

---

## 1. Visual Theme & Art Direction

### 1.1 Overall Aesthetic

**Style Reference:** Arcade neon meets cosmic crypto adventure. The game blends 80s/90s arcade nostalgia with modern DeFi aesthetics—think "Space Invaders" meets "Flappy Bird" with a crypto-native twist.

**Key Visual Anchors:**
- **Character:** Koda (bear with rocket backpack) - playful, determined expression, crypto-casual aesthetic
- **Obstacles:** Candlestick charts rendered as physical obstacles—red (falling/bearish) and green (rising/bullish)
- **Environment:** Deep space with cosmic nebula effects, distant stars, subtle parallax depth
- **Effects:** Neon glows, particle trails, CRT scanline subtlety for retro feel

**Art Direction Principles:**
1. **High contrast for readability** - UI elements must pop against dark cosmic backgrounds
2. **Neon accent hierarchy** - Bankr purple and orange guide the eye to important elements
3. **Clean silhouettes** - Obstacles and Koda must be instantly recognizable at small sizes
4. **Motion-first design** - Static screenshots should feel alive; animation defines the experience

### 1.2 Color Palette

#### Primary Colors
| Color | Hex | Usage |
|-------|-----|-------|
| **Cosmic Black** | `#0a0a0f` | Main background, void space |
| **Deep Space** | `#1a1a2e` | Secondary background layers |
| **Nebula Purple** | `#2d2b55` | Atmospheric depth, gradient endpoints |

#### Secondary Colors
| Color | Hex | Usage |
|-------|-----|-------|
| **Star White** | `#ffffff` | Stars, score text, highlights |
| **Candle Red** | `#e74c3c` | Falling bear market candles |
| **Candle Green** | `#2ecc71` | Rising bull market candles |
| **Rocket Flame** | `#ff6b35` | Thruster particles, action accents |

#### Accent Colors (Bankr Brand Integration)
| Color | Hex | RGBA | Usage |
|-------|-----|------|-------|
| **Bankr Purple** | `#9d4edd` | `rgba(157, 78, 221, 1)` | Brand accents, victory effects, power-ups |
| **Bankr Orange** | `#ff9e00` | `rgba(255, 158, 0, 1)` | CTAs, important highlights, heat |
| **Bankr Glow** | `#c77dff` | `rgba(199, 125, 255, 0.6)` | Neon glows, hover states |

#### UI Semantic Colors
| Color | Hex | Usage |
|-------|-----|-------|
| **Success Green** | `#00d26a` | Victory states, high scores |
| **Alert Yellow** | `#ffd93d` | Warnings, medium difficulty |
| **Danger Red** | `#ff4757` | Game over, collisions |
| **Info Blue** | `#5f27cd` | Instructions, neutral UI |

#### Gradient Definitions
```css
/* Space Background Gradient */
background: linear-gradient(180deg, #0a0a0f 0%, #1a1a2e 50%, #2d2b55 100%);

/* Victory Glow */
background: radial-gradient(circle, rgba(157, 78, 221, 0.8) 0%, transparent 70%);

/* Rocket Trail */
background: linear-gradient(180deg, #ff9e00 0%, #ff6b35 50%, transparent 100%);

/* Bankr Brand Gradient */
background: linear-gradient(135deg, #9d4edd 0%, #ff9e00 100%);
```

### 1.3 Mood & Atmosphere

**Emotional Arc:**
1. **Anticipation** (Start screen) - Dark, mysterious, pulsing elements
2. **Tension** (Gameplay) - Rhythmic dodging, increasing pressure
3. **Triumph** (Victory) - Explosion of color, celebration
4. **Determination** (Game Over) - Quick reset, "one more try" energy

**Atmospheric Effects:**
- **Parallax Stars:** 3 layers moving at different speeds (0.2x, 0.5x, 1.0x player speed)
- **Nebula Drift:** Subtle purple/blue haze shifting slowly (20s cycle)
- **Scanline Overlay:** 5% opacity horizontal lines for retro feel
- **Vignette:** Darkened edges focusing attention to center

**Audio-Visual Sync (for reference):**
- Tap → Rocket thrust sound + particle burst
- Score milestone → Chime + subtle screen flash
- Collision → Impact sound + screen shake
- Victory → Fanfare + particle explosion

---

## 2. Game UI/UX Layout

### 2.1 Screen Composition (375×812 Baseline)

**Safe Zones:**
- **Top Safe Zone:** 44px (status bar) - Keep UI above this
- **Bottom Safe Zone:** 34px (home indicator) - Keep tap area above this
- **Playable Area:** Full screen minus safe zones

**Layout Grid:**
```
┌─────────────────────────┐  ← 0px (top)
│  [HUD SCORE]      [BEST]│  ← 60px margin-top
│                         │
│    ┌─────────────┐      │
│    │             │      │  ← Game viewport
│    │   GAMEPLAY  │      │     (centered)
│    │   AREA      │      │
│    │             │      │
│    └─────────────┘      │
│                         │
│[BRANDING BAR]           │  ← 60px from bottom
│                         │
└─────────────────────────┘  ← 812px (bottom)
```

**Aspect Ratio Handling:**
- **Base:** 375×812 (iPhone X ratio 9:19.5)
- **Scale Up:** Center game, maintain aspect ratio, fill with background
- **Scale Down:** Shrink uniformly, maintain touch target sizes (min 44×44px)

### 2.2 HUD Elements

#### Score Display (Top Center)
```
Position: center top, margin-top: 60px
Font: "Press Start 2P", 48px, #ffffff
Text-shadow: 0 0 20px rgba(157, 78, 221, 0.8)
Animation: Pulse on score increase (scale 1.0 → 1.2 → 1.0, 200ms)
```

#### High Score (Top Right)
```
Position: right, margin-top: 60px, margin-right: 20px
Font: "Press Start 2P", 16px, #9d4edd
Label: "BEST" above number
Number: 24px, #ffffff with purple glow
```

#### Progress Indicator (Score 90+)
```
Position: Top center, below score
Style: Filled bar + "0xKODA INCOMING!" text
Bar: Width 200px, height 6px, rounded
Fill: Gradient from #ff9e00 to #9d4edd
Pulsing animation when score >= 95
```

### 2.3 Start Screen Design

**Layout:**
```
┌─────────────────────────┐
│                         │
│      [LOGO AREA]        │  ← 150px from top
│      KODA BEAR ICON     │
│      "BULL RUN"         │
│      "ROCKET"           │
│                         │
│    [INSTRUCTIONS]       │
│    Tap to fly up        │
│    Avoid candles        │
│    Score 100 to win     │
│                         │
│    [START BUTTON]       │
│    ┌─────────────┐      │
│    │  🚀 LAUNCH  │      │  ← Bankr orange glow
│    └─────────────┘      │
│                         │
│  [ANIMATED PREVIEW]     │  ← Mini gameplay demo
│  Koda floating with     │
│  candles passing by     │
│                         │
│[BRANDING BAR]           │
└─────────────────────────┘
```

**Start Button Styling:**
```css
.start-button {
  width: 200px;
  height: 60px;
  background: linear-gradient(135deg, #ff9e00 0%, #ff6b35 100%);
  border: 3px solid #ffffff;
  border-radius: 30px;
  font-family: "Press Start 2P", monospace;
  font-size: 16px;
  color: #ffffff;
  text-transform: uppercase;
  box-shadow: 0 0 30px rgba(255, 158, 0, 0.6);
  animation: pulse-glow 2s infinite;
}

@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 0 30px rgba(255, 158, 0, 0.6); }
  50% { box-shadow: 0 0 50px rgba(255, 158, 0, 0.9); }
}
```

**Title Typography:**
- "BULL RUN" - Press Start 2P, 36px, #ffffff, purple glow
- "ROCKET" - Press Start 2P, 36px, #ff9e00, orange glow
- Bear emoji 🐻 between lines, 48px, bobbing animation

### 2.4 Victory Screen (Score 100+)

**Trigger:** Score reaches 100

**Layout:**
```
┌─────────────────────────┐
│  ★ ★ ★ ★ ★ ★ ★ ★ ★ ★   │  ← Confetti falling
│                         │
│      🎉 VICTORY 🎉      │
│                         │
│    ┌─────────────┐      │
│    │             │      │
│    │  FINAL      │      │
│    │  SCORE: 100 │      │
│    │             │      │
│    └─────────────┘      │
│                         │
│    YOUR CODE:           │
│  ┌─────────────────┐    │
│  │   0xKODA        │    │  ← 72px font, marquee
│  └─────────────────┘    │
│                         │
│  [Screenshot to save]   │
│                         │
│  [PLAY AGAIN] [SHARE]   │
│                         │
│[BRANDING BAR]           │
└─────────────────────────┘
```

**0xKODA Code Display:**
```css
.victory-code {
  font-family: "Press Start 2P", monospace;
  font-size: 48px;
  color: #9d4edd;
  background: rgba(0, 0, 0, 0.8);
  border: 4px solid #ff9e00;
  border-radius: 12px;
  padding: 20px 40px;
  text-shadow: 0 0 20px rgba(157, 78, 221, 1);
  box-shadow: 0 0 40px rgba(255, 158, 0, 0.5);
  animation: code-pulse 1.5s ease-in-out infinite;
}

@keyframes code-pulse {
  0%, 100% { 
    transform: scale(1); 
    box-shadow: 0 0 40px rgba(255, 158, 0, 0.5);
  }
  50% { 
    transform: scale(1.05); 
    box-shadow: 0 0 60px rgba(157, 78, 221, 0.8);
  }
}
```

**Victory Effects:**
- Background: Radial burst of purple/orange particles
- Confetti: 50 particles falling, Bankr colors
- Koda: Victory dance animation (3 loops)
- Text: "YOU'RE BULLISH!" appears below code

### 2.5 Game Over Screen

**Layout:**
```
┌─────────────────────────┐
│                         │
│      💥 CRASH 💥        │
│                         │
│    FINAL SCORE: 42      │
│    BEST: 67               │
│                         │
│  [NEW HIGH SCORE!]      │  ← Only if beaten
│                         │
│  [EXPLOSION ANIMATION]  │
│      at crash point     │
│                         │
│  [TRY AGAIN]            │
│  ┌─────────────┐        │
│  │   RETRY   │        │
│  └─────────────┘        │
│                         │
│  Hint: Tap rhythmically │
│                         │
│[BRANDING BAR]           │
└─────────────────────────┘
```

**Game Over Button:**
```css
.retry-button {
  width: 180px;
  height: 50px;
  background: #e74c3c;
  border: 3px solid #ffffff;
  border-radius: 25px;
  font-family: "Press Start 2P", monospace;
  font-size: 14px;
  color: #ffffff;
  animation: shake 0.5s ease-in-out;
}
```

### 2.6 Branding Placement

**Branding Bar (Persistent):**
```
Position: Bottom center, 20px from bottom
Background: Transparent (blends with game)
Text: "Built by Koda 🐻 | Powered by Bankr"
Font: "Press Start 2P", 12px, #ffffff
Koda mention: #9d4edd
Bankr mention: #ff9e00
Divider: | in #666666
```

**Bankr Logo Integration:**
- Small Bankr "B" icon (24×24px) at start screen only
- Color: #9d4edd with #ff9e00 accent
- Position: Above start button, subtle

**Credit Text Styling:**
```css
.branding-bar {
  font-family: "Press Start 2P", monospace;
  font-size: 10px;
  color: rgba(255, 255, 255, 0.7);
  text-align: center;
  letter-spacing: 1px;
}

.branding-bar .koda {
  color: #9d4edd;
}

.branding-bar .bankr {
  color: #ff9e00;
}
```

---

## 3. Animation & Motion Specs

### 3.1 Koda Flight Animation

**Base State (Idle/Floating):**
```
Animation: gentle-bob
Duration: 2000ms
Easing: ease-in-out
Loop: infinite
Transform: translateY(0) → translateY(-8px) → translateY(0)
Rotation: -2deg → 2deg → -2deg (subtle sway)
```

**Thrust State (On Tap):**
```
Trigger: tap/click event
Duration: 300ms
Sequence:
  0ms:   scale(1) → scale(0.95) (anticipation)
  50ms:  scale(1.1) (thrust burst)
  100ms: scale(1.05) (sustain)
  300ms: scale(1.0) (return)

Rocket Flame:
  - Scale Y: 1.0 → 1.5 → 1.0
  - Opacity: 0.8 → 1.0 → 0.6
  - Color shift: #ff9e00 → #ff6b35 → #ff4757
```

**Gravity Fall:**
```
Physics-based fall with visual feedback
Rotation: 0deg → 15deg (nose down as falling)
Duration: Based on fall speed
Easing: Linear (constant acceleration look)

Particle Trail:
  - Emit every 100ms while falling
  - 5 particles per emission
  - Fade out over 500ms
  - Size: 4px → 0px
  - Color: rgba(255, 158, 0, 0.6)
```

**Bank Angle (Horizontal Movement):**
```
Upward thrust: Rotate -20deg (nose up)
Falling: Rotate +20deg (nose down)
Neutral: Rotate 0deg
Transition: 150ms ease-out
```

### 3.2 Candle Movement

**Red Candles (Falling - Bear Market):**
```
Spawn: Top of screen, random X position
Velocity: 2-4 pixels per frame (increasing with difficulty)
Rotation: 0deg → ±5deg (tumbling effect)
Easing: Linear fall with slight acceleration

Visual Effect:
  - Red glow: box-shadow 0 0 15px rgba(231, 76, 60, 0.5)
  - Wick flicker: opacity 0.8 → 1.0 every 200ms
  
Spawn Rate:
  - Easy (0-30 score): Every 2 seconds
  - Medium (31-60): Every 1.5 seconds
  - Hard (61-99): Every 1 second
  - Extreme (100+): Every 0.8 seconds
```

**Green Candles (Rising - Bull Market):**
```
Spawn: Bottom of screen, random X position
Velocity: 2-4 pixels per frame (mirrors red)
Rotation: 0deg → ±5deg (tumbling effect)
Easing: Linear rise

Visual Effect:
  - Green glow: box-shadow 0 0 15px rgba(46, 204, 113, 0.5)
  - Wick flicker: opacity 0.8 → 1.0 every 200ms
  
Spawn Pattern:
  - Alternates with red candles
  - Minimum gap: 100px between obstacles
  - Gap size decreases with difficulty (200px → 120px)
```

**Candle Spawn Animation:**
```
Entry: scale(0) → scale(1.2) → scale(1.0)
Duration: 300ms
Easing: ease-out-back
```

### 3.3 Particle Effects

**Rocket Trail:**
```
Emission: Continuous while thrusting
Rate: 10 particles per 100ms
Particle properties:
  - Size: 8px → 2px over 600ms
  - Color: #ff9e00 → #ff6b35 → transparent
  - Spread: Random ±10px from center
  - Drift: -2px per frame (downward)
  - Opacity: 1.0 → 0.0

Visual:
  - Circular particles with blur(2px)
  - Overlap creates flame effect
```

**Collision Explosion:**
```
Trigger: Koda hits obstacle
Particle count: 30
Spread: 360 degrees
Duration: 800ms

Particle types:
  1. Spark (70%): 4px, #ff9e00, fast outward
  2. Debris (20%): 6px, #e74c3c, slow tumbling
  3. Smoke (10%): 12px, rgba(100,100,100,0.5), slow fade

Animation:
  - 0ms: All at center point
  - 200ms: Explosion peak, scale 1.5
  - 800ms: Fade to transparent
  
Screen Shake:
  - X offset: random -5px to +5px
  - Y offset: random -5px to +5px
  - Duration: 300ms
  - Easing: ease-out
```

**Score Milestone Burst:**
```
Trigger: Every 10 points (10, 20, 30...)
Particle count: 20
Color: Alternating #9d4edd and #ff9e00
Shape: Star sparkles
Duration: 1000ms
Text popup: "+10!" floating upward
```

**Victory Particle Explosion:**
```
Trigger: Score reaches 100
Particle count: 100
Duration: 3000ms (looping)

Types:
  - Confetti (60%): Rectangles, Bankr colors, tumbling
  - Sparks (30%): Circular, purple/orange, outward burst
  - Stars (10%): 5-point star shape, gold, slow fall

Confetti properties:
  - Size: 8×4px rectangles
  - Colors: #9d4edd, #ff9e00, #ffffff, #2ecc71
  - Rotation: Continuous 360° tumble
  - Fall speed: 2-4px per frame
```

**Power-up Glow (if implemented):**
```
Asset: powerup-glow.png
Animation: rotate 360° over 3000ms
Pulse: scale 1.0 → 1.2 → 1.0, 1000ms
Glow: box-shadow 0 0 30px #9d4edd
```

### 3.4 Screen Transitions

**Start → Game:**
```
Duration: 600ms
Sequence:
  0ms:   UI elements fade out (opacity 1→0)
  200ms: Title scales up 1.0→1.5 and fades
  400ms: Game area fades in
  600ms: HUD slides down from top
Easing: ease-in-out
```

**Game → Game Over:**
```
Duration: 800ms
Sequence:
  0ms:   Slow motion effect (game speed 0.3x for 500ms)
  100ms: Explosion at collision point
  300ms: Screen shake
  500ms: Game over UI slides up from bottom
  800ms: Final score counts up (animated number)
```

**Game → Victory:**
```
Duration: 1200ms
Sequence:
  0ms:   Time freeze, Koda freeze-frames
  200ms: Purple radial burst from center
  400ms: Victory text drops in with bounce
  600ms: 0xKODA code types out (character by character)
  800ms: Confetti begins falling
  1000ms: Buttons slide up
  1200ms: Continuous celebration loop
Easing: ease-out-back for UI elements
```

**Game Over/ Victory → Start (Retry):**
```
Duration: 400ms
Sequence:
  0ms:   Current screen fades
  200ms: Quick flash to black (50ms)
  250ms: Start screen fades in
  400ms: All UI elements present
```

### 3.5 Collision Feedback

**Visual Feedback:**
```
Flash: Screen flashes white at 30% opacity for 100ms
Shake: Viewport shakes ±8px for 200ms
Freeze: Game pauses for 100ms (impact moment)
Sound: Impact sound (if audio enabled)
```

**Obstacle Flash:**
```
Collision candle flashes brighter
box-shadow increases to 0 0 30px
Duration: 200ms
```

---

## 4. Typography & Text Styling

### 4.1 Font Choices

**Primary Font: Press Start 2P**
```html
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
```
- Usage: All UI text, scores, buttons, branding
- Character: Retro pixel font, arcade aesthetic
- Fallback: "Courier New", monospace

**Icon Font: System Emoji**
- Usage: Decorative icons (🐻, 🚀, 💥, 🎉)
- Fallback: Native emoji rendering

### 4.2 Typography Hierarchy

| Element | Font | Size | Weight | Color | Effects |
|---------|------|------|--------|-------|---------|
| **Title (BULL RUN)** | Press Start 2P | 36px | 400 | #ffffff | Purple glow |
| **Title (ROCKET)** | Press Start 2P | 36px | 400 | #ff9e00 | Orange glow |
| **Score (Current)** | Press Start 2P | 48px | 400 | #ffffff | Glow pulse |
| **Score (Best)** | Press Start 2P | 24px | 400 | #9d4edd | Subtle glow |
| **0xKODA Code** | Press Start 2P | 48px | 400 | #9d4edd | Heavy glow, border |
| **Button Text** | Press Start 2P | 14-16px | 400 | #ffffff | None |
| **Instructions** | Press Start 2P | 12px | 400 | rgba(255,255,255,0.8) | None |
| **Branding** | Press Start 2P | 10px | 400 | rgba(255,255,255,0.7) | Brand colors |
| **HUD Labels** | Press Start 2P | 10px | 400 | #9d4edd | Uppercase |

### 4.3 Text Effects

**Glow Effects:**
```css
/* Standard Purple Glow */
.glow-purple {
  text-shadow: 
    0 0 10px rgba(157, 78, 221, 0.8),
    0 0 20px rgba(157, 78, 221, 0.6),
    0 0 30px rgba(157, 78, 221, 0.4);
}

/* Orange Glow */
.glow-orange {
  text-shadow: 
    0 0 10px rgba(255, 158, 0, 0.8),
    0 0 20px rgba(255, 158, 0, 0.6);
}

/* White Glow (for scores) */
.glow-white {
  text-shadow: 
    0 0 10px rgba(255, 255, 255, 0.8),
    0 0 20px rgba(157, 78, 221, 0.5);
}
```

**Outline for Readability:**
```css
/* Text stroke for visibility on busy backgrounds */
.text-outline {
  -webkit-text-stroke: 2px #0a0a0f;
  text-shadow: 
    3px 3px 0 #0a0a0f,
    -1px -1px 0 #0a0a0f;
}
```

### 4.4 Readability on Cosmic Background

**Background Contrast Strategy:**
1. **Text Container Backing:** Semi-transparent dark boxes behind text
   ```css
   .text-container {
     background: rgba(10, 10, 15, 0.7);
     backdrop-filter: blur(4px);
     border-radius: 8px;
     padding: 12px 20px;
   }
   ```

2. **Minimum Contrast Ratios:**
   - White text on dark background: 15:1 (exceeds WCAG AAA)
   - Colored text always has glow/shadow backup

3. **Safe Text Zones:**
   - Score: Top center, minimal background clutter
   - Messages: Center screen, temporary overlay
   - Branding: Bottom, static area

**Mobile Readability:**
- Minimum font size: 10px (Press Start 2P is readable at this size)
- Line height: 1.5x for multi-line text
- Letter spacing: 1px for small caps text

---

## 5. Technical Constraints

### 5.1 Single HTML File Output

**File Structure:**
```html
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="Google Fonts" rel="stylesheet">
  <style>
    /* All CSS inline */
    /* Base64 encoded assets as data URIs */
  </style>
</head>
<body>
  <canvas id="game"></canvas>
  <div id="ui">/* UI overlays */</div>
  <script>
    /* All game logic inline */
    /* Base64 asset strings */
  </script>
</body>
</html>
```

**Asset Encoding:**
```javascript
// Assets converted to base64
const ASSETS = {
  koda: 'data:image/png;base64,iVBORw0KGgo...',
  redCandle: 'data:image/png;base64,iVBORw0KGgo...',
  greenCandle: 'data:image/png;base64,iVBORw0KGgo...',
  background: 'data:image/png;base64,iVBORw0KGgo...',
  powerup: 'data:image/png;base64,iVBORw0KGgo...'
};
```

**Size Budget:**
- Target: < 2MB total file size
- Canvas-based rendering (no external image loads)
- CSS animations for UI (GPU accelerated)

### 5.2 Mobile Optimization

**Touch Controls:**
```javascript
// Primary input
canvas.addEventListener('touchstart', handleTap, {passive: true});
canvas.addEventListener('click', handleTap);

// Prevent zoom/scroll
document.addEventListener('touchmove', e => e.preventDefault(), {passive: false});
```

**Responsive Breakpoints:**
```css
/* Mobile First Base: 375px */
/* Tablet */
@media (min-width: 768px) {
  /* Scale up 1.5x */
}

/* Desktop */
@media (min-width: 1024px) {
  /* Center game in viewport */
  /* Max-width: 450px */
}
```

**Performance Targets:**
- Frame rate: 60 FPS minimum
- Input latency: < 50ms
- Memory usage: < 50MB
- Battery efficient: RequestAnimationFrame, no setInterval

**Mobile-Specific Optimizations:**
- Use `will-change: transform` on animated elements
- Disable complex effects on low-power mode
- Canvas size: Match screen, CSS scales
- Touch targets: Minimum 44×44px for any tappable UI

### 5.3 Browser Compatibility

**iOS Safari (Primary):**
- iOS 14+ support
- Disable double-tap zoom: `touch-action: manipulation`
- Prevent elastic scrolling: `overscroll-behavior: none`
- WebKit prefixes for transforms

**Android Chrome (Primary):**
- Chrome 90+ support
- Same touch optimizations as iOS
- Vibration API for haptic feedback (optional)

**Feature Detection:**
```javascript
const supports = {
  touch: 'ontouchstart' in window,
  vibration: 'vibrate' in navigator,
  webp: document.createElement('canvas').toDataURL('image/webp').indexOf('data:image/webp') === 0
};
```

### 5.4 Playtime Target (2-5 minutes)

**Difficulty Curve:**
```javascript
// Speed increases with score
function getGameSpeed(score) {
  return 2 + (score * 0.02); // 2px/frame at start, +0.02 per point
}

// Spawn rate increases
function getSpawnRate(score) {
  return Math.max(800, 2000 - (score * 12)); // 2000ms → 800ms
}

// Gap size decreases
function getGapSize(score) {
  return Math.max(120, 200 - (score * 0.8)); // 200px → 120px
}
```

**Session Length Estimates:**
- Average skilled player: 2-3 minutes to reach 100
- Casual player: Multiple attempts, 5 minutes total
- Expert speedrun: 90 seconds possible

**Progression Pacing:**
- 0-30: Learning phase, forgiving
- 31-60: Skill test, moderate challenge
- 61-99: Intense, mastery required
- 100: Victory, celebration

---

## 6. Bankr Brand Integration

### 6.1 Color Usage

**Primary Brand Colors in Game:**

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| **Victory Code** | Bankr Purple | `#9d4edd` | 0xKODA text, glow effects |
| **CTA Buttons** | Bankr Orange | `#ff9e00` | Start, Retry, Share buttons |
| **Progress Bar** | Gradient | `#9d4edd → #ff9e00` | Score 90+ indicator |
| **High Score** | Bankr Purple | `#9d4edd` | Personal best display |
| **Koda Mention** | Bankr Purple | `#9d4edd` | Branding bar |
| **Bankr Mention** | Bankr Orange | `#ff9e00` | Branding bar |

**Brand Color Distribution:**
- 60% Game colors (space, candles, neutral)
- 25% Bankr Purple (accents, victory, Koda)
- 15% Bankr Orange (actions, heat, excitement)

### 6.2 Logo/Branding Placement

**Persistent Branding Bar:**
```
┌─────────────────────────┐
│                         │
│      GAME AREA          │
│                         │
├─────────────────────────┤
│  Built by Koda 🐻 │     │
│  Powered by Bankr       │
└─────────────────────────┘
```

**Placement Rules:**
- Always visible on all screens
- Bottom center, 20px from edge
- Semi-transparent to not obstruct gameplay
- 12px font size for mobile readability

**Logo Variations:**
- Start screen: Slightly larger (14px) with glow
- Gameplay: Minimal (10px), no glow to reduce distraction
- Victory: Larger (14px), celebratory glow

### 6.3 Credit Text Styling

**Branding Bar CSS:**
```css
.branding-bar {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  font-family: "Press Start 2P", monospace;
  font-size: 10px;
  line-height: 1.6;
  text-align: center;
  color: rgba(255, 255, 255, 0.7);
  z-index: 100;
  pointer-events: none; /* Don't block game touches */
}

.branding-bar .line1 {
  color: #9d4edd; /* Koda purple */
}

.branding-bar .line2 {
  color: #ff9e00; /* Bankr orange */
}

.branding-bar .divider {
  color: rgba(255, 255, 255, 0.4);
  margin: 0 8px;
}

/* Enhanced on static screens */
.screen-start .branding-bar,
.screen-victory .branding-bar {
  font-size: 12px;
  text-shadow: 0 0 10px rgba(157, 78, 221, 0.5);
}
```

**HTML Structure:**
```html
<div class="branding-bar">
  <span class="line1">Built by Koda 🐻</span>
  <span class="divider">|</span>
  <span class="line2">Powered by Bankr</span>
</div>
```

### 6.4 Bankr Visual Elements

**Victory Screen Bankr Integration:**
- 0xKODA code border uses Bankr orange
- Confetti includes Bankr purple and orange
- Victory text: "YOU'RE BULLISH!" (crypto slang + Bankr association)

**Subtle Brand Moments:**
- Score 50: "Halfway to the moon! 🌙" (crypto reference)
- Score 90: Progress bar turns Bankr gradient
- Victory: "Bankr-powered victory!" small text option

---

## 7. Asset Reference

### 7.1 Existing Assets (DO NOT MODIFY)

| Asset | File | Dimensions | Usage |
|-------|------|------------|-------|
| **Koda Sprite** | `koda-sprite.png` | ~64×64px | Player character |
| **Red Candle** | `red-candle.png` | ~32×48px | Falling obstacle (bearish) |
| **Green Candle** | `green-candle.png` | ~32×48px | Rising obstacle (bullish) |
| **Space Background** | `space-background.png` | 375×812+ | Tiled background |
| **Powerup Glow** | `powerup-glow.png` | ~32×32px | Particle effects |

### 7.2 Asset Implementation Notes

**Koda Sprite:**
- Render at 64×64px in game
- Center point at 32×40px (slightly lower for balance)
- Rotation pivot: center of sprite

**Candles:**
- Render at native resolution
- Hitbox: Slightly smaller than visual (2px margin for forgiveness)
- Spawn off-screen, animate in

**Background:**
- Tile horizontally if needed
- Parallax: 0.3x game speed
- Slight vertical drift for depth

---

## 8. Implementation Checklist

### For Development Team

**Core Mechanics:**
- [ ] Canvas setup with 375×812 logical resolution
- [ ] Koda physics (gravity, thrust, rotation)
- [ ] Candle spawning system (alternating red/green)
- [ ] Collision detection (circle vs rectangle)
- [ ] Score tracking and high score persistence (localStorage)
- [ ] Game state management (start, playing, gameover, victory)

**Visuals:**
- [ ] Space background with parallax stars
- [ ] Koda sprite with rotation and particle trail
- [ ] Candle obstacles with glow effects
- [ ] Score HUD with glow animation
- [ ] All screens styled per this document

**Animations:**
- [ ] Koda thrust animation
- [ ] Candle spawn animation
- [ ] Collision explosion
- [ ] Screen transitions
- [ ] Victory celebration

**Audio (if time permits):**
- [ ] Thrust sound
- [ ] Score milestone chime
- [ ] Collision sound
- [ ] Victory fanfare

**Bankr Integration:**
- [ ] Brand colors in victory screen
- [ ] Branding bar on all screens
- [ ] 0xKODA code display
- [ ] Confetti in brand colors

**Mobile Optimization:**
- [ ] Touch controls responsive
- [ ] No zoom/scroll interference
- [ ] 60 FPS on target devices
- [ ] Works offline (single file)

---

## 9. Quick Reference

### Color Palette (Hex)
```
Bankr Purple:  #9d4edd
Bankr Orange:  #ff9e00
Cosmic Black:  #0a0a0f
Deep Space:    #1a1a2e
Nebula Purple: #2d2b55
Star White:    #ffffff
Candle Red:    #e74c3c
Candle Green:  #2ecc71
Rocket Flame:  #ff6b35
```

### Typography Scale
```
Title:       36px  Press Start 2P
Score:       48px  Press Start 2P
Code:        48px  Press Start 2P  (0xKODA)
Buttons:     14-16px Press Start 2P
Labels:      10px  Press Start 2P
Branding:    10-12px Press Start 2P
```

### Animation Durations
```
Thrust:           300ms
Screen fade:      400ms
Explosion:        800ms
Victory sequence: 1200ms
Gentle bob:       2000ms (loop)
Pulse glow:       2000ms (loop)
```

### Z-Index Stack
```
0:  Background (space)
1:  Stars (parallax layers)
2:  Candles (obstacles)
3:  Particles (trails, effects)
4:  Koda (player)
5:  Explosions (collision)
6:  UI Overlay (screens, HUD)
7:  Branding bar
8:  Modal/Victory (highest)
```

---

**Document End**

*For questions about implementation, refer to existing assets in `/assets/` directory and follow the specifications above. The goal is a polished, on-brand gaming experience that celebrates ETHDenver 2026 and showcases Bankr technology.*
