import os
import glob
import re

base_dir = "/Users/jadewee/Desktop/Obrig/outpost-website"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

old_nav_desktop = '''<nav class="hidden md:flex ml-6 space-x-4">
                        <a href="first-timer.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">First Timers</a>
                        <a href="#" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">Programs & Camps</a>
                        <a href="#" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">Certification (SNCS)</a>
                        <a href="packages.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">Packages & Credits</a>
                        <a href="#" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">Parties</a>
                    </nav>'''

new_nav_desktop = '''<nav class="hidden md:flex ml-6 space-x-4">
                        <a href="first-timers.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">First Timers</a>
                        <a href="kids-and-parties.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">Kids & Parties</a>
                        <a href="coaching.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">Coaching & Trips</a>
                        <a href="groups.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">Groups</a>
                        <a href="pricing.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">Pricing</a>
                    </nav>'''

old_nav_mobile = '''<a href="index.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-900 bg-gray-50">Outpost Main (Global)</a>
                <a href="crawford.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Crawford Flagship</a>
                <a href="changi.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Changi T3</a>
                <a href="clementi.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Clementi</a>
                <div class="border-t border-gray-200 my-2"></div>
                <a href="first-timer.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">First Timers</a>
                <a href="packages.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Packages & Credits</a>'''

new_nav_mobile = '''<a href="index.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-900 bg-gray-50">Home</a>
                <a href="first-timers.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">First Timers</a>
                <a href="kids-and-parties.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Kids & Parties</a>
                <a href="coaching.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Coaching & Trips</a>
                <a href="groups.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Groups</a>
                <a href="pricing.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Pricing</a>
                <div class="border-t border-gray-200 my-2"></div>
                <div class="px-3 py-2 text-sm font-bold text-gray-500 uppercase">Locations</div>
                <a href="crawford.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Crawford Flagship</a>
                <a href="changi.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Changi T3</a>
                <a href="clementi.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Clementi</a>'''

for fpath in html_files:
    if "challenge.html" in fpath: continue
    with open(fpath, 'r') as f:
        content = f.read()
    
    # Replace desktop nav
    content = content.replace(old_nav_desktop, new_nav_desktop)
    # Replace mobile nav (this uses re because the whitespace might vary)
    content = re.sub(
        r'<a href="index.html".*?Packages & Credits</a>',
        new_nav_mobile,
        content,
        flags=re.DOTALL
    )

    with open(fpath, 'w') as f:
        f.write(content)

# Rename files
if os.path.exists(os.path.join(base_dir, 'first-timer.html')):
    os.rename(os.path.join(base_dir, 'first-timer.html'), os.path.join(base_dir, 'first-timers.html'))
if os.path.exists(os.path.join(base_dir, 'packages.html')):
    os.rename(os.path.join(base_dir, 'packages.html'), os.path.join(base_dir, 'pricing.html'))

print("Updated navigation and renamed files.")
