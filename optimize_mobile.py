import os
import glob

html_files = glob.glob("/Users/jadewee/Desktop/Obrig/outpost-website/*.html")

mobile_css = """
    /* Mobile Responsive */
    .hamburger { display: none; font-size: 30px; background: none; border: none; cursor: pointer; color: var(--purple); }
    @media (max-width: 1100px) {
      .hamburger { display: block; }
      .nav-links {
        position: absolute; top: 100%; left: 0; width: 100%; max-height: 0;
        overflow: hidden; background: white; flex-direction: column;
        align-items: flex-start !important; padding: 0 5%; gap: 0 !important;
        transition: max-height 0.4s ease, padding 0.4s ease;
        box-shadow: 0 15px 20px rgba(0,0,0,0.1); box-sizing: border-box;
      }
      .nav-links.active { max-height: 100vh; padding: 20px 5% 40px 5%; overflow-y: auto; }
      .nav-links > div { width: 100%; margin-bottom: 15px; box-sizing: border-box; }
      .nav-links > div select { width: 100%; }
      .nav-links a:not(.btn) { width: 100%; padding: 15px 0; border-bottom: 1px solid #eee; display: block; }
      .nav-links .btn { width: 100%; margin-top: 20px; box-sizing: border-box; }
      
      /* Make sure feature cards scale properly */
      .hero { padding: 80px 20px 100px 20px; }
      .hero h1 { font-size: clamp(35px, 10vw, 50px); }
      .section-title { font-size: 35px; }
    }
"""

hamburger_btn = '''
    <button class="hamburger" onclick="document.querySelector('.nav-links').classList.toggle('active')">☰</button>
    <div class="nav-links">'''

for path in html_files:
    with open(path, 'r') as file:
        content = file.read()
        
    # Inject Hamburger button if not present
    if 'class="hamburger"' not in content:
        content = content.replace('<div class="nav-links">', hamburger_btn)
        
    # Inject Mobile CSS if not present
    if '/* Mobile Responsive */' not in content:
        content = content.replace('</style>', mobile_css + '</style>')
        
    with open(path, 'w') as file:
        file.write(content)

print("Mobile optimization applied.")
