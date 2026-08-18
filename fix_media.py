import re

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'r') as f:
    content = f.read()

media_block = """  /* Responsive fixes */
  @media (max-width: 450px) {
    .game-container {
      transform: scale(0.85);
      transform-origin: top center;
      margin-bottom: -90px;
    }
  }"""
  
content = content.replace(media_block, "")

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'w') as f:
    f.write(content)
