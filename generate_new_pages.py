import os
import glob

base_dir = "/Users/jadewee/Desktop/Obrig/outpost-website"
with open(os.path.join(base_dir, 'first-timers.html'), 'r') as f:
    template = f.read()

# Extract top part (up to <main...>)
top_part = template.split('<main class="py-12">')[0]
# Extract bottom part (from </main> onwards)
bottom_part = template.split('</main>')[1]

kids_main = '''<main class="py-12">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <h1 class="text-4xl font-black text-center mb-12">Kids Programs & Birthday Parties</h1>
            
            <div class="grid md:grid-cols-2 gap-12 mb-16">
                <!-- Parties -->
                <div class="bg-white rounded-2xl shadow-lg border-2 border-orange-200 overflow-hidden">
                    <div class="bg-orange-100 p-6">
                        <h2 class="text-2xl font-bold text-orange-800">Birthday Parties 🎈</h2>
                        <p class="text-orange-700">The ultimate climbing birthday experience!</p>
                    </div>
                    <div class="p-8">
                        <table class="w-full text-left border-collapse mb-6">
                            <thead>
                                <tr class="border-b border-gray-200 text-gray-500">
                                    <th class="pb-2">Package Details</th>
                                    <th class="pb-2 text-right">Pricing</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-100">
                                <tr>
                                    <td class="py-3"><span class="font-bold block">Base Package (10 Kids)</span><span class="text-sm text-gray-500">Includes party host & private room</span></td>
                                    <td class="py-3 text-right font-bold text-lg">$450</td>
                                </tr>
                                <tr>
                                    <td class="py-3"><span class="font-bold block">Additional Child</span></td>
                                    <td class="py-3 text-right font-bold">$40/ea</td>
                                </tr>
                            </tbody>
                        </table>
                        <a href="https://wa.me/6512345678" target="_blank" rel="noopener noreferrer" class="block w-full py-3 text-center bg-green-500 text-white font-bold rounded-lg hover:bg-green-600 shadow-md transition-colors">
                            Inquire via WhatsApp
                        </a>
                    </div>
                </div>

                <!-- Programs -->
                <div class="space-y-8">
                    <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100 transition-all hover:shadow-md">
                        <h3 class="text-xl font-bold mb-2">Step-Up! Junior Coaching</h3>
                        <p class="text-gray-600 mb-4">Weekly structured classes designed to build confidence, coordination, and climbing technique in children.</p>
                        <button class="px-4 py-2 bg-blue-100 text-blue-700 font-semibold rounded hover:bg-blue-200 transition-colors">View Schedule</button>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100 transition-all hover:shadow-md">
                        <h3 class="text-xl font-bold mb-2">School Holiday Camps</h3>
                        <p class="text-gray-600 mb-4">Keep them active! Multi-activity combo camps (Climb + Art / Nerf) running every major school holiday.</p>
                        <button class="px-4 py-2 bg-blue-100 text-blue-700 font-semibold rounded hover:bg-blue-200 transition-colors">See Upcoming Camps</button>
                    </div>
                </div>
            </div>
        </div>
    </main>'''

