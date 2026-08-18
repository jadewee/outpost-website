import re

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'r') as f:
    content = f.read()

new_screw = """    if (isLeft) {
      ctx.arc(15, height/2, 2.5, 0, Math.PI*2);
    } else {
      ctx.arc(width - 15, height/2, 2.5, 0, Math.PI*2);
    }"""
    
content = re.sub(r"    if \(isLeft\) \{\n      ctx\.arc\(width - 15, height/2, 2\.5, 0, Math\.PI\*2\);\n    \} else \{\n      ctx\.arc\(15, height/2, 2\.5, 0, Math\.PI\*2\);\n    \}", new_screw, content)

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'w') as f:
    f.write(content)
