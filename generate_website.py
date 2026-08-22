import os

base_dir = "/Users/jadewee/Desktop/Obrig/outpost-website"

# Tailwind script with SRI
tailwind_script = '<script src="https://cdn.tailwindcss.com/3.4.1" integrity="sha384-SOMLQz+nKv/ORIYXo3J3NrWJ33oBgGvkHlV9t8i70QVLq8ZtST9Np1gDsVUkk4xN" crossorigin="anonymous"></script>'

# Note on Tailwind: In production, do not use the CDN. Use npm to install Tailwind and build a static CSS file to avoid needing style-src 'unsafe-inline'.
csp_meta = '''
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' https://cdn.tailwindcss.com 'sha384-SOMLQz+nKv/ORIYXo3J3NrWJ33oBgGvkHlV9t8i70QVLq8ZtST9Np1gDsVUkk4xN'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://dummyimage.com; connect-src 'self'; frame-ancestors 'none';">
    <meta http-equiv="X-Frame-Options" content="DENY">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
'''

# Common header component
header = f'''
    <!-- Global Navigation -->
    <header class="sticky top-0 z-50 bg-white border-b border-gray-200 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <div class="flex items-center">
                    <a href="index.html" class="flex-shrink-0 flex items-center gap-2">
                        <!-- We use an img if they had one, otherwise text -->
                        <span class="font-black text-2xl tracking-tighter text-blue-900">OUTPOST</span>
                    </a>
                    
                    <!-- Location Selector Dropdown -->
                    <div class="relative ml-8 group">
                        <button class="inline-flex items-center px-3 py-2 text-sm font-medium text-gray-700 hover:text-blue-600 focus:outline-none">
                            Locations
                            <svg class="ml-1 h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
                        </button>
                        <div class="absolute left-0 mt-0 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 hidden group-hover:block transition-all z-50">
                            <div class="py-1" role="menu">
                                <a href="index.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 font-bold border-b">Outpost Main (Global)</a>
                                <a href="crawford.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Crawford Flagship</a>
                                <a href="changi.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Changi Airport T3</a>
                                <a href="clementi.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Clementi Hub</a>
                            </div>
                        </div>
                    </div>

                    <!-- Navigation Links -->
                    <nav class="hidden md:flex ml-6 space-x-4">
                        <a href="first-timer.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">First Timers</a>
                        <a href="#" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">Programs & Camps</a>
                        <a href="#" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">Certification (SNCS)</a>
                        <a href="packages.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">Packages & Credits</a>
                        <a href="#" class="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium">Parties</a>
                    </nav>
                </div>
                <div class="flex items-center space-x-3">
                    <button id="signWaiverBtn" class="hidden sm:inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-blue-700 bg-blue-100 hover:bg-blue-200">
                        Sign Waiver
                    </button>
                    <button id="bookClimbBtn" class="inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 shadow-sm">
                        Book a Climb (Rezerv)
                    </button>
                    <!-- Mobile menu button -->
                    <div class="md:hidden flex items-center">
                        <button id="mobileMenuBtn" class="text-gray-500 hover:text-gray-700 focus:outline-none">
                            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Mobile Navigation Drawer -->
        <div id="mobileMenu" class="hidden md:hidden border-t border-gray-200 bg-white">
            <div class="px-2 pt-2 pb-3 space-y-1">
                <a href="index.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-900 bg-gray-50">Home</a>
                <a href="crawford.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Crawford Flagship</a>
                <a href="changi.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Changi T3</a>
                <a href="clementi.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Clementi</a>
                <div class="border-t border-gray-200 my-2"></div>
                <a href="first-timer.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">First Timers</a>
                <a href="packages.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">Packages & Credits</a>
                <button class="w-full text-left mt-2 block px-3 py-2 rounded-md text-base font-medium text-blue-700 bg-blue-50">Sign Waiver</button>
            </div>
        </div>
    </header>

    <!-- Global Modal UI (Used for secure user interaction instead of alerts) -->
    <div id="globalModal" class="fixed inset-0 z-[100] hidden" aria-labelledby="modal-title" role="dialog" aria-modal="true">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
        <div class="fixed inset-0 z-10 overflow-y-auto">
            <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
                <div class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm sm:p-6">
                    <div>
                        <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-blue-100">
                            <svg class="h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" />
                            </svg>
                        </div>
                        <div class="mt-3 text-center sm:mt-5">
                            <h3 class="text-base font-semibold leading-6 text-gray-900" id="modalTitle">Information</h3>
                            <div class="mt-2">
                                <p class="text-sm text-gray-500" id="modalMessage">Message body here.</p>
                            </div>
                        </div>
                    </div>
                    <div class="mt-5 sm:mt-6">
                        <button type="button" id="closeModalBtn" class="inline-flex w-full justify-center rounded-md bg-blue-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600">Got it, thanks!</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
'''

