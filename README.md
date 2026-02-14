# Bull Run Rocket 🚀🐻

A Flappy Bird-style crypto game for ETHDenver 2026 - single-file, play instantly!

## 🎮 Quick Start

1. **Open the game:**
   ```bash
   open index.html
   ```
   Or drag `index.html` into any browser!

2. **Play:**
   - **Mobile:** Tap anywhere to fly
   - **Desktop:** Click or press Space/Arrow Up

3. **Goal:** Score 100 to unlock the "0xKODA" code! ✨

---

## 📁 File Structure

```
bull-run-rocket/
├── index.html           # Complete game (13.3 MB - single file!)
├── DESIGN.md            # Original design specification
├── BUILD_SUMMARY.md     # Detailed build documentation
├── assets/              # Source PNG images (for reference)
│   ├── koda-sprite.png
│   ├── red-candle.png
│   ├── green-candle.png
│   ├── space-background.png
│   └── powerup-glow.png
└── README.md            # This file
```

---

## 🎯 How to Win

1. **Tap rhythmically** to maintain altitude
2. **Avoid red candles** (falling - bear market 📉)
3. **Avoid green candles** (rising - bull market 📈)
4. **Score 100** to unlock the "0xKODA" victory code
5. **Screenshot** the victory screen to save your code!

### Difficulty Curve
- **0-30:** Easy learning phase
- **31-60:** Moderate challenge
- **61-90:** Intense mastery required
- **90-99:** Final push (watch the progress bar!)
- **100:** VICTORY! 🎉

---

## 🎨 Features

### Game Mechanics
- ✅ Flappy Bird-style flight physics
- ✅ Red candles (falling from top) + Green candles (rising from bottom)
- ✅ Gap-based scoring system
- ✅ Progressive difficulty scaling
- ✅ High score persistence (localStorage)

### Visual Effects
- ✅ Rocket trail particles
- ✅ Collision explosions
- ✅ Victory confetti 🎊
- ✅ Parallax star background
- ✅ Candle tumble animations
- ✅ CRT scanline overlay

### Audio
- ✅ Thrust sound (upward beeps)
- ✅ Score chime (melodic)
- ✅ Collision crash
- ✅ Victory fanfare

### UI/UX
- ✅ Press Start 2P retro font
- ✅ Score HUD with pulse animation
- ✅ Progress bar (score 90+)
- ✅ Mobile-first responsive design
- ✅ Touch + keyboard controls
- ✅ Branding: "Built by Koda 🐻 | Powered by Bankr"

---

## 🖥️ Platform Support

### ✅ Mobile
- iOS Safari 14+
- Android Chrome 90+
- Touch-optimized controls
- No zoom/scroll interference

### ✅ Desktop
- Chrome/Edge/Firefox/Safari
- Click or Space/Arrow Up controls
- Responsive canvas scaling

---

## 📊 Game Balance

**Target playtime:** 2-5 minutes per victory run
**Current achievement:** ✅ Balanced and achievable

| Score Range | Difficulty | Game Speed | Spawn Rate |
|-------------|------------|------------|------------|
| 0-30        | Easy       | 2.0-2.6 px/frame | Every 90 frames |
| 31-60       | Moderate   | 2.6-3.2 px/frame | Every 85 frames |
| 61-90       | Hard       | 3.2-3.8 px/frame | Every 80 frames |
| 90-99       | Extreme    | 3.8-4.0 px/frame | Every 75 frames |
| 100         | Victory!   | -          | -          |

---

## 🎨 Design Compliance

Follows Kimi's DESIGN.md specification exactly:

- Colors: Cosmic Black, Bankr Purple (#9d4edd), Bankr Orange (#ff9e00)
- Typography: Press Start 2P from Google Fonts
- All 4 game states: Start, Playing, Victory, Game Over
- Asset base64 encoding for single-file distribution
- Mobile-first 375×812 baseline ratio
- Pixel-perfect UI overlays with glow effects

---

## 🔧 Technical Details

### File Info
- **Size:** 13.3 MB (all assets base64-encoded inside)
- **Type:** Single HTML file
- **Dependencies:** None (Google Fonts loaded remotely)

### Tech Stack
- HTML5 Canvas for rendering
- Pure JavaScript (no frameworks)
- CSS3 for UI overlays
- Web Audio API for sound
- localStorage for persistence

### Performance
- Target: 60 FPS
- Optimizations: RequestAnimationFrame, GPU acceleration
- Tested: iOS Safari + Android Chrome

---

## 🚀 Deployment Options

### 1. Static Hosting (Recommended)
```bash
# GitHub Pages, Netlify, Vercel, etc.
# Just upload index.html - that's it!
```

### 2. Local Server
```bash
cd bull-run-rocket
python3 -m http.server 8000
# Visit http://localhost:8000
```

### 3. Direct File Open
```bash
# Works instantly in any browser
open index.html
# or drag into browser window
```

---

## 📝 Notes

- **File size:** 13.3MB due to base64 encoding (necessary for single-file)
- **Audio context:** Requires first tap/click to initialize (browser policy)
- **Keyboard focus:** On desktop, click the game area before using Space/Arrow Up

---

## 🏆 Achievements

| Achievement | Reward |
|-------------|--------|
| First Blood | Score 10 |
| Halfway There | Score 50 |
| Almost There | Score 90 (progress bar appears) |
| 🎉 VICTORY 🎉 | Score 100 → Unlock "0xKODA" code |

---

## 🤝 Credits

- **Design:** Kimi (ETHDenver 2026)
- **Development:** Per DESIGN.md specifications
- **Branding:** Bankr integration
- **Assets:** Base64-encoded from original PNGs

---

**Built for ETHDenver 2026** 🏔️

**Built by Koda 🐻 | Powered by Bankr**

---

*Tap to fly, dodge the candles, unlock 0xKODA! 🚀*