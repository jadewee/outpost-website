import os
import glob

base_dir = "/Users/jadewee/Desktop/Obrig/outpost-website"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

old_select = '''<select style="border:none; outline:none; font-family:'Quicksand', sans-serif; font-weight:700; font-size:16px; color:var(--text-dark); background:transparent; cursor:pointer; -webkit-appearance: none; appearance: none; padding-right: 10px;">
          <option>Outpost HQ (Main)</option>
          <option>Outpost East</option>
          <option>Outpost West</option>
        </select>'''

new_select = '''<select onchange="if(this.value) window.location.href=this.value;" style="border:none; outline:none; font-family:'Quicksand', sans-serif; font-weight:700; font-size:16px; color:var(--text-dark); background:transparent; cursor:pointer; -webkit-appearance: none; appearance: none; padding-right: 10px;">
          <option value="index.html">Outpost Main</option>
          <option value="crawford.html">Crawford Flagship</option>
          <option value="changi.html">Changi Airport T3</option>
          <option value="clementi.html">Clementi Hub</option>
        </select>'''

for fpath in html_files:
    if "challenge.html" in fpath: continue
    with open(fpath, 'r') as f:
        content = f.read()
    
    if old_select in content:
        content = content.replace(old_select, new_select)
        with open(fpath, 'w') as f:
            f.write(content)

print("Updated navigation dropdown.")