common_js = '''
    <script>
        // Use textContent to set dynamic strings safely.
        function showModal(title, message) {
            const modal = document.getElementById('globalModal');
            document.getElementById('modalTitle').textContent = title;
            document.getElementById('modalMessage').textContent = message;
            modal.classList.remove('hidden');
        }

        document.getElementById('closeModalBtn').addEventListener('click', () => {
            document.getElementById('globalModal').classList.add('hidden');
        });

        // Mobile menu toggle
        document.getElementById('mobileMenuBtn').addEventListener('click', () => {
            const menu = document.getElementById('mobileMenu');
            if (menu.classList.contains('hidden')) {
                menu.classList.remove('hidden');
            } else {
                menu.classList.add('hidden');
            }
        });

        // Mock integration for Rezerv and Waiver buttons
        document.getElementById('signWaiverBtn').addEventListener('click', () => {
            showModal('Sign Waiver', 'Redirecting to secure external waiver signing portal...');
        });
        document.getElementById('bookClimbBtn').addEventListener('click', () => {
            showModal('Rezerv Integration', 'Opening Rezerv booking modal/portal...');
        });
    </script>
'''

# 1. index.html
index_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Outpost Climbing | Singapore's Premier Indoor Climbing Community</title>
    {csp_meta}
    {tailwind_script}