coaching_main = '''<main class="py-12">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <h1 class="text-4xl font-black text-center mb-12">Coaching & Rock Trips</h1>

            <div class="grid md:grid-cols-2 gap-8 mb-16">
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-200 transition-all hover:shadow-md">
                    <h2 class="text-2xl font-bold mb-4">Adult Coaching & SNCS</h2>
                    <p class="text-gray-600 mb-6">From Basics to Advanced, plus official Singapore National Climbing Standards (SNCS) certifications.</p>
                    <ul class="space-y-3 mb-6 text-gray-700 font-medium">
                        <li class="bg-gray-50 p-3 rounded-lg border border-gray-100 flex items-center gap-3"><span class="text-blue-500">✓</span> Basics & Beyond Basics</li>
                        <li class="bg-gray-50 p-3 rounded-lg border border-gray-100 flex items-center gap-3"><span class="text-blue-500">✓</span> SNCS Level 1 (Top Rope)</li>
                        <li class="bg-gray-50 p-3 rounded-lg border border-gray-100 flex items-center gap-3"><span class="text-blue-500">✓</span> SNCS Level 2 (Lead Climbing)</li>
                        <li class="bg-gray-50 p-3 rounded-lg border border-gray-100 flex items-center gap-3"><span class="text-blue-500">✓</span> SNCS Level 3</li>
                    </ul>
                    <button class="w-full py-3 bg-blue-600 text-white font-bold rounded-lg shadow-sm hover:bg-blue-700 transition-colors">View Class Timetable</button>
                </div>
                
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-200 transition-all hover:shadow-md">
                    <h2 class="text-2xl font-bold mb-4">Upcoming Rock Trips 🌍</h2>
                    <p class="text-gray-600 mb-6">Take your skills to real rock! We organize guided outdoor climbing trips across Asia.</p>
                    
                    <div class="space-y-4">
                        <div class="flex justify-between items-center bg-orange-50 p-4 rounded-lg border border-orange-100">
                            <div>
                                <strong class="block text-gray-900">Chiang Mai, Thailand</strong>
                                <span class="text-sm text-gray-500">Jul 24 - 27, 2026</span>
                            </div>
                            <button class="px-4 py-2 bg-white text-orange-600 font-semibold rounded border border-orange-200 shadow-sm hover:bg-orange-100 transition-colors">Details</button>
                        </div>
                        <div class="flex justify-between items-center bg-blue-50 p-4 rounded-lg border border-blue-100">
                            <div>
                                <strong class="block text-gray-900">Ipoh, Malaysia</strong>
                                <span class="text-sm text-gray-500">Sep 10 - 12, 2026</span>
                            </div>
                            <button class="px-4 py-2 bg-white text-blue-600 font-semibold rounded border border-blue-200 shadow-sm hover:bg-blue-100 transition-colors">Details</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>'''

groups_main = '''<main class="py-12">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12">
                <h1 class="text-4xl font-black mb-4">Corporate & Group Events</h1>
                <p class="text-xl text-gray-600 max-w-2xl mx-auto">Build trust, overcome fears, and bond with your team on the wall.</p>
            </div>

            <div class="bg-white rounded-2xl shadow-lg p-8 md:p-12 border border-gray-100">
                <h2 class="text-2xl font-bold mb-6">Team Building Packages</h2>
                <div class="grid md:grid-cols-2 gap-8 mb-8">
                    <div>
                        <h3 class="text-lg font-bold text-blue-600 mb-4">Why Outpost?</h3>
                        <ul class="space-y-3 text-gray-600">
                            <li class="flex items-center gap-2">✓ Dedicated facilitators & customized games</li>
                            <li class="flex items-center gap-2">✓ Private facility rental options</li>
                            <li class="flex items-center gap-2">✓ F&B catering available</li>
                            <li class="flex items-center gap-2">✓ Suitable for all fitness levels</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        <h3 class="font-bold mb-4">Request a Quote</h3>
                        <p class="text-sm text-gray-600 mb-6">Chat with our event concierges directly on WhatsApp to customize your event.</p>
                        <a href="https://wa.me/6512345678" target="_blank" rel="noopener noreferrer" class="block w-full py-3 text-center bg-green-500 text-white font-bold rounded-lg hover:bg-green-600 shadow-md transition-colors">
                            Chat on WhatsApp
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </main>'''


def create_file(filename, main_content, title_tag):
    new_top = top_part.replace('<title>First Timers | Outpost Climbing</title>', title_tag).replace('<title>Outpost Climbing | Singapore\'s Premier Indoor Climbing Community</title>', title_tag)
    # the title might be different depending on which template we used, so just do a regex replace if needed.
    # Actually, the template is from first-timers.html which has <title>Outpost Climbing | ...</title> or something similar.
    import re
    new_top = re.sub(r'<title>.*?</title>', title_tag, new_top)
    
    with open(os.path.join(base_dir, filename), 'w') as f:
        f.write(new_top + main_content + '</main>' + bottom_part)

create_file('kids-and-parties.html', kids_main, '<title>Kids & Parties | Outpost Climbing</title>')
create_file('coaching.html', coaching_main, '<title>Coaching & Trips | Outpost Climbing</title>')
create_file('groups.html', groups_main, '<title>Groups & Corporate | Outpost Climbing</title>')

print("Generated new pages based on the original design.")
