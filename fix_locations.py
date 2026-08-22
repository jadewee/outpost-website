import re

filepath = "/Users/jadewee/Desktop/Obrig/outpost-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

new_locations = """    <h2 class="section-title" style="margin-bottom: 20px;">Explore Our Locations</h2>
    <p style="font-size: 20px; color: #666; max-width: 600px; margin: 0 auto 50px auto; font-weight: 600;">We have 3 awesome locations across Singapore. Find the one that fits your vibe!</p>
    
    <div class="features-grid">
      <!-- Crawford -->
      <a href="crawford.html" style="text-decoration: none; color: inherit; display: block; height: 100%;">
        <div class="feature-card" style="height: 100%; border: 4px solid transparent; background: rgba(146, 199, 215, 0.15); border-radius: 40px; transition: all 0.3s; padding: 50px 30px;">
          <div class="feature-icon" style="background: var(--blue); color: white; box-shadow: 0 8px 15px rgba(146,199,215,0.4);">📍</div>
          <h3 style="font-size: 32px; color: var(--blue);">Crawford Flagship</h3>
          <p style="color: var(--blue); font-weight: 800; font-size: 18px; margin-bottom: 15px;">Level 1 Fun + Level 3 Climb</p>
          <p style="color: #555; font-weight: 600; line-height: 1.6; margin-bottom: 30px;">The full experience with thematic lanes, lead walls, and AR bouldering.</p>
          <span class="btn blue" style="padding: 10px 25px; font-size: 16px;">Explore Crawford</span>
        </div>
      </a>

      <!-- Changi -->
      <a href="changi.html" style="text-decoration: none; color: inherit; display: block; height: 100%;">
        <div class="feature-card" style="height: 100%; border: 4px solid transparent; background: rgba(243, 195, 122, 0.15); border-radius: 40px; transition: all 0.3s; padding: 50px 30px;">
          <div class="feature-icon" style="background: var(--orange); color: white; box-shadow: 0 8px 15px rgba(243,195,122,0.4);">✈️</div>
          <h3 style="font-size: 32px; color: var(--orange);">Changi Airport T3</h3>
          <p style="color: var(--orange); font-weight: 800; font-size: 18px; margin-bottom: 15px;">Family & Kids Hub</p>
          <p style="color: #555; font-weight: 600; line-height: 1.6; margin-bottom: 30px;">The ultimate family day-out with kids' intro sessions and epic birthday parties.</p>
          <span class="btn" style="padding: 10px 25px; font-size: 16px;">Explore Changi</span>
        </div>
      </a>

      <!-- Clementi -->
      <a href="clementi.html" style="text-decoration: none; color: inherit; display: block; height: 100%;">
        <div class="feature-card" style="height: 100%; border: 4px solid transparent; background: rgba(76, 106, 95, 0.1); border-radius: 40px; transition: all 0.3s; padding: 50px 30px;">
          <div class="feature-icon" style="background: var(--green); color: white; box-shadow: 0 8px 15px rgba(76,106,95,0.4);">🧗‍♂️</div>
          <h3 style="font-size: 32px; color: var(--green);">Clementi Hub</h3>
          <p style="color: var(--green); font-weight: 800; font-size: 18px; margin-bottom: 15px;">Bouldering & Youth Combo</p>
          <p style="color: #555; font-weight: 600; line-height: 1.6; margin-bottom: 30px;">Community bouldering cave with dynamic weekly resets and youth coaching.</p>
          <span class="btn green" style="padding: 10px 25px; font-size: 16px;">Explore Clementi</span>
        </div>
      </a>
    </div>"""

# Find the start and end of the old block and replace
pattern = r'<h2 class="section-title" style="margin-bottom: 20px;">Explore Our Locations</h2>.*?</a>\s*</div>'
content = re.sub(pattern, new_locations, content, flags=re.DOTALL)

with open(filepath, 'w') as f:
    f.write(content)
print("Updated locations section in index.html")
