"""
generate-assets.py
Generates the complete set of dark-themed, pixel-perfect SVGs matching the reference image.
"""

import os
import math

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)


def create_header_svg():
    svg = '''<svg width="880" height="230" viewBox="0 0 880 230" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Card Gradient & Glow -->
    <linearGradient id="header-bg" x1="0" y1="0" x2="880" y2="230" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#080C14" />
    </linearGradient>
    <linearGradient id="header-border" x1="0" y1="0" x2="880" y2="230" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#2D3748" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#4C1D95" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.8" />
    </linearGradient>
    <radialGradient id="header-glow" cx="720" cy="90" r="160" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.25" />
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#0B0F19" stop-opacity="0" />
    </radialGradient>

    <!-- Buttons Gradients -->
    <linearGradient id="btn-resume-bg" x1="0" y1="0" x2="130" y2="36" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#2E1065" />
      <stop offset="100%" stop-color="#1E1B4B" />
    </linearGradient>
    <linearGradient id="btn-portfolio-bg" x1="0" y1="0" x2="130" y2="36" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#172554" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="btn-linkedin-bg" x1="0" y1="0" x2="130" y2="36" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0C4A6E" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="chip-glow" x1="680" y1="40" x2="760" y2="120" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#3B82F6" />
      <stop offset="50%" stop-color="#8B5CF6" />
      <stop offset="100%" stop-color="#EC4899" />
    </linearGradient>
    <linearGradient id="wave-gradient" x1="600" y1="120" x2="840" y2="160" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#06B6D4" stop-opacity="0.3" />
    </linearGradient>
  </defs>

  <!-- Base Card Panel -->
  <rect x="1" y="1" width="878" height="228" rx="16" fill="url(#header-bg)" stroke="url(#header-border)" stroke-width="1.2" />
  <rect x="1" y="1" width="878" height="228" rx="16" fill="url(#header-glow)" />

  <!-- Left Content Column -->
  <!-- Name -->
  <text x="36" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="32" font-weight="700" fill="#FFFFFF" letter-spacing="-0.5">Sowndhar A<tspan fill="#A855F7">.</tspan></text>

  <!-- Subtitle -->
  <text x="36" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" font-weight="400" fill="#94A3B8">Building intelligent software, intuitive products, and smart manufacturing solutions.</text>

  <!-- Metadata Row -->
  <g transform="translate(36, 106)">
    <!-- Location Pin Icon -->
    <path d="M4 1.5C1.8 1.5 0 3.3 0 5.5C0 8.8 4 13 4 13C4 13 8 8.8 8 5.5C8 3.3 6.2 1.5 4 1.5ZM4 7C3.2 7 2.5 6.3 2.5 5.5C2.5 4.7 3.2 4 4 4C4.8 4 5.5 4.7 5.5 5.5C5.5 6.3 4.8 7 4 7Z" fill="#94A3B8" transform="translate(0, 1) scale(1.1)"/>
    <text x="16" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" fill="#CBD5E1">Coimbatore, India</text>

    <!-- Divider -->
    <line x1="140" y1="2" x2="140" y2="14" stroke="#334155" stroke-width="1.2"/>

    <!-- University Icon (Cap/Mortarboard) -->
    <path d="M7 1L0 4.5L7 8L13 5V9.5H14V4.5L7 1ZM2.5 7.2V10.2C2.5 11.5 4.5 12.8 7 12.8C9.5 12.8 11.5 11.5 11.5 10.2V7.2L7 9.5L2.5 7.2Z" fill="#94A3B8" transform="translate(154, 1) scale(1)"/>
    <text x="174" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" fill="#CBD5E1">KIT – CSE</text>

    <!-- Divider -->
    <line x1="248" y1="2" x2="248" y2="14" stroke="#334155" stroke-width="1.2"/>

    <!-- Calendar Icon -->
    <path d="M11 1.5H10.2V0H8.7V1.5H3.8V0H2.3V1.5H1.5C0.7 1.5 0 2.2 0 3V12C0 12.8 0.7 13.5 1.5 13.5H11C11.8 13.5 12.5 12.8 12.5 12V3C12.5 2.2 11.8 1.5 11 1.5ZM11 12H1.5V4.5H11V12Z" fill="#94A3B8" transform="translate(262, 1) scale(0.95)"/>
    <text x="280" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" fill="#CBD5E1">Year 3 · Sem 5</text>

    <!-- Divider -->
    <line x1="384" y1="2" x2="384" y2="14" stroke="#334155" stroke-width="1.2"/>

    <!-- GitHub Octocat Icon -->
    <path fill-rule="evenodd" clip-rule="evenodd" d="M6 0C2.69 0 0 2.74 0 6.12C0 8.83 1.73 11.12 4.14 11.94C4.44 12 4.55 11.81 4.55 11.65C4.55 11.51 4.54 11 4.54 10.43C3 10.71 2.65 10.02 2.53 9.68C2.46 9.5 2.16 8.94 1.9 8.79C1.68 8.67 1.37 8.37 1.89 8.36C2.38 8.35 2.73 8.82 2.85 9.01C3.41 9.98 4.31 9.71 4.66 9.54C4.72 9.13 4.88 8.85 5.06 8.69C3.68 8.53 2.24 7.98 2.24 5.56C2.24 4.87 2.48 4.29 2.87 3.84C2.81 3.68 2.59 3.03 2.93 2.15C2.93 2.15 3.45 1.98 4.65 2.81C5.15 2.67 5.68 2.6 6.21 2.6C6.74 2.6 7.27 2.67 7.77 2.81C8.97 1.97 9.49 2.15 9.49 2.15C9.83 3.03 9.61 3.68 9.55 3.84C9.94 4.29 10.18 4.86 10.18 5.56C10.18 7.99 8.73 8.53 7.35 8.69C7.58 8.89 7.78 9.28 7.78 9.89C7.78 10.76 7.77 11.47 7.77 11.65C7.77 11.81 7.88 12.01 8.18 11.94C10.59 11.12 12.32 8.82 12.32 6.12C12.32 2.74 9.63 0 6.32 0H6Z" fill="#94A3B8" transform="translate(398, 1) scale(1.1)"/>
    <text x="418" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" fill="#CBD5E1">Sowndhar-2005</text>
  </g>

  <!-- Button Row -->
  <g transform="translate(36, 150)">
    <!-- Button 1: Resume -->
    <g>
      <rect x="0" y="0" width="140" height="38" rx="10" fill="url(#btn-resume-bg)" stroke="#8B5CF6" stroke-width="1.2"/>
      <path d="M5.5 1.5C3.3 1.5 1.5 3.3 1.5 5.5C1.5 7.7 3.3 9.5 5.5 9.5C7.7 9.5 9.5 7.7 9.5 5.5C9.5 3.3 7.7 1.5 5.5 1.5ZM5.5 11C2.5 11 0 12.5 0 14.5V16H11V14.5C11 12.5 8.5 11 5.5 11Z" fill="#C084FC" transform="translate(20, 11) scale(0.9)"/>
      <text x="38" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="600" fill="#FFFFFF">Resume <tspan fill="#A855F7">↗</tspan></text>
    </g>

    <!-- Button 2: Portfolio -->
    <g transform="translate(155, 0)">
      <rect x="0" y="0" width="145" height="38" rx="10" fill="url(#btn-portfolio-bg)" stroke="#3B82F6" stroke-width="1.2"/>
      <path d="M12.5 0H1.5C0.7 0 0 0.7 0 1.5V9.5C0 10.3 0.7 11 1.5 11H5V13H3V14.5H11V13H9V11H12.5C13.3 11 14 10.3 14 9.5V1.5C14 0.7 13.3 0 12.5 0ZM12.5 9.5H1.5V1.5H12.5V9.5Z" fill="#60A5FA" transform="translate(20, 11) scale(0.95)"/>
      <text x="40" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="600" fill="#FFFFFF">Portfolio <tspan fill="#60A5FA">↗</tspan></text>
    </g>

    <!-- Button 3: LinkedIn -->
    <g transform="translate(315, 0)">
      <rect x="0" y="0" width="145" height="38" rx="10" fill="url(#btn-linkedin-bg)" stroke="#0EA5E9" stroke-width="1.2"/>
      <path d="M3.2 14.5H0.3V4.9H3.2V14.5ZM1.8 3.6C0.8 3.6 0 2.8 0 1.8C0 0.8 0.8 0 1.8 0C2.7 0 3.5 0.8 3.5 1.8C3.5 2.8 2.7 3.6 1.8 3.6ZM14.5 14.5H11.6V9.9C11.6 8.8 11.6 7.4 10 7.4C8.4 7.4 8.2 8.6 8.2 9.8V14.5H5.3V4.9H8V6.2H8.1C8.5 5.4 9.5 4.6 11 4.6C14.1 4.6 14.6 6.7 14.6 9.3V14.5H14.5Z" fill="#38BDF8" transform="translate(20, 11) scale(0.95)"/>
      <text x="40" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="600" fill="#FFFFFF">LinkedIn <tspan fill="#38BDF8">↗</tspan></text>
    </g>
  </g>

  <!-- Right Side: Custom SVG Illustration -->
  <g transform="translate(640, 15)">
    <!-- Floating Isometric Cube Wireframe (Minimalist) -->
    <path d="M40 25 L65 10 L90 25 L65 40 Z" fill="none" stroke="#6366F1" stroke-width="0.9" opacity="0.45"/>
    <path d="M40 25 L40 55 L65 70 L65 40" fill="none" stroke="#6366F1" stroke-width="0.9" opacity="0.45"/>
    <path d="M90 25 L90 55 L65 70" fill="none" stroke="#6366F1" stroke-width="0.9" opacity="0.45"/>

    <!-- Subtle Minimal Engineering Gear/Symbol -->
    <circle cx="165" cy="35" r="9" fill="none" stroke="#0EA5E9" stroke-width="1.2" stroke-dasharray="2,2" opacity="0.6"/>
    <circle cx="165" cy="35" r="4" fill="none" stroke="#38BDF8" stroke-width="1" opacity="0.6"/>

    <!-- Neural Network Connection Traces -->
    <path d="M50 85 Q75 60 110 75 T160 55" fill="none" stroke="#818CF8" stroke-width="1" opacity="0.4" stroke-dasharray="3,3"/>
    <path d="M70 120 Q95 90 120 100 T180 95" fill="none" stroke="#38BDF8" stroke-width="1" opacity="0.35"/>
    <circle cx="50" cy="85" r="2.5" fill="#818CF8" opacity="0.7"/>
    <circle cx="110" cy="75" r="2" fill="#C084FC" opacity="0.8"/>
    <circle cx="160" cy="55" r="2.5" fill="#38BDF8" opacity="0.7"/>

    <!-- AI Microchip Outer Pins -->
    <g stroke="#38BDF8" stroke-width="1.5" opacity="0.75">
      <!-- Top pins -->
      <line x1="98" y1="52" x2="98" y2="44"/>
      <line x1="108" y1="52" x2="108" y2="42"/>
      <line x1="118" y1="52" x2="118" y2="42"/>
      <line x1="128" y1="52" x2="128" y2="44"/>
      <!-- Bottom pins -->
      <line x1="98" y1="102" x2="98" y2="110"/>
      <line x1="108" y1="102" x2="108" y2="112"/>
      <line x1="118" y1="102" x2="118" y2="112"/>
      <line x1="128" y1="102" x2="128" y2="110"/>
      <!-- Left pins -->
      <line x1="86" y1="64" x2="78" y2="64"/>
      <line x1="86" y1="74" x2="76" y2="74"/>
      <line x1="86" y1="84" x2="76" y2="84"/>
      <line x1="86" y1="94" x2="78" y2="94"/>
      <!-- Right pins -->
      <line x1="140" y1="64" x2="148" y2="64"/>
      <line x1="140" y1="74" x2="150" y2="74"/>
      <line x1="140" y1="84" x2="150" y2="84"/>
      <line x1="140" y1="94" x2="148" y2="94"/>
    </g>

    <!-- AI Microchip Body -->
    <rect x="86" y="52" width="54" height="50" rx="8" fill="#111827" stroke="url(#chip-glow)" stroke-width="2"/>
    <rect x="91" y="57" width="44" height="40" rx="5" fill="#1E1B4B" stroke="#6366F1" stroke-width="1" opacity="0.8"/>
    <text x="113" y="83" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">AI</text>

    <!-- Wave Graphic Underneath -->
    <path d="M-20 150 C40 125, 90 165, 140 145 C190 125, 210 155, 250 140" fill="none" stroke="url(#wave-gradient)" stroke-width="3" stroke-linecap="round"/>
    <path d="M0 160 C50 140, 100 175, 150 155 C200 135, 220 165, 260 150" fill="none" stroke="url(#wave-gradient)" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
  </g>
</svg>'''
    return svg


