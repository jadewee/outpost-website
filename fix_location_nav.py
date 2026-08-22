import os
import glob

html_files = glob.glob("/Users/jadewee/Desktop/Obrig/outpost-website/*.html")

for path in html_files:
    with open(path, 'r') as file:
        content = file.read()
        
    # Remove the background and border-radius from the location selector div
    old_style = "display: flex; align-items: center; gap: 5px; background: rgba(146, 199, 215, 0.2); padding: 8px 15px; border-radius: 20px;"
    new_style = "display: flex; align-items: center; gap: 5px; padding: 8px 15px;"
    
    if old_style in content:
        content = content.replace(old_style, new_style)
        with open(path, 'w') as file:
            file.write(content)

print("Removed location nav background.")
