import re

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'r') as f:
    content = f.read()

# Update game-container CSS
old_css = """  .game-container {
    position: relative;
    width: 400px;
    height: 600px;
    border-radius: 16px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.8);
    background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
  }

  canvas {
    border-radius: 16px;
  }"""

new_css = """  .game-container {
    position: relative;
    width: 100%;
    max-width: 400px;
    aspect-ratio: 2 / 3;
    border-radius: 16px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.8);
    background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
    overflow: hidden;
    touch-action: none; /* Prevent scrolling when tapping game */
  }

  canvas {
    border-radius: 16px;
    width: 100% !important;
    height: 100% !important;
    object-fit: cover;
  }"""
content = content.replace(old_css, new_css)

# Update instructions text
content = content.replace("<p>🕹️ Use Left/Right Arrows or A/D</p>", "<p>🕹️ Left/Right Arrows or Tap Sides of Screen</p>")

# Add touch listeners to the Javascript
touch_script = """
  // Touch Controls for Mobile
  const gameContainer = document.querySelector('.game-container');
  
  function handleTouch(e) {
    e.preventDefault(); // Prevent scrolling
    
    // Reset keys
    keys.ArrowLeft = false;
    keys.ArrowRight = false;

    if (e.touches.length > 0) {
      // Get the first active touch
      let touch = e.touches[0];
      let rect = gameContainer.getBoundingClientRect();
      let x = touch.clientX - rect.left; // x position within the element
      
      // If tapped on the left half
      if (x < rect.width / 2) {
        keys.ArrowLeft = true;
      } else {
        keys.ArrowRight = true;
      }
    }
  }

  gameContainer.addEventListener('touchstart', handleTouch, { passive: false });
  gameContainer.addEventListener('touchmove', handleTouch, { passive: false });
  gameContainer.addEventListener('touchend', (e) => {
    e.preventDefault();
    if (e.touches.length === 0) {
      keys.ArrowLeft = false;
      keys.ArrowRight = false;
    } else {
      handleTouch(e);
    }
  }, { passive: false });
  gameContainer.addEventListener('touchcancel', (e) => {
    keys.ArrowLeft = false;
    keys.ArrowRight = false;
  });

  // UI Restart Button listener
"""

content = content.replace("  // UI Restart Button listener", touch_script)

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'w') as f:
    f.write(content)