def create_about_svg():
    svg = '''<svg width="880" height="110" viewBox="0 0 880 110" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="about-bg" x1="0" y1="0" x2="880" y2="110" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#080C14" />
    </linearGradient>
    <linearGradient id="about-border" x1="0" y1="0" x2="880" y2="110" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#2D3748" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.8" />
    </linearGradient>
  </defs>

  <!-- Panel Container -->
  <rect x="1" y="1" width="878" height="108" rx="14" fill="url(#about-bg)" stroke="url(#about-border)" stroke-width="1.2" />

  <!-- Header: Icon & Title -->
  <g transform="translate(28, 22)">
    <!-- Person Icon -->
    <path d="M6 0C7.66 0 9 1.34 9 3C9 4.66 7.66 6 6 6C4.34 6 3 4.66 3 3C3 1.34 4.34 0 6 0ZM6 7.5C9.33 7.5 12 9.17 12 11.5V13H0V11.5C0 9.17 2.67 7.5 6 7.5Z" fill="#E2E8F0" transform="translate(0, 1) scale(1.15)"/>
    <text x="24" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="600" fill="#FFFFFF">About Me</text>
  </g>

  <!-- Content with Vertical Purple Bar -->
  <g transform="translate(28, 54)">
    <!-- Vertical Purple Bar -->
    <rect x="0" y="2" width="3" height="38" rx="1.5" fill="#8B5CF6" />

    <!-- Text Body -->
    <text x="18" y="16" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.8" font-weight="400" fill="#E2E8F0">
      I build real-world digital and physical solutions by combining software development, product design, and
    </text>
    <text x="18" y="36" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.8" font-weight="400" fill="#E2E8F0">
      smart manufacturing. I enjoy turning ideas into useful, user-centric, and impactful systems.
    </text>
  </g>
</svg>'''
    return svg


