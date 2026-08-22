import os
import glob
import re

html_files = glob.glob("/Users/jadewee/Desktop/Obrig/outpost-website/*.html")

for path in html_files:
    with open(path, 'r') as file:
        content = file.read()
        
    # Remove .nav-links { display: none; }
    content = re.sub(r'\.nav-links\s*\{\s*display:\s*none;\s*\}', '', content)
    
    with open(path, 'w') as file:
        file.write(content)

print("Removed conflicting display:none from old media queries.")
