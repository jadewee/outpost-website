import re

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'r') as f:
    content = f.read()

# Replace the brace drawing logic
new_brace = """    if (isLeft) {
      // Brace on the left side (wall is left)
      ctx.moveTo(0, height);
      ctx.lineTo(35, height);
      ctx.lineTo(0, height + 35);
    } else {
      // Brace on the right side (wall is right)
      ctx.moveTo(width, height);
      ctx.lineTo(width - 35, height);
      ctx.lineTo(width, height + 35);
    }"""
    
content = re.sub(r"    if \(isLeft\) \{\n      // Brace on the left side \(wall is left\)\n      ctx\.moveTo\(10, height\);\n      ctx\.lineTo\(40, height\);\n      ctx\.lineTo\(10, height \+ 40\);\n    \} else \{\n      // Brace on the right side \(wall is right\)\n      ctx\.moveTo\(width - 10, height\);\n      ctx\.lineTo\(width - 40, height\);\n      ctx\.lineTo\(width - 10, height \+ 40\);\n    \}", new_brace, content)

with open('/Users/jadewee/Desktop/Obrig/obrig-game/challenge.html', 'w') as f:
    f.write(content)