</head>
<body class="bg-gray-50 font-sans antialiased text-gray-900">
    {header}

    <main>
        <!-- Hero Section -->
        <section class="bg-blue-900 text-white py-20 relative overflow-hidden">
            <div class="absolute inset-0 opacity-20 bg-[url('https://dummyimage.com/1920x1080/000/fff&text=Climbing+Background')] bg-cover bg-center"></div>
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
                <h1 class="text-4xl md:text-6xl font-black mb-6 tracking-tight">Where It Begins &bull; Where It Matters &bull; Where The People Are</h1>
                <p class="text-xl md:text-2xl font-light mb-10 max-w-3xl mx-auto text-blue-100">Singapore's premier indoor climbing community across Crawford, Changi T3, and Clementi.</p>
                <div class="flex flex-col sm:flex-row justify-center gap-4">
                    <a href="first-timer.html" class="px-8 py-4 bg-white text-blue-900 font-bold rounded-lg hover:bg-gray-100 transition shadow-lg">First Time Here?</a>
                    <a href="#locations" class="px-8 py-4 bg-blue-700 text-white font-bold rounded-lg border border-blue-500 hover:bg-blue-600 transition shadow-lg">Explore Locations</a>
                </div>
            </div>
        </section>

        <!-- Gamified Lead Gen Banner -->
        <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-8 relative z-20">
            <div class="bg-gradient-to-r from-teal-400 to-blue-500 rounded-xl shadow-xl overflow-hidden flex flex-col md:flex-row items-center justify-between p-6 md:p-8 text-white">
                <div class="mb-4 md:mb-0">
                    <h2 class="text-2xl font-bold mb-2 flex items-center gap-2">🧗 Take the Outpost Challenge!</h2>
                    <p class="text-teal-50">Play our Otter Jump mini-game to unlock free day passes, starter discounts, and founding member merch.</p>
                </div>
                <a href="challenge.html" class="shrink-0 px-6 py-3 bg-white text-blue-600 font-bold rounded-full shadow-md hover:scale-105 transition transform">Play Mini-Game 🎮</a>
            </div>
        </section>

        <!-- Location Finder Gateway -->
        <section id="locations" class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold text-center mb-12 text-gray-900">Choose Your Outpost</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <!-- Crawford -->
                <a href="crawford.html" class="group block rounded-2xl bg-white shadow-sm hover:shadow-xl transition-all overflow-hidden border border-gray-100">
                    <div class="h-48 bg-gray-200 relative">
                        <img src="https://dummyimage.com/600x400/2980b9/ffffff&text=Crawford+Flagship" alt="Crawford" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        <div class="absolute bottom-0 left-0 bg-blue-900 text-white px-4 py-1 rounded-tr-lg font-bold">FLAGSHIP</div>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold mb-2 group-hover:text-blue-600">Crawford</h3>
                        <p class="text-sm font-semibold text-blue-600 mb-3">The Full Experience</p>
                        <p class="text-gray-600 text-sm">Level 1 Fun Zone & Level 3 Climb Zone. High walls, AR bouldering, and adult coaching.</p>
                    </div>
                </a>
                
                <!-- Changi T3 -->
                <a href="changi.html" class="group block rounded-2xl bg-white shadow-sm hover:shadow-xl transition-all overflow-hidden border border-gray-100">
                    <div class="h-48 bg-gray-200 relative">
                        <img src="https://dummyimage.com/600x400/e67e22/ffffff&text=Changi+T3" alt="Changi T3" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold mb-2 group-hover:text-blue-600">Changi Airport T3</h3>
                        <p class="text-sm font-semibold text-orange-500 mb-3">Family & Kids Hub</p>
                        <p class="text-gray-600 text-sm">Fun-first climbing, birthday party venues, and weekend family passes.</p>
                    </div>
                </a>

                <!-- Clementi -->
                <a href="clementi.html" class="group block rounded-2xl bg-white shadow-sm hover:shadow-xl transition-all overflow-hidden border border-gray-100">
                    <div class="h-48 bg-gray-200 relative">
                        <img src="https://dummyimage.com/600x400/27ae60/ffffff&text=Clementi+Hub" alt="Clementi" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold mb-2 group-hover:text-blue-600">Clementi</h3>
                        <p class="text-sm font-semibold text-green-600 mb-3">Bouldering & Youth Hub</p>
                        <p class="text-gray-600 text-sm">Pure bouldering cave with dynamic weekly resets and youth classes.</p>
                    </div>
                </a>
            </div>
        </section>

        <!-- First Timer Onboarding Fast-Track -->
        <section class="bg-gray-100 py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="bg-white rounded-2xl p-8 shadow-md flex flex-col lg:flex-row gap-10 items-center">
                    <div class="lg:w-1/2">
                        <h2 class="text-3xl font-bold mb-4">New to Climbing? Start Here.</h2>
                        <p class="text-gray-600 mb-6">We've made getting on the wall as easy as possible. Check out our starter packs tailored for beginners.</p>
                        
                        <div class="space-y-4 mb-6">
                            <div class="flex items-start gap-3">
                                <div class="bg-green-100 text-green-600 p-2 rounded-full shrink-0"><svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg></div>
                                <div>
                                    <strong class="block text-gray-900">First-Timer Pack ($32)</strong>
                                    <span class="text-sm text-gray-500">Includes day pass, free harness & shoe rentals.</span>
                                </div>
                            </div>
                            <div class="flex items-start gap-3">
                                <div class="bg-green-100 text-green-600 p-2 rounded-full shrink-0"><svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg></div>
                                <div>
                                    <strong class="block text-gray-900">Outpost Starter Pack ($55)</strong>
                                    <span class="text-sm text-gray-500">3 entries plus basics classes to kickstart your journey.</span>
                                </div>
                            </div>
                        </div>

                        <div class="bg-orange-50 border border-orange-200 rounded-lg p-4 text-orange-800 text-sm">
                            <strong class="block mb-1">Important Notice:</strong>
                            <ul class="list-disc pl-5 space-y-1">
                                <li>Mandatory Waiver must be signed before climbing.</li>
                                <li>1:2 Adult-to-Child supervision rule enforced for kids ≤12 y/o.</li>
                            </ul>
                        </div>
                    </div>
                    <div class="lg:w-1/2 flex justify-center">
                        <img src="https://dummyimage.com/500x400/ecf0f1/2c3e50&text=Climbing+Made+Easy" alt="First Timer" class="rounded-xl shadow-lg transform rotate-2">
                    </div>
                </div>
            </div>
        </section>

        <!-- Value Prop -->
        <section class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold text-center mb-12">The Outpost Difference</h2>
            <div class="grid md:grid-cols-3 gap-8 text-center">
                <div>
                    <div class="text-4xl mb-4">📱</div>
                    <h3 class="text-xl font-bold mb-2">AR Climbing Walls</h3>
                    <p class="text-gray-600">Experience the future of climbing with interactive Augmented Reality walls and thematic obstacle lanes.</p>
                </div>
                <div>
                    <div class="text-4xl mb-4">🎓</div>
                    <h3 class="text-xl font-bold mb-2">Official Certification</h3>
                    <p class="text-gray-600">Get certified! We offer SNCS Level 1-3 & SNAS Abseiling Certification Courses.</p>
                </div>
                <div>
                    <div class="text-4xl mb-4">💳</div>
                    <h3 class="text-xl font-bold mb-2">Universal Outpost Credits</h3>
                    <p class="text-gray-600">1 Credit = $1. Shareable and redeemable seamlessly across all our outlets.</p>
                </div>
            </div>
        </section>
    </main>

    <footer class="bg-gray-900 text-gray-400 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <p>&copy; 2026 Outpost Climbing. All rights reserved.</p>
        </div>
    </footer>

    {common_js}
