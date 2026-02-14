#!/usr/bin/env python3
"""
Add power-up system with debugging - step by step approach
"""

import base64
import re

# Read the power-up image
with open('/home/profeeder/.openclaw/media/inbound/08d2712f-406f-4eba-bb7e-71e911994dfb.png', 'rb') as f:
    powerup_data = base64.b64encode(f.read()).decode('utf-8')

powerup_base64 = f'data:image/png;base64,{powerup_data}'

# Read the current index.html
with open('index.html', 'r') as f:
    html = f.read()

# 1. Add power-up asset to ASSETS object
assets_pattern = r'(const ASSETS = \{[^}]+)(};)'
assets_addition = f",\n      powerup: '{powerup_base64}'"
html = re.sub(assets_pattern, r'\1' + assets_addition + r'\n    \2', html)

# 2. Add power-up variables after game state variables
# Find where score variables are defined
state_vars_pattern = r'(let score = 0;\s+let scoreTimer = 0;)'
powerup_vars = '''
    
    // Power-up system
    let powerups = [];
    let powerupSpawnTimer = 0;
    let nextPowerupSpawn = 600; // First spawn at 10 seconds (60fps * 10)
    let boosting = false;
    let boostTimer = 0;
    let invincible = false;
    let invincibleTimer = 0;
    const BOOST_DURATION = 5000; // 5 seconds in milliseconds
    const POWERUP_SPAWN_MIN = 900; // 15 seconds at 60fps
    const POWERUP_SPAWN_MAX = 1200; // 20 seconds at 60fps
    
    console.log('Power-up variables initialized');'''

html = html.replace(state_vars_pattern, state_vars_pattern + powerup_vars)

# 3. Add power-up functions before update() function
# Find the update() function
update_pattern = r'(\s+function update\(\) \{)'

powerup_functions = '''
    // Spawn power-up
    function spawnPowerup() {
      console.log('Spawning power-up');
      const x = Math.random() * (GAME_WIDTH - 48) + 24;
      const y = Math.random() * (GAME_HEIGHT * 0.6) + GAME_HEIGHT * 0.2;
      powerups.push({
        x: x,
        y: y,
        size: 48,
        collected: false,
        pulseTimer: 0
      });
    }
    
    // Update power-ups
    function updatePowerups() {
      if (gameState === 'playing') {
        powerupSpawnTimer++;
        
        if (powerupSpawnTimer >= nextPowerupSpawn && powerups.length === 0) {
          spawnPowerup();
          powerupSpawnTimer = 0;
          nextPowerupSpawn = POWERUP_SPAWN_MIN + Math.random() * (POWERUP_SPAWN_MAX - POWERUP_SPAWN_MIN);
        }
      }
      
      // Update existing powerups
      for (let i = powerups.length - 1; i >= 0; i--) {
        const p = powerups[i];
        p.pulseTimer += 0.1;
        
        // Check collision with Koda
        if (!p.collected && gameState === 'playing') {
          const dx = p.x - koda.x;
          const dy = p.y - koda.y;
          const distance = Math.sqrt(dx * dx + dy * dy);
          
          if (distance < (p.size / 2 + 32)) {
            console.log('Power-up collected!');
            p.collected = true;
            activateBoost();
            playSound('victory');
          }
        }
        
        // Remove collected powerups
        if (p.collected) {
          powerups.splice(i, 1);
        }
      }
    }
    
    // Activate boost
    function activateBoost() {
      console.log('Activating boost');
      boosting = true;
      boostTimer = Date.now();
      invincible = true;
      invincibleTimer = 300; // 5 seconds at 60fps
      
      // Create boost collection particles
      for (let i = 0; i < 30; i++) {
        particles.push({
          x: koda.x,
          y: koda.y,
          vx: (Math.random() - 0.5) * 8,
          vy: (Math.random() - 0.5) * 8,
          life: 60,
          decay: 1,
          color: `hsl(${Math.random() * 60 + 180}, 100%, 60%)`,
          size: Math.random() * 4 + 2
        });
      }
    }
    
    // Draw power-ups
    function drawPowerups(ctx) {
      for (const p of powerups) {
        if (!p.collected) {
          ctx.save();
          
          // Pulsing glow
          const pulse = Math.sin(p.pulseTimer) * 0.3 + 1;
          const glowSize = p.size * pulse;
          
          const gradient = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, glowSize);
          gradient.addColorStop(0, 'rgba(255, 165, 0, 0.4)');
          gradient.addColorStop(0.5, 'rgba(255, 120, 0, 0.2)');
          gradient.addColorStop(1, 'rgba(255, 120, 0, 0)');
          
          ctx.fillStyle = gradient;
          ctx.fillRect(p.x - glowSize, p.y - glowSize, glowSize * 2, glowSize * 2);
          
          // Draw icon
          const img = images.powerup;
          if (img && img.complete) {
            ctx.drawImage(img, p.x - p.size/2, p.y - p.size/2, p.size, p.size);
          }
          
          ctx.restore();
        }
      }
      
      // Draw boost effect
      if (boosting) {
        ctx.save();
        ctx.strokeStyle = 'rgba(0, 200, 255, 0.5)';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(koda.x, koda.y, 42 + Math.sin(Date.now() / 100) * 5, 0, Math.PI * 2);
        ctx.stroke();
        ctx.restore();
      }
    }
    
'''

html = re.sub(update_pattern, powerup_functions + r'\1', html)

# 4. Add updatePowerups() call in update() function
# Find the invincibility timer section
invincible_pattern = r'(// Handle invincibility[\s\S]+?invincible = false;\s+}\s+})'
powerup_update = r'''\1
      
      // Handle boost expiry
      if (boosting && Date.now() - boostTimer > BOOST_DURATION) {
        console.log('Boost expired');
        boosting = false;
      }
      
      // Update power-ups
      updatePowerups();'''

html = re.sub(invincible_pattern, powerup_update, html)

# 5. Modify collision detection to respect invincibility
collision_pattern = r'(// Check collision[\s\S]*?)(if \(checkCollision\(\)\) \{)'
collision_fix = r'\1if (!invincible && checkCollision()) {'

html = re.sub(collision_pattern, collision_fix, html)

# 6. Add drawPowerups() call in draw() function
# Find where particles are drawn
draw_pattern = r'(// Draw particles[\s\S]+?drawParticles\(ctx\);)'
draw_powerup = r'\1\n      drawPowerups(ctx);'

html = re.sub(draw_pattern, draw_powerup, html)

# 7. Reset power-up state in startGame()
# Find where particles are cleared in startGame
startgame_pattern = r'(function startGame\(\) \{[\s\S]+?particles = \[\];)'
powerup_reset = r'''\1
      
      // Reset power-up state
      powerups = [];
      powerupSpawnTimer = 0;
      nextPowerupSpawn = 600;
      boosting = false;
      boostTimer = 0;
      invincible = false;
      invincibleTimer = 0;
      console.log('Power-up state reset');'''

html = re.sub(startgame_pattern, powerup_reset, html)

# Write the modified HTML
with open('index.html', 'w') as f:
    f.write(html)

print("✅ Power-up system added with debug logging")
print("   - Check browser console for logs")
print("   - Power-up spawns at 10 seconds")
print("   - 5-second boost with invincibility")
