import os

base_dir = "/Users/jadewee/Desktop/Obrig/outpost-website"
index_path = os.path.join(base_dir, 'index.html')

with open(index_path, 'r') as f:
    content = f.read()

locations_html = '''
  <!-- Locations Gateway -->
  <section class="section" style="background: rgba(146, 199, 215, 0.2); border-radius: 40px; margin-bottom: 60px; max-width: 1100px;">
    <h2 class="section-title" style="margin-bottom: 20px;">Explore Our Locations</h2>
    <p style="font-size: 20px; color: #666; max-width: 600px; margin: 0 auto 50px auto; font-weight: 500;">We have 3 awesome locations across Singapore. Find the one that fits your vibe!</p>
    
    <div class="features-grid">
      <!-- Crawford -->
      <a href="crawford.html" style="text-decoration: none; color: inherit; display: block;">
        <div class="feature-card" style="height: 100%; border: 4px solid var(--blue);">
          <div class="feature-icon" style="background: var(--blue); color: white;">🏢</div>
          <h3>Crawford Flagship</h3>
          <p style="color: var(--blue); font-weight: 800; margin-bottom: 10px;">Level 1 Fun Zone + Level 3 Climb Zone</p>
          <p>The full experience with thematic lanes, lead walls, and AR bouldering.</p>
        </div>
      </a>

      <!-- Changi -->
      <a href="changi.html" style="text-decoration: none; color: inherit; display: block;">
        <div class="feature-card" style="height: 100%; border: 4px solid var(--orange);">
          <div class="feature-icon" style="background: var(--orange); color: white;">✈️</div>
          <h3>Changi Airport T3</h3>
          <p style="color: var(--orange); font-weight: 800; margin-bottom: 10px;">Family & Kids Hub</p>
          <p>The ultimate family day-out with kids' intro sessions and epic birthday parties.</p>
        </div>
      </a>

      <!-- Clementi -->
      <a href="clementi.html" style="text-decoration: none; color: inherit; display: block;">
        <div class="feature-card" style="height: 100%; border: 4px solid var(--green);">
          <div class="feature-icon" style="background: var(--green); color: white;">🧗‍♂️</div>
          <h3>Clementi</h3>
          <p style="color: var(--green); font-weight: 800; margin-bottom: 10px;">Bouldering & Youth Combo</p>
          <p>Community bouldering cave with dynamic weekly resets and youth coaching.</p>
        </div>
      </a>
    </div>
  </section>
'''

# Insert after game-banner
target = '  </div>\n\n  <!-- Features Section -->'
if target in content:
    new_content = content.replace('  <!-- Features Section -->', locations_html + '\n  <!-- Features Section -->')
    with open(index_path, 'w') as f:
        f.write(new_content)
    print("Locations section added.")
else:
    print("Could not find insertion point.")