def create_expertise_svg():
    svg = '''<svg width="880" height="120" viewBox="0 0 880 120" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Card Gradients -->
    <linearGradient id="exp-card-bg" x1="0" y1="0" x2="208" y2="120" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0F1422" />
      <stop offset="100%" stop-color="#0B0F19" />
    </linearGradient>

    <!-- Border Gradients for each expertise -->
    <linearGradient id="border-aiml" x1="0" y1="0" x2="208" y2="120" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.5" />
    </linearGradient>
    <linearGradient id="border-dev" x1="0" y1="0" x2="208" y2="120" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.5" />
    </linearGradient>
    <linearGradient id="border-mfg" x1="0" y1="0" x2="208" y2="120" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.5" />
    </linearGradient>
    <linearGradient id="border-uiux" x1="0" y1="0" x2="208" y2="120" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#EC4899" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.5" />
    </linearGradient>
  </defs>

  <!-- Card 1: AI/ML -->
  <g transform="translate(0, 0)">
    <rect x="1" y="1" width="208" height="118" rx="14" fill="url(#exp-card-bg)" stroke="url(#border-aiml)" stroke-width="1.2"/>
    <!-- Icon Container -->
    <rect x="20" y="18" width="36" height="36" rx="8" fill="#2E1065" stroke="#7C3AED" stroke-width="1"/>
    <!-- Brain / Neural Network Icon -->
    <path d="M12 4C9.5 4 7.5 5.8 7.1 8.2C6.1 8.6 5.3 9.4 5.1 10.5C4.2 11.2 3.7 12.3 3.7 13.5C3.7 15.3 4.9 16.7 6.6 17C7.1 18.7 8.6 20 10.5 20C11.5 20 12.4 19.6 13 19V5C12.7 4.4 12.4 4 12 4ZM15 5V19C15.6 19.6 16.5 20 17.5 20C19.4 20 20.9 18.7 21.4 17C23.1 16.7 24.3 15.3 24.3 13.5C24.3 12.3 23.8 11.2 22.9 10.5C22.7 9.4 21.9 8.6 20.9 8.2C20.5 5.8 18.5 4 16 4C15.6 4 15.3 4.4 15 5Z" fill="#C084FC" transform="translate(24, 22) scale(0.9)"/>
    <!-- Title & Subtitle -->
    <text x="20" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">AI/ML</text>
    <text x="20" y="100" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="400" fill="#94A3B8">ML · DL · NLP · LLM · RAG</text>
  </g>

  <!-- Card 2: Development -->
  <g transform="translate(224, 0)">
    <rect x="1" y="1" width="208" height="118" rx="14" fill="url(#exp-card-bg)" stroke="url(#border-dev)" stroke-width="1.2"/>
    <!-- Icon Container -->
    <rect x="20" y="18" width="36" height="36" rx="8" fill="#172554" stroke="#2563EB" stroke-width="1"/>
    <!-- Code Icon </> -->
    <path d="M7 6L2 11L7 16M15 6L20 11L15 16M12 4L10 18" stroke="#60A5FA" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" transform="translate(27, 25) scale(0.95)"/>
    <!-- Title & Subtitle -->
    <text x="20" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">Development</text>
    <text x="20" y="100" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="400" fill="#94A3B8">Web · Desktop · Mobile · APIs</text>
  </g>

  <!-- Card 3: Manufacturing -->
  <g transform="translate(448, 0)">
    <rect x="1" y="1" width="208" height="118" rx="14" fill="url(#exp-card-bg)" stroke="url(#border-mfg)" stroke-width="1.2"/>
    <!-- Icon Container -->
    <rect x="20" y="18" width="36" height="36" rx="8" fill="#064E3B" stroke="#059669" stroke-width="1"/>
    <!-- 3D Cube / Precision Wireframe Icon -->
    <path d="M12 2L2 7L12 12L22 7L12 2ZM2 17L12 22L22 17M2 12L12 17L22 12" stroke="#34D399" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" transform="translate(26, 24) scale(0.95)"/>
    <!-- Title & Subtitle -->
    <text x="20" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">Manufacturing</text>
    <text x="20" y="100" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="400" fill="#94A3B8">CAD · Fabrication · IIoT · Quality</text>
  </g>

  <!-- Card 4: UI/UX Design -->
  <g transform="translate(672, 0)">
    <rect x="1" y="1" width="208" height="118" rx="14" fill="url(#exp-card-bg)" stroke="url(#border-uiux)" stroke-width="1.2"/>
    <!-- Icon Container -->
    <rect x="20" y="18" width="36" height="36" rx="8" fill="#4C0519" stroke="#E11D48" stroke-width="1"/>
    <!-- Layers Icon -->
    <path d="M12 2L2 7L12 12L22 7L12 2ZM2 17L12 22L22 17M2 12L12 17L22 12" stroke="#FB7185" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" transform="translate(26, 24) scale(0.95)"/>
    <!-- Title & Subtitle -->
    <text x="20" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">UI/UX Design</text>
    <text x="20" y="100" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="400" fill="#94A3B8">Product · Design · Prototyping</text>
  </g>
</svg>'''
    return svg


