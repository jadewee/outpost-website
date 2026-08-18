import re

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'r') as f:
    content = f.read()

# Replace drawOtter
new_draw_otter = """
  // Helper to draw the otter matching the screenshot
  function drawOtter(x, y, width, height) {
    const w = width;
    const h = height; 
    
    ctx.save();
    ctx.translate(x, y);

    // Drop shadow
    ctx.fillStyle = 'rgba(0,0,0,0.15)';
    ctx.beginPath();
    ctx.ellipse(w/2, h + 5, w/2, 6, 0, 0, Math.PI * 2);
    ctx.fill();

    // Arms (up in the air)
    ctx.fillStyle = '#A46543'; // Brown
    ctx.lineWidth = 6;
    ctx.lineCap = 'round';
    
    // Left arm
    ctx.beginPath();
    ctx.moveTo(w*0.1, h*0.4);
    ctx.lineTo(-w*0.2, h*0.1);
    ctx.stroke();
    // Right arm
    ctx.beginPath();
    ctx.moveTo(w*0.9, h*0.4);
    ctx.lineTo(w*1.2, h*0.1);
    ctx.stroke();

    // Legs
    // Left leg
    ctx.beginPath();
    ctx.moveTo(w*0.3, h*0.85);
    ctx.lineTo(w*0.2, h*1.05);
    ctx.stroke();
    // Right leg
    ctx.beginPath();
    ctx.moveTo(w*0.7, h*0.85);
    ctx.lineTo(w*0.8, h*1.05);
    ctx.stroke();

    // Dark brown feet/hands (paws)
    ctx.fillStyle = '#3E2723';
    ctx.beginPath(); ctx.arc(-w*0.2, h*0.1, 3.5, 0, Math.PI*2); ctx.fill(); // L hand
    ctx.beginPath(); ctx.arc(w*1.2, h*0.1, 3.5, 0, Math.PI*2); ctx.fill();  // R hand
    ctx.beginPath(); ctx.arc(w*0.2, h*1.05, 3.5, 0, Math.PI*2); ctx.fill(); // L foot
    ctx.beginPath(); ctx.arc(w*0.8, h*1.05, 3.5, 0, Math.PI*2); ctx.fill(); // R foot

    // Main Body
    ctx.fillStyle = '#A46543'; // Brown body
    ctx.beginPath();
    ctx.roundRect(0, 0, w, h, w/2);
    ctx.fill();

    // Lighter Belly and Face
    ctx.fillStyle = '#F4D2A6'; // Tan/wheat
    
    // Face area
    ctx.beginPath();
    ctx.ellipse(w/2, h*0.4, w*0.4, h*0.25, 0, 0, Math.PI * 2);
    ctx.fill();

    // Belly area
    ctx.beginPath();
    ctx.ellipse(w/2, h*0.65, w*0.35, h*0.3, 0, 0, Math.PI * 2);
    ctx.fill();

    // Ears
    ctx.fillStyle = '#A46543';
    ctx.beginPath(); ctx.arc(w*0.15, h*0.15, 5, 0, Math.PI*2); ctx.fill();
    ctx.beginPath(); ctx.arc(w*0.85, h*0.15, 5, 0, Math.PI*2); ctx.fill();

    // Inner ears
    ctx.fillStyle = '#3E2723';
    ctx.beginPath(); ctx.arc(w*0.15, h*0.15, 2, 0, Math.PI*2); ctx.fill();
    ctx.beginPath(); ctx.arc(w*0.85, h*0.15, 2, 0, Math.PI*2); ctx.fill();

    // Eyes
    ctx.fillStyle = '#222';
    ctx.beginPath(); ctx.arc(w*0.35, h*0.32, 2.5, 0, Math.PI * 2); ctx.fill();
    ctx.beginPath(); ctx.arc(w*0.65, h*0.32, 2.5, 0, Math.PI * 2); ctx.fill();

    // Nose
    ctx.beginPath(); ctx.ellipse(w/2, h*0.38, 3.5, 2.5, 0, 0, Math.PI*2); ctx.fill();

    // Mouth / Smile
    ctx.strokeStyle = '#222';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.arc(w*0.42, h*0.4, 4, 0, Math.PI);
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(w*0.58, h*0.4, 4, 0, Math.PI);
    ctx.stroke();

    // Whiskers
    ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(w*0.25, h*0.38); ctx.lineTo(w*0.1, h*0.36); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(w*0.25, h*0.42); ctx.lineTo(w*0.1, h*0.44); ctx.stroke();
    
    ctx.beginPath(); ctx.moveTo(w*0.75, h*0.38); ctx.lineTo(w*0.9, h*0.36); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(w*0.75, h*0.42); ctx.lineTo(w*0.9, h*0.44); ctx.stroke();

    ctx.restore();
  }
"""
content = re.sub(r"  // Helper to draw a CUTE full-body otter.*?  // Helper to draw a LEGO Brick", new_draw_otter + "\n  // Helper to draw a Ledge", content, flags=re.DOTALL)