</body>
</html>
'''

# 2. crawford.html
crawford_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crawford Flagship | Outpost Climbing</title>
    {csp_meta}
    {tailwind_script}
</head>
<body class="bg-gray-50 font-sans antialiased text-gray-900">
    {header}

    <main>
        <section class="bg-blue-800 text-white py-16 relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <span class="bg-blue-600 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider mb-4 inline-block">Flagship Location</span>
                <h1 class="text-4xl md:text-5xl font-black mb-4">Crawford Flagship</h1>
                <p class="text-xl text-blue-100 max-w-2xl mb-8">The Full Experience. Two levels of climbing action for all ages and skill levels.</p>
                <button class="px-6 py-3 bg-white text-blue-900 font-bold rounded-lg hover:bg-gray-100 shadow-md">Book @ Crawford</button>
            </div>
        </section>

        <section class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold mb-8 text-center">Two Unique Zones</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-8">
                    <h3 class="text-2xl font-bold text-blue-600 mb-2">Zone 1: Level 1 Fun Zone</h3>
                    <p class="text-gray-600 mb-6">Perfect for kids and casual climbers.</p>
                    <ul class="space-y-3 mb-6">
                        <li class="flex items-center gap-2">✓ 30 thematic high wall lanes</li>
                        <li class="flex items-center gap-2">✓ AR bouldering walls</li>
                        <li class="flex items-center gap-2">✓ Min age 4 y/o, 15kg</li>
                        <li class="flex items-center gap-2">✓ 1.5-hr timed slots (Guided & Unguided)</li>
                    </ul>
                </div>
                
                <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-8">
                    <h3 class="text-2xl font-bold text-gray-900 mb-2">Zone 2: Level 3 Climb Zone</h3>
                    <p class="text-gray-600 mb-6">For the serious enthusiasts and pros.</p>
                    <ul class="space-y-3 mb-6">
                        <li class="flex items-center gap-2">✓ 40+ high wall lanes</li>
                        <li class="flex items-center gap-2">✓ Dedicated bouldering cave</li>
                        <li class="flex items-center gap-2">✓ Lead climbing routes</li>
                        <li class="flex items-center gap-2">✓ Adult coaching available</li>
                    </ul>
                </div>
            </div>
        </section>

        <section class="bg-gray-100 py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <h2 class="text-3xl font-bold mb-6">Featured Offerings</h2>
                <div class="grid sm:grid-cols-3 gap-6">
                    <div class="bg-white p-6 rounded-xl shadow-sm">
                        <h4 class="font-bold text-lg mb-2">SNCS Certification</h4>
                        <p class="text-sm text-gray-600">Get your official Level 1-3 certification right here at Crawford.</p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-sm">
                        <h4 class="font-bold text-lg mb-2">Outpost Basics</h4>
                        <p class="text-sm text-gray-600">Workshops tailored to transition you from novice to independent climber.</p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-sm">
                        <h4 class="font-bold text-lg mb-2">Adult Climb Squad</h4>
                        <p class="text-sm text-gray-600">Join our community training group and push your limits together.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>
    {common_js}
</body>
</html>
'''

