import os
import glob
import re

html_files = glob.glob("/Users/jadewee/Desktop/Obrig/outpost-website/*.html")

for path in html_files:
    with open(path, 'r') as file:
        content = file.read()
        
    # Replace the old mobile nav-links css block
    old_css_pattern = r'\.nav-links \{\s*position: absolute; top: 100%;.*?box-sizing: border-box;\s*\}'
    new_css = """.nav-links {
        position: absolute; top: 100%; left: 0; width: 100%;
        background: white; flex-direction: column;
        align-items: flex-start !important; padding: 20px 5% 40px 5% !important; gap: 0 !important;
        box-shadow: 0 15px 20px rgba(0,0,0,0.1); box-sizing: border-box;
        opacity: 0; visibility: hidden; pointer-events: none;
        transform: translateY(-10px);
        transition: all 0.3s ease;
        z-index: 99;
      }"""
      
    content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)
    
    # Replace the old .nav-links.active
    old_active_pattern = r'\.nav-links\.active \{\s*max-height: 100vh;.*?overflow-y: auto;\s*\}'
    new_active = """.nav-links.active {
        opacity: 1; visibility: visible; pointer-events: auto;
        transform: translateY(0);
      }"""
      
    content = re.sub(old_active_pattern, new_active, content, flags=re.DOTALL)
    
    with open(path, 'w') as file:
        file.write(content)

print("Hamburger menu CSS updated to use opacity/visibility.")
