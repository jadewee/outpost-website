import re

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'r') as f:
    content = f.read()

# Add globals
globals_old = """  let score = 0;
  let gameOver = false;
  let gameStarted = false;
  let baseGravity = 0.15; // Start much slower
  let currentGravity = baseGravity;"""
globals_new = """  let score = 0;
  let gameOver = false;
  let gameStarted = false;
  let baseGravity = 0.15; // Start much slower
  let currentGravity = baseGravity;
  let lastLevel = 1;
  let levelUpTimer = 0;"""
content = content.replace(globals_old, globals_new)

# Reset in init()
init_old = """    score = 0;
    gameOver = false;
    currentGravity = baseGravity;"""
init_new = """    score = 0;
    gameOver = false;
    currentGravity = baseGravity;
    lastLevel = 1;
    levelUpTimer = 0;"""
content = content.replace(init_old, init_new)

# Update Player.update() physics
physics_old = """      // Calculate dynamic gravity and jump strength based on score
      let speedMultiplier = 1 + Math.min(score / 5000, 2); 
      currentGravity = baseGravity * speedMultiplier;
      this.jumpStrength = this.baseJumpStrength * Math.sqrt(speedMultiplier);"""

physics_new = """      // Calculate Level based on score
      let currentLevel = Math.floor(score / 3000) + 1;
      if (currentLevel > lastLevel) {
          lastLevel = currentLevel;
          levelUpTimer = 120; // 2 seconds at 60fps
      }

      // Discrete speed increases per level (e.g. +30% harder each level)
      let speedMultiplier = 1 + (lastLevel - 1) * 0.3; 
      currentGravity = baseGravity * speedMultiplier;
      this.jumpStrength = this.baseJumpStrength * Math.sqrt(speedMultiplier);"""
content = content.replace(physics_old, physics_new)

# Add Celebration UI in gameLoop()
loop_old = """    // Check collisions and draw platforms
    platforms.forEach(p => {"""

loop_new = """    // Level Up Celebration
    if (levelUpTimer > 0) {
        levelUpTimer--;
        ctx.save();
        
        // Background flash
        ctx.fillStyle = `rgba(255, 255, 255, ${ (levelUpTimer / 120) * 0.3 })`;
        ctx.fillRect(0, 0, GAME_WIDTH, GAME_HEIGHT);

        // Text
        let alpha = Math.min(1, levelUpTimer / 40); // fade out at the end
        ctx.fillStyle = `rgba(255, 215, 0, ${alpha})`; 
        ctx.font = '900 48px Quicksand, sans-serif';
        ctx.textAlign = 'center';
        
        // Shadow
        ctx.shadowColor = 'rgba(0,0,0,0.5)';
        ctx.shadowBlur = 10;
        ctx.shadowOffsetX = 0;
        ctx.shadowOffsetY = 4;
        
        ctx.fillText(`LEVEL ${lastLevel}!`, GAME_WIDTH / 2, GAME_HEIGHT / 2 - 30);
        
        ctx.font = '700 24px Quicksand, sans-serif';
        ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`; 
        ctx.fillText("SPEED UP!", GAME_WIDTH / 2, GAME_HEIGHT / 2 + 20);
        
        ctx.restore();
    }

    // Check collisions and draw platforms
    platforms.forEach(p => {"""
content = content.replace(loop_old, loop_new)

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'w') as f:
    f.write(content)
