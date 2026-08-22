import os
import glob

base_dir = "/Users/jadewee/Desktop/Obrig/outpost-website"
microsites = ['crawford.html', 'changi.html', 'clementi.html']

iframe_html = '''
  <!-- Timetable Widget Section -->
  <section class="section" id="timetable" style="padding-top: 40px; padding-bottom: 80px;">
    <h2 class="section-title">Live Timetable</h2>
    <div style="max-width: 1100px; margin: 0 auto; background: white; border-radius: 35px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.06); padding: 20px; border: 4px solid var(--blue);">
      <!-- REPLACE THE SRC ATTRIBUTE BELOW WITH YOUR ACTUAL REZERV IFRAME URL -->
      <iframe src="https://example.rezerv.co/widget" width="100%" height="600" frameborder="0" style="border:0; border-radius: 20px;" allowfullscreen></iframe>
    </div>
  </section>
'''

for site in microsites:
    path = os.path.join(base_dir, site)
    with open(path, 'r') as f:
        content = f.read()
    
    # We'll customize the border color based on the site for consistency
    site_html = iframe_html
    if site == 'changi.html':
        site_html = site_html.replace('var(--blue)', 'var(--orange)')
    elif site == 'clementi.html':
        site_html = site_html.replace('var(--blue)', 'var(--green)')
        
    if '<!-- Timetable Widget Section -->' not in content:
        new_content = content.replace('  <!-- Footer -->', site_html + '\n  <!-- Footer -->')
        with open(path, 'w') as f:
            f.write(new_content)

print("Timetable placeholders added.")