# 3. changi.html
changi_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Changi Airport T3 | Outpost Climbing</title>
    {csp_meta}
    {tailwind_script}
</head>
<body class="bg-gray-50 font-sans antialiased text-gray-900">
    {header}

    <main>
        <section class="bg-orange-500 text-white py-16 relative overflow-hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <span class="bg-orange-400 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider mb-4 inline-block">Family & Kids Hub</span>
                <h1 class="text-4xl md:text-5xl font-black mb-4">Changi Airport T3</h1>
                <p class="text-xl text-orange-100 max-w-2xl mb-8">Fun-first climbing, unforgettable parties, and the ultimate family day-out.</p>
                <button class="px-6 py-3 bg-white text-orange-600 font-bold rounded-lg hover:bg-gray-100 shadow-md">Book Family Session @ T3</button>
            </div>
        </section>

        <section class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-2 gap-12 items-center">
                <div>
                    <h2 class="text-3xl font-bold mb-6">Birthday Party Packages 🎂</h2>
                    <p class="text-gray-600 mb-6 text-lg">Give your child an unforgettable birthday experience. Our all-inclusive packages handle everything so you can relax.</p>
                    <ul class="space-y-4">
                        <li class="flex items-start gap-3">
                            <span class="bg-orange-100 text-orange-600 p-1 rounded-full">✨</span>
                            <span>Dedicated party host and guided climbing</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="bg-orange-100 text-orange-600 p-1 rounded-full">🍕</span>
                            <span>Private function room for food and cake cutting</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="bg-orange-100 text-orange-600 p-1 rounded-full">🎁</span>
                            <span>Customizable add-ons (goodie bags, special themes)</span>
                        </li>
                    </ul>
                </div>
                <div class="bg-white p-8 rounded-2xl shadow-lg border-2 border-orange-100">
                    <h3 class="text-2xl font-bold mb-4">Holiday Camps</h3>
                    <div class="space-y-6">
                        <div>
                            <h4 class="font-bold text-lg text-orange-600">StepUp! Crash Course</h4>
                            <p class="text-sm text-gray-600">A structured 3-day intensive camp to build kids' confidence and climbing fundamentals.</p>
                        </div>
                        <div>
                            <h4 class="font-bold text-lg text-orange-600">Multi-Activity Camps</h4>
                            <p class="text-sm text-gray-600">Climb & Nerf / Climb & Art combo camps ensuring non-stop action during the school holidays.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    {common_js}
</body>
</html>
'''

# 4. clementi.html
clementi_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clementi | Outpost Climbing</title>
    {csp_meta}
    {tailwind_script}
</head>
<body class="bg-gray-50 font-sans antialiased text-gray-900">
    {header}

    <main>
        <section class="bg-green-700 text-white py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <span class="bg-green-600 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider mb-4 inline-block">Bouldering & Youth Hub</span>
                <h1 class="text-4xl md:text-5xl font-black mb-4">Clementi Outpost</h1>
                <p class="text-xl text-green-100 max-w-2xl mb-8">A modern, community-focused pure bouldering cave with dynamic weekly resets.</p>
                <button class="px-6 py-3 bg-white text-green-800 font-bold rounded-lg hover:bg-gray-100 shadow-md">Book @ Clementi</button>
            </div>
        </section>

        <!-- Universal Credits Banner -->
        <div class="bg-gray-900 text-white py-4">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center flex justify-center items-center gap-3">
                <span class="text-2xl">💳</span>
                <p class="font-semibold text-sm sm:text-base">Universal Credits Accepted Here! Redeem your Outpost Credits seamlessly at Clementi.</p>
            </div>
        </div>

        <section class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold mb-12 text-center">What's at Clementi?</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="bg-white rounded-xl shadow-sm p-8 border-l-4 border-green-500">
                    <h3 class="text-2xl font-bold mb-4">Pure Bouldering Cave</h3>
                    <p class="text-gray-600">Immerse yourself in our dedicated bouldering environment. With dynamic weekly route resets, there's always a new puzzle to solve, whether you are a V0 beginner or a V8 crusher.</p>
                </div>
                <div class="bg-white rounded-xl shadow-sm p-8 border-l-4 border-green-500">
                    <h3 class="text-2xl font-bold mb-4">Side-by-Side Coaching</h3>
                    <p class="text-gray-600">Unique to Clementi, we offer side-by-side adult bouldering clinics alongside our youth coaching programs, making it the perfect hub for multi-generational progression.</p>
                </div>
            </div>
        </section>
    </main>
    {common_js}
</body>
</html>
'''

