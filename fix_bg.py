import re

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'r') as f:
    content = f.read()

new_draw_bg = """
  let cloudOffset = 0;

  function drawBackground() {
    // Sky gradient
    let grad = ctx.createLinearGradient(0, 0, 0, GAME_HEIGHT);
    grad.addColorStop(0, '#56BAF2');
    grad.addColorStop(1, '#97DEF2');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, GAME_WIDTH, GAME_HEIGHT);

    // Clouds
    cloudOffset = (cloudOffset + 0.2) % 400;
    ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
    ctx.beginPath();
    ctx.arc(200 - cloudOffset, 120, 25, 0, Math.PI*2);
    ctx.arc(230 - cloudOffset, 120, 35, 0, Math.PI*2);
    ctx.arc(260 - cloudOffset, 120, 25, 0, Math.PI*2);
    ctx.fill();
    
    ctx.beginPath();
    ctx.arc(380 - cloudOffset, 250, 20, 0, Math.PI*2);
    ctx.arc(400 - cloudOffset, 250, 30, 0, Math.PI*2);
    ctx.arc(420 - cloudOffset, 250, 20, 0, Math.PI*2);
    ctx.fill();

    // Bush at bottom left
    ctx.fillStyle = '#6ECA66';
    ctx.beginPath();
    ctx.arc(40, GAME_HEIGHT, 50, 0, Math.PI*2);
    ctx.arc(80, GAME_HEIGHT - 20, 40, 0, Math.PI*2);
    ctx.arc(110, GAME_HEIGHT, 30, 0, Math.PI*2);
    ctx.fill();
    ctx.fillStyle = '#8FE082';
    ctx.beginPath();
    ctx.arc(50, GAME_HEIGHT, 40, 0, Math.PI*2);
    ctx.arc(85, GAME_HEIGHT - 10, 25, 0, Math.PI*2);
    ctx.fill();

    // Climbing Walls
    const wallWidth = 60;
    
    // Left Wall (Salmon)
    ctx.fillStyle = '#F47D75';
    ctx.fillRect(0, 0, wallWidth, GAME_HEIGHT);
    ctx.fillStyle = '#E36961'; // shade line
    ctx.fillRect(wallWidth - 5, 0, 5, GAME_HEIGHT);
    
    // Right Wall (Yellow)
    ctx.fillStyle = '#F3D248';
    ctx.fillRect(GAME_WIDTH - wallWidth, 0, wallWidth, GAME_HEIGHT);
    ctx.fillStyle = '#DEC03D'; // shade line
    ctx.fillRect(GAME_WIDTH - wallWidth, 0, 5, GAME_HEIGHT);

    // Wall dots (screws/holds)
    ctx.fillStyle = '#A0AAB5';
    ctx.strokeStyle = '#555';
    ctx.lineWidth = 1;
    // Draw some static dots on walls
    for (let i=0; i<10; i++) {
        let yPos = (i * 100 + score) % GAME_HEIGHT;
        // Left
        ctx.beginPath(); ctx.arc(wallWidth/2, yPos, 4, 0, Math.PI*2); ctx.fill(); ctx.stroke();
        // Right
        ctx.beginPath(); ctx.arc(GAME_WIDTH - wallWidth/2, yPos + 50, 4, 0, Math.PI*2); ctx.fill(); ctx.stroke();
    }
  }
"""

content = re.sub(r"  class Platform \{", new_draw_bg + "\n  class Platform {", content)

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'w') as f:
    f.write(content)
