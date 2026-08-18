<script>
  const canvas = document.getElementById('gameCanvas');
  const ctx = canvas.getContext('2d');
  
  const GAME_WIDTH = 400;
  const GAME_HEIGHT = 600;
  
  // Set up canvas for high-DPI displays
  const dpr = window.devicePixelRatio || 1;
  canvas.width = GAME_WIDTH * dpr;
  canvas.height = GAME_HEIGHT * dpr;
  canvas.style.width = GAME_WIDTH + 'px';
  canvas.style.height = GAME_HEIGHT + 'px';
  ctx.scale(dpr, dpr);
  
  // UI Elements
  const scoreText = document.getElementById('score-text');
  const gameOverScreen = document.getElementById('game-over-screen');
  const finalScoreText = document.getElementById('final-score-text');
  const rewardTierText = document.getElementById('reward-tier-text');
  const restartBtn = document.getElementById('restart-btn');
  const startScreen = document.getElementById('start-screen');
  const startBtn = document.getElementById('start-btn');
  const claimBtn = document.getElementById('claim-btn');

  let score = 0;
  let gameOver = false;
  let gameStarted = false;
  let baseGravity = 0.15; // Start much slower
  let currentGravity = baseGravity;

  // Handle Initial Start
  startBtn.addEventListener('click', () => {
    startScreen.classList.add('hidden');
    gameStarted = true;
    init(); // Start the game loop
  });

  const keys = {
    ArrowLeft: false,
    ArrowRight: false,
    a: false,
    d: false
  };

  document.addEventListener('keydown', (e) => {
    // Prevent default scrolling for game keys if game is active
    if (gameStarted && !gameOver && (e.key === 'ArrowLeft' || e.key === 'ArrowRight' || e.key === ' ' || e.key === 'ArrowUp' || e.key === 'ArrowDown')) {
        e.preventDefault();
    }
    if (keys.hasOwnProperty(e.key)) keys[e.key] = true;
    if (e.key === 'a' || e.key === 'A') keys.a = true;
    if (e.key === 'd' || e.key === 'D') keys.d = true;
  });

  document.addEventListener('keyup', (e) => {
    if (keys.hasOwnProperty(e.key)) keys[e.key] = false;
    if (e.key === 'a' || e.key === 'A') keys.a = false;
    if (e.key === 'd' || e.key === 'D') keys.d = false;
  });

  // UI Restart Button listener
  restartBtn.addEventListener('click', () => {
    if (gameOver) {
      gameOverScreen.classList.remove('visible');
      init();
    }
  });

  claimBtn.addEventListener('click', () => {
    alert("Redirecting to chatbot handoff flow...");
  });


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


  function drawLedge(x, y, width, height, color, isLeft) {
    ctx.save();
    ctx.translate(x, y);

    // Support brace (Diagonal line connecting ledge to wall)
    ctx.fillStyle = '#28467A'; // Dark blue brace
    ctx.beginPath();
    if (isLeft) {
      // Brace on the left side (wall is left)
      ctx.moveTo(0, height);
      ctx.lineTo(35, height);
      ctx.lineTo(0, height + 35);
    } else {
      // Brace on the right side (wall is right)
      ctx.moveTo(width, height);
      ctx.lineTo(width - 35, height);
      ctx.lineTo(width, height + 35);
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
      ctx.arc(15, height/2, 2.5, 0, Math.PI*2);
    } else {
      ctx.arc(width - 15, height/2, 2.5, 0, Math.PI*2);
    }
    ctx.fill();

    ctx.restore();
  }

  class Player {
    constructor() {
      this.width = 36;
      this.height = 54;
      this.x = GAME_WIDTH / 2 - this.width / 2;
      this.y = GAME_HEIGHT / 2;
      this.vx = 0;
      this.vy = 0;
      this.baseJumpStrength = -7; 
      this.jumpStrength = this.baseJumpStrength;
      this.speed = 6;
    }

    update() {
      // Horizontal movement
      if (keys.ArrowLeft || keys.a) {
        this.vx = -this.speed;
      } else if (keys.ArrowRight || keys.d) {
        this.vx = this.speed;
      } else {
        this.vx *= 0.8; // Friction
      }

      this.x += this.vx;

      // Screen Wrapping (Left/Right)
      if (this.x > GAME_WIDTH) this.x = -this.width;
      if (this.x + this.width < 0) this.x = GAME_WIDTH;

      // Calculate dynamic gravity and jump strength based on score
      let speedMultiplier = 1 + Math.min(score / 5000, 2); 
      currentGravity = baseGravity * speedMultiplier;
      this.jumpStrength = this.baseJumpStrength * Math.sqrt(speedMultiplier);

      // Vertical movement & gravity
      this.vy += currentGravity;
      this.y += this.vy;

      // Camera logic: When player reaches top half of screen
      if (this.y < GAME_HEIGHT / 2) {
        let diff = GAME_HEIGHT / 2 - this.y;
        this.y = GAME_HEIGHT / 2; // Lock player in center visually
        score += diff; // Increase score based on distance traveled upwards
        
        // Pan all platforms down
        platforms.forEach(p => p.y += diff);
      }

      // Death condition
      if (this.y > GAME_HEIGHT) {
        gameOver = true;
      }
    }

    draw() {
      drawOtter(this.x, this.y, this.width, this.height);
    }
  }


  const ledgeColors = [
    '#F24C4A', // Red
    '#5BB561', // Green
    '#4E72D7'  // Blue
  ];


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

  let player;
  let platforms = [];

  function init() {
    player = new Player();
    platforms = [];
    score = 0;
    gameOver = false;
    currentGravity = baseGravity;
    
    // Create an initial static platform directly underneath the player
    let startPlatform = new Platform(player.y + 100);
    startPlatform.x = player.x - (startPlatform.width / 2) + (player.width / 2); // Center start platform
    startPlatform.isLeft = true; // doesn't matter, just need a base
    platforms.push(startPlatform);

    // Procedurally generate platforms upwards
    let currentY = player.y + 100;
    for (let i = 1; i < 28; i++) {
      let gap = 40 + Math.random() * 40; // evenly distributed gaps
      currentY -= gap;
      platforms.push(new Platform(currentY));
    }

    if (!gameStarted) {
       // Just draw the initial state behind the start menu without running logic
       drawBackground();
       platforms.forEach(p => p.draw());
       player.draw();
    } else {
       requestAnimationFrame(gameLoop);
    }
  }

  function gameLoop() {
    if (gameOver) {
      // Trigger UI Game Over Screen
      finalScoreText.innerText = Math.floor(score);
      
      let rewardText = "";
      if (score >= 5000) {
          rewardText = "Tier 1 Unlocked:<br>1 Month Free + Exclusive Launch Merch!";
      } else if (score >= 2000) {
          rewardText = "Tier 2 Unlocked:<br>10% off your first 3 months.";
      } else {
          rewardText = "Tier 3 Unlocked:<br>Free Day Pass.";
      }
      rewardTierText.innerHTML = rewardText;

      gameOverScreen.classList.add('visible');
      return; // Stop the loop
    }

    drawBackground();
    
    // Update Score UI
    scoreText.innerText = Math.floor(score);

    player.update();

    // Check collisions and draw platforms
    platforms.forEach(p => {
      p.update();
      p.draw();

      // Collision detection: ONLY if falling down
      if (player.vy > 0 && 
          player.x < p.x + p.width && 
          player.x + player.width > p.x && 
          player.y + player.height > p.y && 
          player.y + player.height < p.y + p.height + player.vy) {
        
        // Bounce!
        player.vy = player.jumpStrength;
        // Snap to top of platform slightly for visual consistency
        player.y = p.y - player.height; 
      }
    });

    // Procedural cleanup: remove off-screen platforms
    while (platforms.length > 0 && platforms[0].y > GAME_HEIGHT) {
      platforms.shift(); // Remove bottom platform
      
      // Generate a new one at the top
      let highestY = platforms[platforms.length - 1].y;
      
      let gap = 40 + Math.random() * 40; 
      platforms.push(new Platform(highestY - gap));
    }

    player.draw();

    requestAnimationFrame(gameLoop);
  }

  // Start the game
  init();
</script>