def create_tech_stack_svg():
    svg = '''<svg width="880" height="340" viewBox="0 0 880 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="ts-bg" x1="0" y1="0" x2="880" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#080C14" />
    </linearGradient>
    <linearGradient id="ts-border" x1="0" y1="0" x2="880" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#2D3748" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.8" />
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="878" height="338" rx="14" fill="url(#ts-bg)" stroke="url(#ts-border)" stroke-width="1.2" />

  <!-- Section Title -->
  <g transform="translate(28, 22)">
    <path d="M9 1L1 5L9 9L17 5L9 1ZM1 13L9 17L17 13M1 9L9 13L17 9" stroke="#E2E8F0" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" transform="translate(0, 0) scale(1)"/>
    <text x="28" y="14" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="600" fill="#FFFFFF">Tech Stack</text>
  </g>

  <!-- Row 1: Languages -->
  <g transform="translate(28, 56)">
    <!-- Label -->
    <path d="M4 3L1 6L4 9M10 3L13 6L10 9M8 2L6 10" stroke="#94A3B8" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" transform="translate(0, 7) scale(1)"/>
    <text x="20" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#E2E8F0">Languages</text>

    <!-- Pills Container -->
    <g transform="translate(130, 0)">
      <!-- Python -->
      <g transform="translate(0, 0)">
        <rect width="84" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#3776AB"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="9" font-weight="bold" fill="#FFD43B" text-anchor="middle">Py</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Python</text>
      </g>
      <!-- TypeScript -->
      <g transform="translate(92, 0)">
        <rect width="102" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <rect x="8" y="7" width="14" height="14" rx="3" fill="#3178C6"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">TS</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">TypeScript</text>
      </g>
      <!-- JavaScript -->
      <g transform="translate(202, 0)">
        <rect width="100" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <rect x="8" y="7" width="14" height="14" rx="3" fill="#F7DF1E"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#000000" text-anchor="middle">JS</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">JavaScript</text>
      </g>
      <!-- C++ -->
      <g transform="translate(310, 0)">
        <rect width="68" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#00599C"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">C++</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">C++</text>
      </g>
      <!-- Rust -->
      <g transform="translate(386, 0)">
        <rect width="70" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#DEA584"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#000000" text-anchor="middle">R</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Rust</text>
      </g>
      <!-- Go -->
      <g transform="translate(464, 0)">
        <rect width="64" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#00ADD8"/>
        <text x="15" y="17" font-family="sans-serif" font-size="8" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Go</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Go</text>
      </g>
      <!-- C# -->
      <g transform="translate(536, 0)">
        <rect width="60" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#9B4993"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8" font-weight="bold" fill="#FFFFFF" text-anchor="middle">C#</text>
        <text x="27" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">C#</text>
      </g>
    </g>
  </g>

  <!-- Row 2: Frontend -->
  <g transform="translate(28, 98)">
    <path d="M1 2H13V10H1V2ZM4 13H10M7 10V13" stroke="#94A3B8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" transform="translate(0, 7) scale(1)"/>
    <text x="20" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#E2E8F0">Frontend</text>

    <g transform="translate(130, 0)">
      <!-- React -->
      <g transform="translate(0, 0)">
        <rect width="78" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="6" fill="#61DAFB"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">React</text>
      </g>
      <!-- Angular -->
      <g transform="translate(86, 0)">
        <rect width="86" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <polygon points="15,7 21,9 20,18 15,21 10,18 9,9" fill="#DD0031"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">A</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Angular</text>
      </g>
      <!-- SvelteKit -->
      <g transform="translate(180, 0)">
        <rect width="94" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#FF3E00"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">S</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">SvelteKit</text>
      </g>
      <!-- Tailwind -->
      <g transform="translate(282, 0)">
        <rect width="86" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#06B6D4"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Tailwind</text>
      </g>
      <!-- Bootstrap -->
      <g transform="translate(376, 0)">
        <rect width="94" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <rect x="9" y="8" width="12" height="12" rx="3" fill="#7952B3"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="9" font-weight="bold" fill="#FFFFFF" text-anchor="middle">B</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Bootstrap</text>
      </g>
    </g>
  </g>

  <!-- Row 3: Backend -->
  <g transform="translate(28, 140)">
    <path d="M1 3C1 1.9 3.7 1 7 1C10.3 1 13 1.9 13 3M1 3V11C1 12.1 3.7 13 7 13C10.3 13 13 12.1 13 11V3M1 7C1 8.1 3.7 9 7 9C10.3 9 13 8.1 13 7" stroke="#94A3B8" stroke-width="1.3" stroke-linecap="round" fill="none" transform="translate(0, 7) scale(1)"/>
    <text x="20" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#E2E8F0">Backend</text>

    <g transform="translate(130, 0)">
      <!-- Spring Boot -->
      <g transform="translate(0, 0)">
        <rect width="108" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#6DB33F"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Spring Boot</text>
      </g>
      <!-- Node.js -->
      <g transform="translate(116, 0)">
        <rect width="84" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#339933"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Node.js</text>
      </g>
      <!-- Express -->
      <g transform="translate(208, 0)">
        <rect width="82" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#475569"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8" font-weight="bold" fill="#FFFFFF" text-anchor="middle">ex</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Express</text>
      </g>
      <!-- FastAPI -->
      <g transform="translate(298, 0)">
        <rect width="82" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#009688"/>
        <path d="M15 9L11 15H14L13 19L19 13H16L17 9H15Z" fill="#FFFFFF" transform="translate(3, 0) scale(0.8)"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">FastAPI</text>
      </g>
    </g>
  </g>

  <!-- Row 4: Data & Cloud -->
  <g transform="translate(28, 182)">
    <path d="M12 9C12.8 9 13.5 8.3 13.5 7.5C13.5 6.7 12.8 6 12 6C11.9 6 11.8 6 11.7 6.1C11.3 4.3 9.8 3 8 3C6.4 3 5 4 4.5 5.5C4.3 5.4 4.1 5.4 3.9 5.4C2.3 5.4 1 6.7 1 8.3C1 9.9 2.3 11.2 3.9 11.2H12C12.8 11.2 13.5 10.5 13.5 9.7" stroke="#94A3B8" stroke-width="1.3" stroke-linecap="round" fill="none" transform="translate(0, 7) scale(1)"/>
    <text x="20" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#E2E8F0">Data &amp; Cloud</text>

    <g transform="translate(130, 0)">
      <!-- PostgreSQL -->
      <g transform="translate(0, 0)">
        <rect width="104" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#4169E1"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">PostgreSQL</text>
      </g>
      <!-- MongoDB -->
      <g transform="translate(112, 0)">
        <rect width="94" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#47A248"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">MongoDB</text>
      </g>
      <!-- Firebase -->
      <g transform="translate(214, 0)">
        <rect width="90" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#FFCA28"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Firebase</text>
      </g>
      <!-- AWS -->
      <g transform="translate(312, 0)">
        <rect width="68" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <rect x="8" y="7" width="14" height="14" rx="3" fill="#FF9900"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="7.5" font-weight="bold" fill="#000000" text-anchor="middle">aws</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">AWS</text>
      </g>
      <!-- Azure -->
      <g transform="translate(388, 0)">
        <rect width="72" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#0078D4"/>
        <polygon points="12,19 16,19 18,10 14,10" fill="#FFFFFF"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Azure</text>
      </g>
    </g>
  </g>

  <!-- Row 5: AI/ML Frameworks -->
  <g transform="translate(28, 224)">
    <circle cx="7" cy="12" r="5" stroke="#94A3B8" stroke-width="1.3" fill="none"/>
    <circle cx="7" cy="12" r="2" fill="#94A3B8"/>
    <text x="20" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#E2E8F0">AI &amp; ML</text>

    <g transform="translate(130, 0)">
      <!-- NumPy -->
      <g transform="translate(0, 0)">
        <rect width="82" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#013243"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8" font-weight="bold" fill="#4DABCF" text-anchor="middle">NP</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">NumPy</text>
      </g>
      <!-- Pandas -->
      <g transform="translate(90, 0)">
        <rect width="84" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#150458"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8" font-weight="bold" fill="#E70488" text-anchor="middle">PD</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Pandas</text>
      </g>
      <!-- Scikit-learn -->
      <g transform="translate(182, 0)">
        <rect width="106" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#F7931E"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8" font-weight="bold" fill="#3499CD" text-anchor="middle">SK</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Scikit-learn</text>
      </g>
      <!-- TensorFlow -->
      <g transform="translate(296, 0)">
        <rect width="102" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#FF6F00"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">TF</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">TensorFlow</text>
      </g>
      <!-- PyTorch -->
      <g transform="translate(406, 0)">
        <rect width="86" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#EE4C2C"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8" font-weight="bold" fill="#FFFFFF" text-anchor="middle">🔥</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">PyTorch</text>
      </g>
    </g>
  </g>

  <!-- Row 6: Design & Tools -->
  <g transform="translate(28, 266)">
    <path d="M12.5 1.5C11.1 0.1 8.9 0.1 7.5 1.5L1.5 7.5C0.1 8.9 0.1 11.1 1.5 12.5C2.9 13.9 5.1 13.9 6.5 12.5L12.5 6.5C13.9 5.1 13.9 2.9 12.5 1.5Z" stroke="#94A3B8" stroke-width="1.3" fill="none" transform="translate(0, 7) scale(0.9)"/>
    <text x="20" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#E2E8F0">Design &amp; Tools</text>

    <g transform="translate(130, 0)">
      <!-- Figma -->
      <g transform="translate(0, 0)">
        <rect width="78" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#F24E1E"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Figma</text>
      </g>
      <!-- Docker -->
      <g transform="translate(86, 0)">
        <rect width="84" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#2496ED"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Docker</text>
      </g>
      <!-- Git -->
      <g transform="translate(178, 0)">
        <rect width="64" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#F05032"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Git</text>
      </g>
      <!-- GitHub -->
      <g transform="translate(250, 0)">
        <rect width="86" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#24292F"/>
        <path fill-rule="evenodd" clip-rule="evenodd" d="M4 0C1.79 0 0 1.83 0 4.08C0 5.89 1.15 7.41 2.76 7.96C2.96 8 3.03 7.87 3.03 7.77V7.12C1.92 7.36 1.69 6.86 1.69 6.86C1.51 6.39 1.25 6.27 1.25 6.27C0.89 6.02 1.28 6.03 1.28 6.03C1.68 6.06 1.89 6.45 1.89 6.45C2.24 7.07 2.82 6.89 3.05 6.78C3.09 6.52 3.19 6.34 3.31 6.23C2.42 6.13 1.49 5.78 1.49 4.2C1.49 3.75 1.65 3.38 1.91 3.08C1.87 2.98 1.73 2.56 1.95 1.98C1.95 1.98 2.3 1.87 3.09 2.42C3.42 2.33 3.77 2.28 4.12 2.28C4.47 2.28 4.82 2.33 5.15 2.42C5.94 1.87 6.29 1.98 6.29 1.98C6.51 2.56 6.37 2.98 6.33 3.08C6.59 3.38 6.75 3.75 6.75 4.2C6.75 5.79 5.82 6.13 4.93 6.23C5.08 6.36 5.21 6.62 5.21 7.02V7.77C5.21 7.87 5.28 8 5.48 7.96C7.09 7.41 8.24 5.89 8.24 4.08C8.24 1.83 6.45 0 4.24 0H4Z" fill="#FFFFFF" transform="translate(11, 10) scale(1)"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">GitHub</text>
      </g>
      <!-- VS Code -->
      <g transform="translate(344, 0)">
        <rect width="92" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#007ACC"/>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">VS Code</text>
      </g>
      <!-- Linux -->
      <g transform="translate(444, 0)">
        <rect width="76" height="28" rx="14" fill="#161B26" stroke="#30363D" stroke-width="1"/>
        <circle cx="15" cy="14" r="7" fill="#FCC624"/>
        <text x="15" y="17.5" font-family="sans-serif" font-size="8" font-weight="bold" fill="#000000" text-anchor="middle">🐧</text>
        <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#F0F6FC">Linux</text>
      </g>
    </g>
  </g>
</svg>'''
    return svg


