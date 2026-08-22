import os
import glob

base_dir = "/Users/jadewee/Desktop/Obrig/outpost-website"

with open(os.path.join(base_dir, 'index.html'), 'r') as f:
    index_content = f.read()

# Extract everything before <!-- Hero Section -->
top_part = index_content.split('<!-- Hero Section -->')[0]

# Extract everything from <!-- Footer --> to the end
footer_part = "  <!-- Footer -->" + index_content.split('<!-- Footer -->')[1]

# We need to build the content for Crawford, Changi, and Clementi using the existing CSS classes:
# .hero, .hero h1, .hero p, .hero-buttons, .wave, .section, .section-title, .features-grid, .feature-card, .feature-icon

crawford_content = '''
  <!-- Hero Section -->
  <section class="hero" style="background-color: var(--blue);">
    <h1>Crawford Flagship</h1>
    <p>The Full Experience. Two levels of climbing action for all ages and skill levels.</p>
    <div class="hero-buttons">
      <a href="#" class="btn">Book @ Crawford (Level 1 or Level 3)</a>
    </div>

    <!-- Wavy bottom edge -->
    <div class="wave">
      <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V120H0V95.8C59.71,118.08,130.83,119.3,196.36,99.51,241.65,85.83,283.47,63.45,321.39,56.44Z" class="shape-fill"></path>
      </svg>
    </div>
  </section>

  <section class="section">
    <h2 class="section-title">Dual-Zone Selector</h2>
    <div class="features-grid" style="grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));">
      <!-- Zone 1 -->
      <div class="feature-card">
        <div class="feature-icon" style="background: var(--yellow);">🎡</div>
        <h3>Zone 1: Level 1 Fun Zone</h3>
        <p>30 thematic high wall lanes (min age 4 y/o, 15kg) & AR bouldering walls. Enjoy 1.5-hr timed slots (Guided vs Unguided).</p>
      </div>

      <!-- Zone 2 -->
      <div class="feature-card">
        <div class="feature-icon" style="background: var(--purple); color: white;">🧗‍♂️</div>
        <h3>Zone 2: Level 3 Climb Zone</h3>
        <p>40+ high wall lanes, dedicated bouldering cave, lead climbing routes, and adult coaching.</p>
      </div>
    </div>
  </section>

  <section class="section" style="background: var(--bg-light); padding-top: 20px;">
    <h2 class="section-title" style="color: var(--text-dark);">Featured Offerings</h2>
    <div class="features-grid">
      <div class="feature-card">
        <div class="feature-icon" style="background: var(--green);">🎓</div>
        <h3>SNCS Certification</h3>
        <p>Official Level 1-3 certification.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon" style="background: var(--blue);">📚</div>
        <h3>Outpost Basics</h3>
        <p>Basics & Beyond Basics workshops.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon" style="background: var(--orange);">💪</div>
        <h3>Adult Climb Squad</h3>
        <p>Join the community and train together.</p>
      </div>
    </div>
  </section>
'''

changi_content = '''
  <!-- Hero Section -->
  <section class="hero" style="background-color: var(--orange);">
    <h1>Changi Airport T3</h1>
    <p>Playful, family-oriented, and vibrant. The ultimate fun-first climbing and party venue.</p>
    <div class="hero-buttons">
      <a href="#" class="btn blue">Book Family Session @ T3</a>
    </div>

    <!-- Wavy bottom edge -->
    <div class="wave">
      <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V120H0V95.8C59.71,118.08,130.83,119.3,196.36,99.51,241.65,85.83,283.47,63.45,321.39,56.44Z" class="shape-fill"></path>
      </svg>
    </div>
  </section>

  <section class="section">
    <h2 class="section-title">Family & Kids Hub</h2>
    <div class="features-grid">
      <div class="feature-card">
        <div class="feature-icon" style="background: var(--yellow);">👨‍👩‍👧‍👦</div>
        <h3>Family Day-Outs</h3>
        <p>Kids' intro sessions and special weekend passes for the whole family.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon" style="background: var(--green);">🎈</div>
        <h3>Birthday Parties</h3>
        <p>All-inclusive packages with a private function room and a dedicated party host.</p>
      </div>
    </div>
  </section>

  <section class="section" style="background: rgba(146, 199, 215, 0.2); border-radius: 40px;">
    <h2 class="section-title" style="margin-bottom: 20px;">Holiday Camps</h2>
    <p style="font-size: 20px; color: #666; max-width: 600px; margin: 0 auto 40px auto; font-weight: 500;">Keep the kids active with our "StepUp! Crash Course" and multi-activity camps featuring Climb & Nerf / Art combos!</p>
    <a href="#" class="btn blue" style="font-size: 20px; padding: 15px 40px; border-radius: 30px; display: inline-block;">See Upcoming Camps</a>
  </section>
'''

clementi_content = '''
  <!-- Hero Section -->
  <section class="hero" style="background-color: var(--green);">
    <h1>Clementi Hub</h1>
    <p>Modern, community-focused, and accessible. Your pure bouldering and youth coaching hub.</p>
    <div class="hero-buttons">
      <a href="#" class="btn">Book @ Clementi</a>
    </div>

    <!-- Wavy bottom edge -->
    <div class="wave">
      <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V120H0V95.8C59.71,118.08,130.83,119.3,196.36,99.51,241.65,85.83,283.47,63.45,321.39,56.44Z" class="shape-fill"></path>
      </svg>
    </div>
  </section>

  <!-- Game Banner modified for Universal Credits -->
  <div class="game-banner" style="background: linear-gradient(135deg, var(--purple) 0%, #a8a0e8 100%); margin-top: -30px; margin-bottom: 60px;">
    <div class="game-banner-content">
      <h2 style="color: white; text-shadow: none;">Universal Credits</h2>
      <p style="color: white;">Redeem your Outpost Credits seamlessly at Clementi for day passes and classes.</p>
      <a href="#" class="btn" style="background: white; color: var(--purple);">Learn More</a>
    </div>
    <div class="game-mascot" style="font-size: 100px; transform: none; animation: none;">💳</div>
  </div>

  <section class="section" style="padding-top: 0;">
    <h2 class="section-title">Featured Offerings</h2>
    <div class="features-grid">
      <div class="feature-card">
        <div class="feature-icon" style="background: var(--blue);">🧱</div>
        <h3>Dedicated Bouldering Cave</h3>
        <p>Experience dynamic weekly resets to keep the challenges fresh.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon" style="background: var(--yellow);">👥</div>
        <h3>Side-by-Side Coaching</h3>
        <p>Adult bouldering and youth coaching happening simultaneously for the community.</p>
      </div>
    </div>
  </section>
'''

def write_microsite(filename, content_block, title_text):
    new_top = top_part.replace('<title>Outpost Climbing</title>', f'<title>{title_text} | Outpost Climbing</title>')
    full_html = new_top + content_block + footer_part
    with open(os.path.join(base_dir, filename), 'w') as f:
        f.write(full_html)

write_microsite('crawford.html', crawford_content, "Crawford Flagship")
write_microsite('changi.html', changi_content, "Changi Airport T3")
write_microsite('clementi.html', clementi_content, "Clementi Hub")

print("Created 3 microsites using the original design.")
