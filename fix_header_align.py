import os
import glob
import re

html_files = glob.glob("/Users/jadewee/Desktop/Obrig/outpost-website/*.html")

for path in html_files:
    with open(path, 'r') as file:
        content = file.read()
        
    # Standardize the nav-links CSS format first if it's minified
    content = re.sub(r'\.nav-links\s*\{\s*display:\s*flex;\s*gap:\s*\d+px;\s*align-items:\s*center;\s*\}', 
                     '.nav-links { display: flex; gap: 30px; align-items: center; }', content)
                     
    content = re.sub(r'\.nav-links\s*a\s*\{\s*font-weight:\s*700;\s*font-size:\s*\d+px;\s*color:\s*var\(--text-dark\);\s*transition:\s*color\s*0\.2s;\s*\}', 
                     '.nav-links a { font-weight: 700; font-size: 18px; color: var(--text-dark); transition: color 0.2s; }', content)

    # Some files might have it un-minified:
    #     .nav-links {
    #       display: flex;
    #       gap: 30px;
    #       align-items: center;
    #     }
    # It won't match the regex, but those are already correct from index.html!
    
    with open(path, 'w') as file:
        file.write(content)

print("Header aligned across all pages.")