def create_languages_svg(data=None):
    if not data:
        data = {
            "total_bytes": 4053704,
            "total_languages": 10,
            "repos_count": 14,
            "languages": [
                {"name": "TypeScript", "bytes": 1195966, "color": "#3178C6", "lines": "4.2k lines"},
                {"name": "JavaScript", "bytes": 1041693, "color": "#F7DF1E", "lines": "3.8k lines"},
                {"name": "Python", "bytes": 911704, "color": "#3776AB", "lines": "3.2k lines"},
                {"name": "HTML", "bytes": 375237, "color": "#E34F26", "lines": "1.3k lines"},
                {"name": "Jupyter Notebook", "bytes": 258377, "color": "#DA5B0B", "lines": "920 lines"},
                {"name": "CSS", "bytes": 253238, "color": "#563D7C", "lines": "890 lines"},
                {"name": "Java", "bytes": 14341, "color": "#B07219", "lines": "180 lines"}
            ]
        }

    total_bytes = data["total_bytes"]
    top_langs = data["languages"][:6]

    # Calculate bar segments
    bar_width = 824
    segments_svg = ""
    curr_x = 0
    for idx, l in enumerate(top_langs):
        w = max(4, round((l["bytes"] / total_bytes) * bar_width))
        if curr_x + w > bar_width or idx == len(top_langs) - 1:
            w = bar_width - curr_x
        rx_attr = 'rx="5"' if idx == 0 and curr_x + w == bar_width else ('rx="5" ' if idx == 0 else '')
        segments_svg += f'<rect x="{curr_x}" y="0" width="{w}" height="10" fill="{l["color"]}" />\n'
        curr_x += w
        if curr_x >= bar_width:
            break

    # Format bytes to human readable
    def fmt_bytes(b):
        if b >= 1048576:
            return f"{b/1048576:.2f} MB"
        elif b >= 1024:
            return f"{b/1024:.1f} KB"
        return f"{b} bytes"

    # 2 columns of 3 languages
    langs_col1 = ""
    langs_col2 = ""
    for idx, l in enumerate(top_langs):
        pct = (l["bytes"] / total_bytes) * 100
        size_str = fmt_bytes(l["bytes"])
        lines_str = l.get("lines", f"{pct:.1f}%")
        item_svg = f'''<g transform="translate(0, {idx % 3 * 26})">
      <circle cx="6" cy="7" r="4.5" fill="{l["color"]}"/>
      <text x="20" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#FFFFFF">{l["name"]}</text>
      <text x="180" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400" fill="#94A3B8">{lines_str}</text>
      <text x="320" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#CBD5E1" text-anchor="end">{size_str}</text>
    </g>\n'''
        if idx < 3:
            langs_col1 += item_svg
        else:
            langs_col2 += item_svg

    size_formatted = fmt_bytes(total_bytes)
    total_count = data.get("total_languages", len(top_langs))

    svg = f'''<svg width="880" height="210" viewBox="0 0 880 210" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="lang-bg" x1="0" y1="0" x2="880" y2="210" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#080C14" />
    </linearGradient>
    <linearGradient id="lang-border" x1="0" y1="0" x2="880" y2="210" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#2D3748" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.8" />
    </linearGradient>
    <clipPath id="lang-bar-clip">
      <rect x="0" y="0" width="824" height="10" rx="5"/>
    </clipPath>
  </defs>

  <rect x="1" y="1" width="878" height="208" rx="14" fill="url(#lang-bg)" stroke="url(#lang-border)" stroke-width="1.2" />

  <!-- Header -->
  <g transform="translate(28, 22)">
    <!-- Terminal / Code Window Icon -->
    <path d="M1 2C1 1.45 1.45 1 2 1H14C14.55 1 15 1.45 15 2V12C15 12.55 14.55 13 14 13H2C1.45 13 1 12.55 1 12V2ZM3.5 4.5L6.5 7L3.5 9.5M8 9.5H12.5" stroke="#E2E8F0" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <text x="26" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="600" fill="#FFFFFF">Most Used Languages</text>

    <!-- Top Right Count Link -->
    <text x="824" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#818CF8" text-anchor="end">{total_count} Languages ↗</text>
  </g>

  <!-- Subtitle -->
  <text x="28" y="62" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400" fill="#94A3B8">Estimation from {size_formatted} of code across {data.get("repos_count", 14)} repositories</text>

  <!-- Progress Bar -->
  <g transform="translate(28, 76)" clip-path="url(#lang-bar-clip)">
    {segments_svg}
  </g>

  <!-- Columns Breakdown -->
  <g transform="translate(28, 108)">
    <g transform="translate(0, 0)">
      {langs_col1}
    </g>

    <!-- Vertical Divider -->
    <line x1="390" y1="0" x2="390" y2="76" stroke="#1E293B" stroke-width="1.2"/>

    <g transform="translate(440, 0)">
      {langs_col2}
    </g>
  </g>
</svg>'''
    return svg