# Replace drawLegoBrick with drawLedge
new_draw_ledge = """
  function drawLedge(x, y, width, height, color, isLeft) {
    ctx.save();
    ctx.translate(x, y);

    // Support brace (Diagonal line connecting ledge to wall)
    ctx.fillStyle = '#28467A'; // Dark blue brace
    ctx.beginPath();
    if (isLeft) {
      // Brace on the left side (wall is left)
      ctx.moveTo(10, height);
      ctx.lineTo(40, height);
      ctx.lineTo(10, height + 40);
    } else {
      // Brace on the right side (wall is right)
      ctx.moveTo(width - 10, height);
      ctx.lineTo(width - 40, height);
      ctx.lineTo(width - 10, height + 40);
    }
    ctx.fill();

    // Main Ledge Body
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.roundRect(0, 0, width, height, height/2);
    ctx.fill();

    // Ledge Highlight (top edge)
    ctx.fillStyle = 'rgba(255,255,255,0.3)';
    ctx.beginPath();
    ctx.roundRect(0, 0, width, height/2, height/2);
    ctx.fill();

    // Little screw on the ledge
    ctx.fillStyle = '#A0AAB5';
    ctx.beginPath();
    if (isLeft) {
      ctx.arc(width - 15, height/2, 2.5, 0, Math.PI*2);
    } else {
      ctx.arc(15, height/2, 2.5, 0, Math.PI*2);
    }
    ctx.fill();

    ctx.restore();
  }
"""
content = re.sub(r"  // Helper to draw a Ledge.*?  class Player", new_draw_ledge + "\n  class Player", content, flags=re.DOTALL)

# Background drawing function
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

# Modify Platform Class
new_platform = """
  const ledgeColors = [
    '#F24C4A', // Red
    '#5BB561', // Green
    '#4E72D7'  // Blue
  ];

  class Platform {
    constructor(y) {
      this.width = 80;
      this.height = 14; 
      this.y = y;
      
      const wallWidth = 60;
      // 50% chance to be on left wall, 50% right wall
      this.isLeft = Math.random() > 0.5;
      
      if (this.isLeft) {
          this.x = wallWidth;
      } else {
          this.x = GAME_WIDTH - wallWidth - this.width;
      }
      
      this.color = ledgeColors[Math.floor(Math.random() * ledgeColors.length)];
      this.type = 'static'; // Keep them static for now as per screenshot vibe
      this.vx = 0;
    }

    update() {}

    draw() {
      drawLedge(this.x, this.y, this.width, this.height, this.color, this.isLeft);
    }
  }
"""
content = re.sub(r"  const rainbowColors = \[.*?  let player;", new_platform + "\n  let player;", content, flags=re.DOTALL)

# Initial platform layout adjustments
content = re.sub(r"let startPlatform = new Platform\(player.y \+ 100\);\n.*?startPlatform\.type = 'static';\n    platforms\.push\(startPlatform\);", 
"""let startPlatform = new Platform(player.y + 100);
    startPlatform.x = player.x - (startPlatform.width / 2) + (player.width / 2); // Center start platform
    startPlatform.isLeft = true; // doesn't matter, just need a base
    platforms.push(startPlatform);""", content, flags=re.DOTALL)

# Add drawBackground() to gameLoop and init
content = re.sub(r"ctx\.clearRect\(0, 0, GAME_WIDTH, GAME_HEIGHT\);", "drawBackground();", content)

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'w') as f:
    f.write(content)
