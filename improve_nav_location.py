import glob

html_files = glob.glob("/Users/jadewee/Desktop/Obrig/outpost-website/*.html")

old_snippet = """<div style="display: flex; align-items: center; gap: 5px; padding: 8px 15px;">
        <span style="font-size: 18px;">📍</span>
        <select onchange="if(this.value) window.location.href=this.value;" style="border:none; outline:none; font-family:'Quicksand', sans-serif; font-weight:700; font-size:16px; color:var(--text-dark); background:transparent; cursor:pointer; -webkit-appearance: none; appearance: none; padding-right: 10px;">"""

# Maybe the user's files have slightly different whitespace, let's use a regex replace.
import re

for path in html_files:
    with open(path, 'r') as file:
        content = file.read()
        
    # We want to replace the div style and the select style.
    # The div currently has: `style="display: flex; align-items: center; gap: 5px; padding: 8px 15px;"`
    
    new_div_style = 'style="display: flex; align-items: center; gap: 8px; padding: 8px 20px; border: 2px solid #eaeaea; border-radius: 30px; background: white; box-shadow: 0 4px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;"'
    new_select_style = 'style="border:none; outline:none; font-family:\'Quicksand\', sans-serif; font-weight:700; font-size:16px; color:var(--text-dark); background:transparent; cursor:pointer; -webkit-appearance: none; appearance: none; padding-right: 5px;"'
    
    # Regex to match the div
    content = re.sub(
        r'<div style="display: flex; align-items: center; gap: 5px; padding: 8px 15px;">',
        f'<div {new_div_style} onmouseover="this.style.borderColor=\'var(--orange)\'" onmouseout="this.style.borderColor=\'#eaeaea\'">',
        content
    )
    
    # Regex to match the select
    content = re.sub(
        r'<select onchange="if\(this\.value\) window\.location\.href=this\.value;" style="border:none; outline:none; font-family:\'Quicksand\', sans-serif; font-weight:700; font-size:16px; color:var\(--text-dark\); background:transparent; cursor:pointer; -webkit-appearance: none; appearance: none; padding-right: 10px;">',
        f'<select onchange="if(this.value) window.location.href=this.value;" {new_select_style}>',
        content
    )
    
    with open(path, 'w') as file:
        file.write(content)

print("Updated nav location selector UI.")