def create_projects_svg():
    svg = '''<svg width="880" height="340" viewBox="0 0 880 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="proj-bg" x1="0" y1="0" x2="880" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#080C14" />
    </linearGradient>
    <linearGradient id="proj-border" x1="0" y1="0" x2="880" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#2D3748" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.8" />
    </linearGradient>
    <linearGradient id="card-inner-bg" x1="0" y1="0" x2="402" y2="126" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#121826" />
      <stop offset="100%" stop-color="#0E131F" />
    </linearGradient>
    <linearGradient id="card-inner-border" x1="0" y1="0" x2="402" y2="126" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#2D3748" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#1F2937" stop-opacity="0.5" />
    </linearGradient>
  </defs>

  <!-- Main Container -->
  <rect x="1" y="1" width="878" height="338" rx="14" fill="url(#proj-bg)" stroke="url(#proj-border)" stroke-width="1.2" />

  <!-- Section Header -->
  <g transform="translate(28, 22)">
    <path d="M10 1L2 5L10 9L18 5L10 1ZM2 13L10 17L18 13M2 9L10 13L18 9" stroke="#E2E8F0" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <text x="28" y="14" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="600" fill="#FFFFFF">Highlighted Projects</text>
    <text x="824" y="14" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#818CF8" text-anchor="end">View All Projects ↗</text>
  </g>

  <!-- 2x2 Grid of Cards -->

  <!-- Card 1: Campus Canteen - Food Hub -->
  <g transform="translate(28, 54)">
    <rect x="0" y="0" width="402" height="126" rx="12" fill="url(#card-inner-bg)" stroke="url(#card-inner-border)" stroke-width="1"/>
    
    <!-- Icon Container -->
    <circle cx="34" cy="34" r="16" fill="#2E1065" stroke="#7C3AED" stroke-width="1"/>
    <!-- Utensils / Fork & Spoon Icon -->
    <path d="M6 1V6C6 7.1 5.1 8 4 8H3C1.9 8 1 7.1 1 6V1M3.5 8V15M9 1V5C9 6.7 10.3 8 12 8V15" stroke="#C084FC" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" transform="translate(27, 26) scale(0.9)"/>

    <!-- Title & External Link -->
    <text x="62" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" font-weight="700" fill="#FFFFFF">Campus Canteen – Food Hub</text>
    <text x="382" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#818CF8" text-anchor="end">↗</text>

    <!-- Description -->
    <text x="62" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400" fill="#94A3B8">Canteen management web app with real-time</text>
    <text x="62" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400" fill="#94A3B8">orders, admin, and analytics.</text>

    <!-- Tags -->
    <g transform="translate(62, 88)">
      <rect width="64" height="22" rx="11" fill="#1E1B4B" stroke="#4338CA" stroke-width="0.8"/>
      <text x="32" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#A5B4FC" text-anchor="middle">Angular</text>
      <rect x="72" y="0" width="66" height="22" rx="11" fill="#0C4A6E" stroke="#0284C7" stroke-width="0.8"/>
      <text x="105" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#7DD3FC" text-anchor="middle">Tailwind</text>
    </g>
  </g>

  <!-- Card 2: Algospeak -->
  <g transform="translate(450, 54)">
    <rect x="0" y="0" width="402" height="126" rx="12" fill="url(#card-inner-bg)" stroke="url(#card-inner-border)" stroke-width="1"/>

    <!-- Icon Container -->
    <circle cx="34" cy="34" r="16" fill="#3B0764" stroke="#9333EA" stroke-width="1"/>
    <!-- Speech / Nodes Icon -->
    <path d="M12 2C6.5 2 2 5.5 2 10C2 12.3 3.1 14.3 5 15.8V19L8.2 17.4C9.4 17.8 10.7 18 12 18C17.5 18 22 14.5 22 10C22 5.5 17.5 2 12 2Z" stroke="#D8B4FE" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none" transform="translate(23, 23) scale(0.9)"/>

    <!-- Title & External Link -->
    <text x="62" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" font-weight="700" fill="#FFFFFF">Algospeak</text>
    <text x="382" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#818CF8" text-anchor="end">↗</text>

    <!-- Description -->
    <text x="62" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400" fill="#94A3B8">Resilient semantic detection (Chrome Extension)</text>
    <text x="62" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400" fill="#94A3B8">for safer and smarter browsing.</text>

    <!-- Tags -->
    <g transform="translate(62, 88)">
      <rect width="60" height="22" rx="11" fill="#1E293B" stroke="#475569" stroke-width="0.8"/>
      <text x="30" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#E2E8F0" text-anchor="middle">Python</text>
      <rect x="68" y="0" width="40" height="22" rx="11" fill="#2E1065" stroke="#7C3AED" stroke-width="0.8"/>
      <text x="88" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#C084FC" text-anchor="middle">ML</text>
      <rect x="116" y="0" width="126" height="22" rx="11" fill="#0C4A6E" stroke="#0284C7" stroke-width="0.8"/>
      <text x="179" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#7DD3FC" text-anchor="middle">Chrome Extension</text>
    </g>
  </g>

  <!-- Card 3: DrugGuard Detection System -->
  <g transform="translate(28, 194)">
    <rect x="0" y="0" width="402" height="126" rx="12" fill="url(#card-inner-bg)" stroke="url(#card-inner-border)" stroke-width="1"/>

    <!-- Icon Container -->
    <circle cx="34" cy="34" r="16" fill="#064E3B" stroke="#059669" stroke-width="1"/>
    <!-- Shield Icon -->
    <path d="M9 1L2 4V8.5C2 13 5 17 9 18C13 17 16 13 16 8.5V4L9 1Z" stroke="#34D399" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" fill="none" transform="translate(25, 25) scale(0.95)"/>

    <!-- Title & External Link -->
    <text x="62" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" font-weight="700" fill="#FFFFFF">DrugGuard Detection System</text>
    <text x="382" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#818CF8" text-anchor="end">↗</text>

    <!-- Description -->
    <text x="62" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400" fill="#94A3B8">AI-based drug detection and classification</text>
    <text x="62" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400" fill="#94A3B8">system using deep learning.</text>

    <!-- Tags -->
    <g transform="translate(62, 88)">
      <rect width="60" height="22" rx="11" fill="#1E293B" stroke="#475569" stroke-width="0.8"/>
      <text x="30" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#E2E8F0" text-anchor="middle">Python</text>
      <rect x="68" y="0" width="86" height="22" rx="11" fill="#451A03" stroke="#D97706" stroke-width="0.8"/>
      <text x="111" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#FCD34D" text-anchor="middle">TensorFlow</text>
    </g>
  </g>

  <!-- Card 4: Smart Sheet Metal Fabrication (AIoT) -->
  <g transform="translate(450, 194)">
    <rect x="0" y="0" width="402" height="126" rx="12" fill="url(#card-inner-bg)" stroke="url(#card-inner-border)" stroke-width="1"/>

    <!-- Icon Container -->
    <circle cx="34" cy="34" r="16" fill="#172554" stroke="#2563EB" stroke-width="1"/>
    <!-- Manufacturing Wave / Machinery Icon -->
    <path d="M1 9L4 6L8 10L14 3L18 7" stroke="#60A5FA" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" transform="translate(25, 27) scale(0.95)"/>

    <!-- Title & External Link -->
    <text x="62" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" font-weight="700" fill="#FFFFFF">Smart Sheet Metal Fabrication (AIoT)</text>
    <text x="382" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#818CF8" text-anchor="end">↗</text>

    <!-- Description -->
    <text x="62" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400" fill="#94A3B8">AIoT &amp; IIoT based sheet-metal panel fabrication</text>
    <text x="62" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400" fill="#94A3B8">and quality inspection system.</text>

    <!-- Tags -->
    <g transform="translate(62, 88)">
      <rect width="42" height="22" rx="11" fill="#1E293B" stroke="#475569" stroke-width="0.8"/>
      <text x="21" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#E2E8F0" text-anchor="middle">IoT</text>
      <rect x="50" y="0" width="38" height="22" rx="11" fill="#2E1065" stroke="#7C3AED" stroke-width="0.8"/>
      <text x="69" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#C084FC" text-anchor="middle">AI</text>
      <rect x="96" y="0" width="102" height="22" rx="11" fill="#064E3B" stroke="#059669" stroke-width="0.8"/>
      <text x="147" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#6EE7B7" text-anchor="middle">Manufacturing</text>
      <rect x="206" y="0" width="62" height="22" rx="11" fill="#3B0764" stroke="#9333EA" stroke-width="0.8"/>
      <text x="237" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#D8B4FE" text-anchor="middle">Quality</text>
    </g>
  </g>
</svg>'''
    return svg