# 5. first-timer.html
first_timer_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First Timers | Outpost Climbing</title>
    {csp_meta}
    {tailwind_script}
</head>
<body class="bg-gray-50 font-sans antialiased text-gray-900">
    {header}

    <main class="py-12">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <h1 class="text-4xl font-black mb-6">Welcome to Outpost!</h1>
            <p class="text-xl text-gray-600 mb-10">We're thrilled to have you. Here is your step-by-step guide to getting on the wall.</p>

            <div class="space-y-8">
                <!-- Step 1 -->
                <div class="bg-white p-6 rounded-xl shadow-sm flex gap-6">
                    <div class="shrink-0 flex items-center justify-center w-12 h-12 bg-blue-100 text-blue-600 font-black text-xl rounded-full">1</div>
                    <div>
                        <h3 class="text-xl font-bold mb-2">Create an Account & Sign Waiver</h3>
                        <p class="text-gray-600 mb-3">Safety first! A mandatory waiver is required for everyone entering the active areas. You can do this quickly via our Rezerv integration.</p>
                        <button class="text-sm font-semibold text-blue-600 hover:underline">Sign Waiver Now &rarr;</button>
                    </div>
                </div>

                <!-- Step 2 -->
                <div class="bg-white p-6 rounded-xl shadow-sm flex gap-6">
                    <div class="shrink-0 flex items-center justify-center w-12 h-12 bg-blue-100 text-blue-600 font-black text-xl rounded-full">2</div>
                    <div>
                        <h3 class="text-xl font-bold mb-2">What to Wear</h3>
                        <p class="text-gray-600">Comfortable, stretchy athletic wear. <strong>Covered non-marking shoes or climbing shoes are required.</strong> If you don't have climbing shoes, you must wear socks to rent ours!</p>
                    </div>
                </div>

                <!-- Step 3 -->
                <div class="bg-white p-6 rounded-xl shadow-sm flex gap-6">
                    <div class="shrink-0 flex items-center justify-center w-12 h-12 bg-blue-100 text-blue-600 font-black text-xl rounded-full">3</div>
                    <div>
                        <h3 class="text-xl font-bold mb-2">Supervision Rules (Kids ≤12 y/o)</h3>
                        <div class="bg-red-50 text-red-800 p-4 rounded-lg mt-2 text-sm">
                            <strong>Strict 1:2 Adult-to-Child Ratio</strong><br>
                            One supervising adult (21+) can supervise a maximum of 2 children aged 12 or below. The supervising adult must be actively watching on the mats.
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="mt-12 text-center">
                <a href="packages.html" class="inline-block px-8 py-4 bg-blue-600 text-white font-bold rounded-lg shadow-md hover:bg-blue-700">View Starter Packages</a>
            </div>
        </div>
    </main>
    {common_js}
