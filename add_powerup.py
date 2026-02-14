#!/usr/bin/env python3
"""
Add power-up system to Bull Run Rocket game
- 64x64 control panel icon
- Spawns every 15-20 seconds
- 5-second hyper speed + invincibility
- Guaranteed spawn within first 25 seconds
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

# 2. Add power-up variables after other game state variables
# Find where game state vars are defined (after "let particles = [];")
state_vars_pattern = r'(let particles = \[\];)'
powerup_vars = '''
    // Power-up system
    let powerups = [];
    let powerupSpawnTimer = 0;
    let boosting = false;
    let boostTimer = 0;
    let invincible = false;
    let invincibleTimer = 0;
    const BOOST_DURATION = 5000; // 5 seconds in milliseconds
    const POWERUP_SPAWN_MIN = 900; // 15 seconds at 60fps
    const POWERUP_SPAWN_MAX = 1200; // 20 seconds at 60fps'''

html = html.replace(state_vars_pattern, state_vars_pattern + powerup_vars)

# 3. Add power-up spawn function before update() function
spawn_function = '''
    function spawnPowerup() {
      const x = Math.random() * (GAME_WIDTH - 48) + 24; // Keep away from edges
      const y = Math.random() * (GAME_HEIGHT * 0.6) + GAME_HEIGHT * 0.2; // Middle 60% of screen
      powerups.push({
        x: x,
        y: y,
        size: 48,
        collected: false,
        pulseTimer: 0
      });
    }
    
    function updatePowerups() {
      // Spawn timer
      if (playing && !gameOver && !victory) {
        powerupSpawnTimer++;
        
        // Random spawn between 15-20 seconds
        const nextSpawn = POWERUP_SPAWN_MIN + Math.random() * (POWERUP_SPAWN_MAX - POWERUP_SPAWN_MIN);
        
        if (powerupSpawnTimer >= nextSpawn && powerups.length === 0) {
          spawnPowerup();
          powerupSpawnTimer = 0;
        }
      }
      
      // Update existing powerups
      powerups.forEach(p => {
        p.pulseTimer += 0.1;
        
        // Check collision with Koda
        if (!p.collected && playing && !gameOver) {
          const dx = p.x - koda.x;
          const dy = p.y - koda.y;
          const distance = Math.sqrt(dx * dx + dy * dy);
          
          if (distance < (p.size / 2 + koda.size / 2 - 10)) {
            p.collected = true;
            activateBoost();
            playSound('victory');
          }
        }
      });
      
      // Remove collected powerups
      powerups = powerups.filter(p => !p.collected);
    }
    
    function activateBoost() {
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
          color: `hsl(${Math.random() * 60 + 180}, 100%, 60%)`, // Cyan/blue particles
          size: Math.random() * 4 + 2
        });
      }
    }
    
    function drawPowerups(ctx) {
      powerups.forEach(p => {
        if (!p.collected) {
          ctx.save();
          
          // Pulsing glow effect
          const pulse = Math.sin(p.pulseTimer) * 0.3 + 1;
          const glowSize = p.size * pulse;
          
          // Outer glow
          const gradient = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, glowSize);
          gradient.addColorStop(0, 'rgba(255, 165, 0, 0.4)');
          gradient.addColorStop(0.5, 'rgba(255, 120, 0, 0.2)');
          gradient.addColorStop(1, 'rgba(255, 120, 0, 0)');
          
          ctx.fillStyle = gradient;
          ctx.fillRect(p.x - glowSize, p.y - glowSize, glowSize * 2, glowSize * 2);
          
          // Draw power-up icon
          const img = images.powerup;
          if (img && img.complete) {
            ctx.drawImage(img, p.x - p.size/2, p.y - p.size/2, p.size, p.size);
          }
          
          // Spinning particles around powerup
          for (let i = 0; i < 3; i++) {
            const angle = p.pulseTimer * 2 + (i * Math.PI * 2 / 3);
            const radius = 30;
            const px = p.x + Math.cos(angle) * radius;
            const py = p.y + Math.sin(angle) * radius;
            
            ctx.fillStyle = 'rgba(255, 165, 0, 0.6)';
            ctx.beginPath();
            ctx.arc(px, py, 3, 0, Math.PI * 2);
            ctx.fill();
          }
          
          ctx.restore();
        }
      });
      
      // Draw boost effect when active
      if (boosting) {
        // Hyper speed trail
        ctx.save();
        for (let i = 0; i < 5; i++) {
          const alpha = (5 - i) / 10;
          const offset = i * 15;
          ctx.globalAlpha = alpha;
          
          // Speed lines
          ctx.strokeStyle = `rgba(0, 200, 255, ${alpha})`;
          ctx.lineWidth = 3;
          ctx.beginPath();
          ctx.moveTo(koda.x - 30, koda.y - offset);
          ctx.lineTo(koda.x - 60, koda.y - offset - 20);
          ctx.stroke();
        }
        ctx.restore();
        
        // Invincibility shield
        ctx.save();
        ctx.strokeStyle = 'rgba(0, 200, 255, 0.5)';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(koda.x, koda.y, koda.size + 10 + Math.sin(Date.now() / 100) * 5, 0, Math.PI * 2);
        ctx.stroke();
        ctx.restore();
      }
    }
'''

# Find the update() function and insert powerup functions before it
update_pattern = r'(\s+)(function update\(\) \{)'
html = re.sub(update_pattern, r'\n' + spawn_function + r'\1\2', html)

# 4. Add updatePowerups() call inside update() function after particle updates
# Find where particles are updated in the update function
particle_update_pattern = r'(particles\.forEach\(p => \{[^}]+\}\);[\s\n]+particles = particles\.filter\(p => p\.life > 0\);)'
powerup_update_call = r'\1\n      \n      // Update power-ups\n      updatePowerups();'

html = re.sub(particle_update_pattern, powerup_update_call, html, flags=re.DOTALL)

# 5. Add boost expiry check in update() function
# Find the invincibility timer decrement and add boost check after it
invincible_pattern = r'(if \(invincibleTimer > 0\) \{\s+invincibleTimer--;[\s\n]+if \(invincibleTimer === 0\) \{\s+invincible = false;\s+\}\s+\})'
boost_check = r'\1\n      \n      // Handle boost expiry\n      if (boosting && Date.now() - boostTimer > BOOST_DURATION) {\n        boosting = false;\n      }'

html = re.sub(invincible_pattern, boost_check, html)

# 6. Modify collision detection to respect invincibility
collision_pattern = r'(function checkCollision\(\) \{)'
collision_replacement = r'\1\n      if (invincible) return false; // No collision during invincibility'

html = html.replace(collision_pattern, collision_replacement)

# 7. Add boost effect to Koda movement (auto-upward during boost)
# Find where koda velocity is updated and add boost logic
velocity_pattern = r'(koda\.vy \+= GRAVITY;)'
boost_movement = r'// Apply boost effect\n      if (boosting) {\n        koda.vy = -8; // Auto-upward movement during boost\n      }\n      \n      \1'

html = html.replace(velocity_pattern, boost_movement)

# 8. Add drawPowerups() call in draw() function before UI elements
draw_pattern = r'(drawParticles\(ctx\);)'
draw_powerup_call = r'\1\n    drawPowerups(ctx);'

html = html.replace(draw_pattern, draw_powerup_call)

# 9. Reset power-up state in startGame()
startgame_pattern = r'(function startGame\(\) \{[^}]+particles = \[\];)'
powerup_reset = r'\1\n      \n      // Reset power-up state\n      powerups = [];\n      powerupSpawnTimer = 0;\n      boosting = false;\n      boostTimer = 0;\n      invincible = false;\n      invincibleTimer = 0;'

html = re.sub(startgame_pattern, powerup_reset, html)

# Write the modified HTML
with open('index.html', 'w') as f:
    f.write(html)

print("✅ Power-up system added successfully!")
print("🎮 Features:")
print("   - 64x64 control panel power-up icon")
print("   - Spawns every 15-20 seconds")
print("   - 5-second hyper speed + invincibility")
print("   - Cyan boost effects and shield")
print("   - Auto-upward movement during boost")