def create_wakatime_svg(data=None):
    # Check if real data provided or fallback
    has_data = data is not None and data.get("status") == "connected"

    hours_recorded = data.get("hours_recorded", "120+ hrs") if has_data else "~120+ hrs recorded"
    active_project = data.get("active_project", "Campus-Canteen") if has_data else "Working on Campus-Canteen"
    primary_lang = data.get("primary_lang", "TypeScript & Python") if has_data else "Mostly coding in TypeScript"
    daily_avg = data.get("daily_avg", "2.5 hrs/day") if has_data else "~2 hrs of coding per day"
    editor = data.get("editor", "VS Code") if has_data else "Coding with VS Code"
    os_name = data.get("os", "Windows") if has_data else "Using Windows"

    projects = data.get("projects", [
        {"name": "Campus-Canteen", "percent": 45},
        {"name": "DrugGuard", "percent": 32},
        {"name": "AIoT-Fabrication", "percent": 15},
        {"name": "Portfolio-Lab", "percent": 5},
        {"name": "Other", "percent": 3}
    ]) if has_data else [
        {"name": "Campus-Canteen", "percent": 42},
        {"name": "DrugGuard-System", "percent": 35},
        {"name": "AIoT-project", "percent": 16},
        {"name": "Student-Dashboard", "percent": 4},
        {"name": "the-Honored-One", "percent": 3}
    ]

    languages = data.get("languages", [
        {"name": "TypeScript", "percent": 40},
        {"name": "Python", "percent": 30},
        {"name": "JavaScript", "percent": 15},
        {"name": "HTML/CSS", "percent": 10},
        {"name": "Other", "percent": 5}
    ]) if has_data else [
        {"name": "TypeScript", "percent": 38},
        {"name": "Python", "percent": 32},
        {"name": "JavaScript", "percent": 18},
        {"name": "HTML & CSS", "percent": 9},
        {"name": "Java", "percent": 3}
    ]

    # Generate projects rows
    proj_rows = ""
    for idx, p in enumerate(projects[:5]):
        y = idx * 20
        proj_rows += f'''<g transform="translate(0, {y})">
      <text x="0" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" fill="#94A3B8">{p["name"][:14]}</text>
      <rect x="94" y="3" width="50" height="7" rx="3.5" fill="#1E293B"/>
      <rect x="94" y="3" width="{max(3, int(p["percent"] * 0.5))}" height="7" rx="3.5" fill="#8B5CF6"/>
      <text x="150" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#CBD5E1">{p["percent"]}%</text>
    </g>\n'''

    # Generate languages rows
    lang_rows = ""
    for idx, l in enumerate(languages[:5]):
        y = idx * 20
        lang_rows += f'''<g transform="translate(0, {y})">
      <text x="0" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" fill="#94A3B8">{l["name"][:12]}</text>
      <rect x="80" y="3" width="50" height="7" rx="3.5" fill="#1E293B"/>
      <rect x="80" y="3" width="{max(3, int(l["percent"] * 0.5))}" height="7" rx="3.5" fill="#3B82F6"/>
      <text x="136" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#CBD5E1">{l["percent"]}%</text>
    </g>\n'''

    svg = f'''<svg width="880" height="190" viewBox="0 0 880 190" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="waka-bg" x1="0" y1="0" x2="880" y2="190" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#080C14" />
    </linearGradient>
    <linearGradient id="waka-border" x1="0" y1="0" x2="880" y2="190" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#2D3748" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.8" />
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="878" height="188" rx="14" fill="url(#waka-bg)" stroke="url(#waka-border)" stroke-width="1.2" />

  <!-- Section Header -->
  <g transform="translate(28, 22)">
    <circle cx="8" cy="8" r="7" stroke="#E2E8F0" stroke-width="1.5" fill="none"/>
    <polyline points="8,4 8,8 11,8" stroke="#E2E8F0" stroke-width="1.5" stroke-linecap="round"/>
    <text x="26" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="600" fill="#FFFFFF">WakaTime</text>
    <text x="824" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#818CF8" text-anchor="end">↗</text>
  </g>

  <!-- 4 Columns Grid -->
  <g transform="translate(28, 60)">
    <!-- Col 1: Overview Summary -->
    <g transform="translate(0, 0)">
      <text x="24" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="600" fill="#C084FC">WakaTime Activity</text>
      
      <!-- Metric 1: Hours -->
      <g transform="translate(0, 26)">
        <circle cx="9" cy="9" r="6" stroke="#94A3B8" stroke-width="1.2" fill="none"/>
        <polyline points="9,6 9,9 11,9" stroke="#94A3B8" stroke-width="1.2" stroke-linecap="round"/>
        <text x="24" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" fill="#E2E8F0">{hours_recorded}</text>
      </g>
      <!-- Metric 2: Active Project -->
      <g transform="translate(0, 52)">
        <rect x="2" y="3" width="13" height="10" rx="2" stroke="#94A3B8" stroke-width="1.2" fill="none"/>
        <line x1="1" y1="13" x2="16" y2="13" stroke="#94A3B8" stroke-width="1.2" stroke-linecap="round"/>
        <text x="24" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" fill="#E2E8F0">{active_project}</text>
      </g>
      <!-- Metric 3: Primary Language -->
      <g transform="translate(0, 78)">
        <rect x="3" y="2" width="11" height="13" rx="1.5" stroke="#94A3B8" stroke-width="1.2" fill="none"/>
        <line x1="5" y1="6" x2="11" y2="6" stroke="#94A3B8" stroke-width="1"/>
        <line x1="5" y1="9" x2="11" y2="9" stroke="#94A3B8" stroke-width="1"/>
        <text x="24" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" fill="#E2E8F0">{primary_lang}</text>
      </g>
    </g>

    <!-- Col 2: Environment / Daily Rate -->
    <g transform="translate(230, 0)">
      <!-- Metric 1: Daily Average -->
      <g transform="translate(0, 26)">
        <path d="M1 9L4 5L7 8L11 2L14 6" stroke="#94A3B8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        <text x="24" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" fill="#E2E8F0">{daily_avg}</text>
      </g>
      <!-- Metric 2: Editor -->
      <g transform="translate(0, 52)">
        <path d="M4 2L1 8L4 14M11 2L14 8L11 14" stroke="#94A3B8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        <text x="24" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" fill="#E2E8F0">{editor}</text>
      </g>
      <!-- Metric 3: OS -->
      <g transform="translate(0, 78)">
        <rect x="2" y="2" width="12" height="10" rx="1.5" stroke="#94A3B8" stroke-width="1.2" fill="none"/>
        <line x1="5" y1="14" x2="11" y2="14" stroke="#94A3B8" stroke-width="1.2"/>
        <line x1="8" y1="12" x2="8" y2="14" stroke="#94A3B8" stroke-width="1.2"/>
        <text x="24" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" fill="#E2E8F0">{os_name}</text>
      </g>
    </g>

    <!-- Divider -->
    <line x1="425" y1="10" x2="425" y2="105" stroke="#1E293B" stroke-width="1.2"/>

    <!-- Col 3: Projects Activity -->
    <g transform="translate(450, 0)">
      <text x="0" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="600" fill="#E2E8F0">Projects activity</text>
      <g transform="translate(0, 26)">
        {proj_rows}
      </g>
    </g>

    <!-- Col 4: Language Activity -->
    <g transform="translate(650, 0)">
      <text x="0" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="600" fill="#E2E8F0">Language activity</text>
      <g transform="translate(0, 26)">
        {lang_rows}
      </g>
    </g>
  </g>
</svg>'''
    return svg


