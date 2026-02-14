#!/usr/bin/env python3
"""
Fix power-up spawning issues and update high score display
"""

import re

# Read the current index.html
with open('index.html', 'r') as f:
    html = f.read()

# 1. Fix power-up spawn timer - needs to store target spawn time
# Replace the powerup variables section with proper spawn target tracking
old_powerup_vars = r'''    // Power-up system
    let powerups = \[\];
    let powerupSpawnTimer = 0;
    let boosting = false;
    let boostTimer = 0;
    let invincible = false;
    let invincibleTimer = 0;
    const BOOST_DURATION = 5000; // 5 seconds in milliseconds
    const POWERUP_SPAWN_MIN = 900; // 15 seconds at 60fps
    const POWERUP_SPAWN_MAX = 1200; // 20 seconds at 60fps'''

new_powerup_vars = '''    // Power-up system
    let powerups = [];
    let powerupSpawnTimer = 0;
    let nextPowerupSpawn = 600; // First spawn at 10 seconds (guaranteed before 25s)
    let boosting = false;
    let boostTimer = 0;
    let invincible = false;
    let invincibleTimer = 0;
    const BOOST_DURATION = 5000; // 5 seconds in milliseconds
    const POWERUP_SPAWN_MIN = 900; // 15 seconds at 60fps
    const POWERUP_SPAWN_MAX = 1200; // 20 seconds at 60fps'''

html = re.sub(old_powerup_vars, new_powerup_vars, html)

# 2. Fix updatePowerups() spawn logic
old_update_powerups = r'''function updatePowerups\(\) \{
      // Spawn timer
      if \(playing && !gameOver && !victory\) \{
        powerupSpawnTimer\+\+;
        
        // Random spawn between 15-20 seconds
        const nextSpawn = POWERUP_SPAWN_MIN \+ Math\.random\(\) \* \(POWERUP_SPAWN_MAX - POWERUP_SPAWN_MIN\);
        
        if \(powerupSpawnTimer >= nextSpawn && powerups\.length === 0\) \{
          spawnPowerup\(\);
          powerupSpawnTimer = 0;
        \}
      \}'''

new_update_powerups = '''function updatePowerups() {
      // Spawn timer
      if (playing && !gameOver && !victory) {
        powerupSpawnTimer++;
        
        // Check if it's time to spawn
        if (powerupSpawnTimer >= nextPowerupSpawn && powerups.length === 0) {
          spawnPowerup();
          powerupSpawnTimer = 0;
          // Set next spawn time (15-20 seconds)
          nextPowerupSpawn = POWERUP_SPAWN_MIN + Math.random() * (POWERUP_SPAWN_MAX - POWERUP_SPAWN_MIN);
        }
      }'''

html = re.sub(old_update_powerups, new_update_powerups, html, flags=re.DOTALL)

# 3. Add updatePowerups() call in the update() function
# Find where particles are being filtered and add powerup update after
particles_filter = r'(particles = particles\.filter\(p => p\.life > 0\);)'
powerup_update_call = r'\1\n      \n      // Update power-ups\n      updatePowerups();'

html = re.sub(particles_filter, powerup_update_call, html)

# 4. Reset power-up state in startGame() - fix the reset section
old_reset = r'''// Reset power-up state
      powerups = \[\];
      powerupSpawnTimer = 0;
      boosting = false;
      boostTimer = 0;
      invincible = false;
      invincibleTimer = 0;'''

new_reset = '''// Reset power-up state
      powerups = [];
      powerupSpawnTimer = 0;
      nextPowerupSpawn = 600; // First spawn at 10 seconds
      boosting = false;
      boostTimer = 0;
      invincible = false;
      invincibleTimer = 0;'''

html = re.sub(old_reset, new_reset, html)

# 5. Update high score display to show "s" for seconds
# Find the bestScore value display
old_score_display = r'(<div class="value">\$\{bestScore\}</div>)'
new_score_display = r'<div class="value">${bestScore}s</div>'

html = re.sub(old_score_display, new_score_display, html)

# 6. Reset the stored high score by updating the localStorage key
# Find where bestScore is loaded from localStorage
old_load_best = r'(let bestScore = parseInt\(localStorage\.getItem\(\'bullRunBestScore\'\)\) \|\| 0;)'
new_load_best = r"let bestScore = parseInt(localStorage.getItem('bullRunBestScoreV2')) || 0;"

html = re.sub(old_load_best, new_load_best, html)

# Update where bestScore is saved
old_save_best = r'(localStorage\.setItem\(\'bullRunBestScore\', bestScore\);)'
new_save_best = r"localStorage.setItem('bullRunBestScoreV2', bestScore);"

html = re.sub(old_save_best, new_save_best, html)

# Write the modified HTML
with open('index.html', 'w') as f:
    f.write(html)

print("✅ Power-ups fixed!")
print("   - Spawn timer now properly tracks target spawn time")
print("   - First power-up spawns at 10 seconds (guaranteed before 25s)")
print("   - updatePowerups() is now called in game loop")
print("   - High score display now shows '##s' format")
print("   - High score reset (uses new localStorage key)")