</body>
</html>
'''

# 6. packages.html
packages_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Packages & Credits | Outpost Climbing</title>
    {csp_meta}
    {tailwind_script}
</head>
<body class="bg-gray-50 font-sans antialiased text-gray-900">
    {header}

    <main class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h1 class="text-4xl font-black text-center mb-4">Packages & Pricing</h1>
            <p class="text-xl text-gray-600 text-center mb-16 max-w-2xl mx-auto">Flexible options whether you drop by once a month or climb every day.</p>

            <div class="grid md:grid-cols-3 gap-8">
                <!-- Single Entries -->
                <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden flex flex-col">
                    <div class="p-8 bg-gray-50 border-b border-gray-100 text-center">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">Single Entry</h3>
                        <p class="text-gray-500 text-sm">Standard day pass</p>
                    </div>
                    <div class="p-8 flex-1 flex flex-col justify-between">
                        <ul class="space-y-4 mb-8">
                            <li class="flex justify-between items-center"><span class="text-gray-600">Adult</span><span class="font-bold">$26</span></li>
                            <li class="flex justify-between items-center"><span class="text-gray-600">Youth (≤20)</span><span class="font-bold">$20</span></li>
                            <li class="flex justify-between items-center"><span class="text-gray-600">Shoe Rental</span><span class="font-bold">$5</span></li>
                        </ul>
                        <button class="w-full py-3 bg-gray-100 text-gray-800 font-bold rounded-lg hover:bg-gray-200">Buy Pass</button>
                    </div>
                </div>

                <!-- First Timer -->
                <div class="bg-white rounded-2xl shadow-xl border-2 border-blue-500 overflow-hidden flex flex-col relative transform md:-translate-y-4">
                    <div class="absolute top-0 inset-x-0 bg-blue-500 text-white text-xs font-bold text-center py-1 uppercase tracking-wider">Best for Beginners</div>
                    <div class="p-8 bg-blue-50 border-b border-blue-100 text-center mt-4">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">Starter Packs</h3>
                        <p class="text-gray-500 text-sm">Everything you need to begin</p>
                    </div>
                    <div class="p-8 flex-1 flex flex-col justify-between">
                        <ul class="space-y-4 mb-8">
                            <li class="flex flex-col gap-1 border-b border-gray-100 pb-3">
                                <div class="flex justify-between"><strong class="text-gray-900">First-Timer Pack</strong><span class="font-bold text-blue-600">$32</span></div>
                                <span class="text-xs text-gray-500">1 Entry + Free Harness & Shoes</span>
                            </li>
                            <li class="flex flex-col gap-1">
                                <div class="flex justify-between"><strong class="text-gray-900">Outpost Starter Pack</strong><span class="font-bold text-blue-600">$55</span></div>
                                <span class="text-xs text-gray-500">3 Entries + Basics Classes</span>
                            </li>
                        </ul>
                        <button class="w-full py-3 bg-blue-600 text-white font-bold rounded-lg hover:bg-blue-700 shadow-md">Get Started</button>
                    </div>
                </div>

                <!-- OP Credits -->
                <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden flex flex-col">
                    <div class="p-8 bg-gray-50 border-b border-gray-100 text-center">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">OP Credits</h3>
                        <p class="text-gray-500 text-sm">Shareable currency ($1 = 1 Credit)</p>
                    </div>
                    <div class="p-8 flex-1 flex flex-col justify-between">
                        <ul class="space-y-4 mb-8 text-center">
                            <li class="font-bold text-3xl text-gray-900">$220 <span class="text-lg text-gray-500 font-normal">/ 220 Credits</span></li>
                            <li class="text-sm text-gray-500">Use for entry, rentals, classes, and merch across all locations. Fully shareable with friends!</li>
                        </ul>
                        <button class="w-full py-3 bg-gray-100 text-gray-800 font-bold rounded-lg hover:bg-gray-200">Buy Credits</button>
                    </div>
                </div>
            </div>

            <div class="mt-16 bg-gray-900 text-white rounded-2xl p-8 md:p-12 flex flex-col md:flex-row items-center justify-between">
                <div class="mb-6 md:mb-0 md:pr-8">
                    <h3 class="text-2xl font-bold mb-2">Outpost Resident Memberships</h3>
                    <p class="text-gray-400">Auto-renewing monthly memberships for unlimited climbing, priority booking, and pro-shop discounts.</p>
                </div>
                <button class="shrink-0 px-8 py-4 bg-white text-gray-900 font-bold rounded-lg hover:bg-gray-100 shadow-lg">View Memberships</button>
            </div>
        </div>
    </main>
    {common_js}
</body>
</html>
'''

# Write files
with open(os.path.join(base_dir, 'index.html'), 'w') as f:
    f.write(index_content)
with open(os.path.join(base_dir, 'crawford.html'), 'w') as f:
    f.write(crawford_content)
with open(os.path.join(base_dir, 'changi.html'), 'w') as f:
    f.write(changi_content)
with open(os.path.join(base_dir, 'clementi.html'), 'w') as f:
    f.write(clementi_content)
with open(os.path.join(base_dir, 'first-timer.html'), 'w') as f:
    f.write(first_timer_content)
with open(os.path.join(base_dir, 'packages.html'), 'w') as f:
    f.write(packages_content)

print("HTML generation complete.")