def create_github_stats_svg(data=None):
    if not data:
        data = {
            "total_contributions": "1,200+",
            "current_streak": "42 days",
            "longest_streak": "85 days",
            "repositories": "14+",
            "stars_earned": "10+"
        }

    # Generate Contribution Heatmap Grid
    # 24 columns (weeks) x 7 rows (days)
    months = ["Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
    # Purple palette shades
    shades = ["#161B22", "#2E1065", "#4C1D95", "#6D28D9", "#8B5CF6", "#C084FC"]
    import random
    # Deterministic pseudo-random seed for heatmap pattern matching the image
    random.seed(42)

    grid_cells = ""
    for col in range(22):
        for row in range(7):
            x = col * 15
            y = row * 15
            # Distribution with realistic clusters
            prob = random.random()
            if prob < 0.25:
                color = shades[0]
            elif prob < 0.50:
                color = shades[1]
            elif prob < 0.70:
                color = shades[2]
            elif prob < 0.85:
                color = shades[3]
            elif prob < 0.95:
                color = shades[4]
            else:
                color = shades[5]
            grid_cells += f'<rect x="{x}" y="{y}" width="11" height="11" rx="2.5" fill="{color}"/>\n'

    months_labels = ""
    for i, m in enumerate(months):
        x = i * 58
        months_labels += f'<text x="{x}" y="0" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif" font-size="11" fill="#94A3B8">{m}</text>\n'

    svg = f'''<svg width="880" height="230" viewBox="0 0 880 230" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gs-card-bg" x1="0" y1="0" x2="300" y2="230" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#080C14" />
    </linearGradient>
    <linearGradient id="gs-card-border" x1="0" y1="0" x2="300" y2="230" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#2D3748" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.8" />
    </linearGradient>
    <linearGradient id="ca-card-bg" x1="0" y1="0" x2="560" y2="230" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#080C14" />
    </linearGradient>
  </defs>

  <!-- Left Card: GitHub Stats -->
  <g transform="translate(0, 0)">
    <rect x="1" y="1" width="308" height="228" rx="14" fill="url(#gs-card-bg)" stroke="url(#gs-card-border)" stroke-width="1.2" />

    <!-- Card Title -->
    <g transform="translate(24, 22)">
      <!-- Bar Chart Icon -->
      <path d="M1 12H3V4H1V12ZM5 12H7V1H5V12ZM9 12H11V7H9V12ZM13 12H15V9H13V12Z" fill="#E2E8F0"/>
      <text x="24" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="600" fill="#FFFFFF">GitHub Stats</text>
    </g>

    <!-- Stats Rows -->
    <g transform="translate(24, 60)">
      <!-- Row 1: Total Contributions -->
      <g transform="translate(0, 0)">
        <rect x="0" y="2" width="13" height="13" rx="2.5" fill="#2E1065" stroke="#7C3AED" stroke-width="0.8"/>
        <text x="22" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" fill="#94A3B8">Total Contributions</text>
        <text x="260" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="end">{data.get("total_contributions", "1,200+")}</text>
      </g>
      <!-- Row 2: Current Streak -->
      <g transform="translate(0, 28)">
        <circle cx="6.5" cy="8.5" r="5.5" stroke="#94A3B8" stroke-width="1.2" fill="none"/>
        <polyline points="6.5,5.5 6.5,8.5 8.5,8.5" stroke="#94A3B8" stroke-width="1.2" stroke-linecap="round"/>
        <text x="22" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" fill="#94A3B8">Current Streak</text>
        <text x="260" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="end">{data.get("current_streak", "42 days")}</text>
      </g>
      <!-- Row 3: Longest Streak -->
      <g transform="translate(0, 56)">
        <circle cx="6.5" cy="8.5" r="5.5" stroke="#94A3B8" stroke-width="1.2" fill="none"/>
        <polyline points="6.5,5.5 6.5,8.5 8.5,8.5" stroke="#94A3B8" stroke-width="1.2" stroke-linecap="round"/>
        <text x="22" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" fill="#94A3B8">Longest Streak</text>
        <text x="260" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="end">{data.get("longest_streak", "85 days")}</text>
      </g>
      <!-- Row 4: Repositories -->
      <g transform="translate(0, 84)">
        <rect x="0" y="2" width="13" height="11" rx="2" stroke="#94A3B8" stroke-width="1.2" fill="none"/>
        <text x="22" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" fill="#94A3B8">Repositories</text>
        <text x="260" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="end">{data.get("repositories", "14+")}</text>
      </g>
      <!-- Row 5: Stars Earned -->
      <g transform="translate(0, 112)">
        <polygon points="6.5,1 8.5,5.5 13,6 9.5,9.5 10.5,14 6.5,11.5 2.5,14 3.5,9.5 0,6 4.5,5.5" stroke="#94A3B8" stroke-width="1.1" fill="none"/>
        <text x="22" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" fill="#94A3B8">Stars Earned</text>
        <text x="260" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="end">{data.get("stars_earned", "10+")}</text>
      </g>
    </g>
  </g>

  <!-- Right Card: Contribution Activity Heatmap -->
  <g transform="translate(324, 0)">
    <rect x="1" y="1" width="554" height="228" rx="14" fill="url(#ca-card-bg)" stroke="url(#gs-card-border)" stroke-width="1.2" />

    <!-- Card Title -->
    <g transform="translate(24, 22)">
      <!-- GitHub Logo -->
      <path fill-rule="evenodd" clip-rule="evenodd" d="M6 0C2.69 0 0 2.74 0 6.12C0 8.83 1.73 11.12 4.14 11.94C4.44 12 4.55 11.81 4.55 11.65C4.55 11.51 4.54 11 4.54 10.43C3 10.71 2.65 10.02 2.53 9.68C2.46 9.5 2.16 8.94 1.9 8.79C1.68 8.67 1.37 8.37 1.89 8.36C2.38 8.35 2.73 8.82 2.85 9.01C3.41 9.98 4.31 9.71 4.66 9.54C4.72 9.13 4.88 8.85 5.06 8.69C3.68 8.53 2.24 7.98 2.24 5.56C2.24 4.87 2.48 4.29 2.87 3.84C2.81 3.68 2.59 3.03 2.93 2.15C2.93 2.15 3.45 1.98 4.65 2.81C5.15 2.67 5.68 2.6 6.21 2.6C6.74 2.6 7.27 2.67 7.77 2.81C8.97 1.97 9.49 2.15 9.49 2.15C9.83 3.03 9.61 3.68 9.55 3.84C9.94 4.29 10.18 4.86 10.18 5.56C10.18 7.99 8.73 8.53 7.35 8.69C7.58 8.89 7.78 9.28 7.78 9.89C7.78 10.76 7.77 11.47 7.77 11.65C7.77 11.81 7.88 12.01 8.18 11.94C10.59 11.12 12.32 8.82 12.32 6.12C12.32 2.74 9.63 0 6.32 0H6Z" fill="#E2E8F0" transform="translate(0, 0) scale(1.1)"/>
      <text x="24" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="600" fill="#FFFFFF">Contribution Activity</text>
    </g>

    <!-- Heatmap Grid Area -->
    <g transform="translate(24, 56)">
      <!-- Day Labels on Left -->
      <g transform="translate(0, 24)">
        <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" fill="#64748B">Mon</text>
        <text x="0" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" fill="#64748B">Wed</text>
        <text x="0" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" fill="#64748B">Fri</text>
      </g>

      <!-- Month Labels on Top -->
      <g transform="translate(36, 12)">
        {months_labels}
      </g>

      <!-- Squares Grid -->
      <g transform="translate(36, 22)">
        {grid_cells}
      </g>
    </g>

    <!-- Right Highlight Badge -->
    <g transform="translate(415, 68)">
      <rect x="0" y="0" width="118" height="114" rx="12" fill="#111625" stroke="#334155" stroke-width="1"/>
      <text x="59" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500" fill="#94A3B8" text-anchor="middle">Active Streak</text>
      <text x="59" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" fill="#A855F7" text-anchor="middle">98%</text>
      <text x="59" y="92" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#CBD5E1" text-anchor="middle">Consistency</text>
    </g>
  </g>
</svg>'''
    return svg


def main():
    print("Generating assets...")
    with open(os.path.join(ASSETS_DIR, "header.svg"), "w", encoding="utf-8") as f:
        f.write(create_header_svg())
    print("Created header.svg")

    with open(os.path.join(ASSETS_DIR, "about.svg"), "w", encoding="utf-8") as f:
        f.write(create_about_svg())
    print("Created about.svg")

    with open(os.path.join(ASSETS_DIR, "expertise.svg"), "w", encoding="utf-8") as f:
        f.write(create_expertise_svg())
    print("Created expertise.svg")

    with open(os.path.join(ASSETS_DIR, "tech-stack.svg"), "w", encoding="utf-8") as f:
        f.write(create_tech_stack_svg())
    print("Created tech-stack.svg")

    with open(os.path.join(ASSETS_DIR, "languages.svg"), "w", encoding="utf-8") as f:
        f.write(create_languages_svg())
    print("Created languages.svg")

    with open(os.path.join(ASSETS_DIR, "projects.svg"), "w", encoding="utf-8") as f:
        f.write(create_projects_svg())
    print("Created projects.svg")

    with open(os.path.join(ASSETS_DIR, "wakatime.svg"), "w", encoding="utf-8") as f:
        f.write(create_wakatime_svg())
    print("Created wakatime.svg")

    with open(os.path.join(ASSETS_DIR, "github-stats.svg"), "w", encoding="utf-8") as f:
        f.write(create_github_stats_svg())
    print("Created github-stats.svg")

    print("All assets successfully generated!")


if __name__ == "__main__":
    main()
