import re

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'r') as f:
    content = f.read()

content = content.replace("ctx.roundRect(0, 0, width, height, height/2);", "ctx.roundRect(0, 0, width, height, 7);")
content = content.replace("ctx.roundRect(0, 0, width, height/2, height/2);", "ctx.roundRect(0, 0, width, height/2, 3);")

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'w') as f:
    f.write(content)
