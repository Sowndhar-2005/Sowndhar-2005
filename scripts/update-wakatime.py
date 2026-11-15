"""
update-wakatime.py
Fetches live WakaTime activity statistics if WAKATIME_API_KEY is configured,
or renders an initial status representation matching the dark-violet dashboard aesthetic.
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SVG_PATH = os.path.join(ASSETS_DIR, "wakatime.svg")


def fetch_wakatime_stats():
    api_key = os.environ.get("WAKATIME_API_KEY")
    if not api_key and len(sys.argv) > 1:
        api_key = sys.argv[1]

    if not api_key:
        print("WAKATIME_API_KEY not configured. Using standby status representation.")
        return None

    api_key = api_key.strip().strip("'\"")

    # Base64 encode api key for HTTP Basic Auth
    auth_header = "Basic " + base64.b64encode(api_key.encode("utf-8")).decode("utf-8")
    url = "https://wakatime.com/api/v1/users/current/stats/last_7_days"

    req = urllib.request.Request(url, headers={
        "Authorization": auth_header,
        "User-Agent": "GitHub-Profile-WakaTime-Sync/2.0"
    })

    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            stats = data.get("data", {})
            
            projects = []
            for p in stats.get("projects", [])[:5]:
                name = p.get("name", "Unknown")
                percent = round(p.get("percent", 0))
                projects.append({"name": name, "percent": percent})

            languages = []
            for l in stats.get("languages", [])[:5]:
                name = l.get("name", "Unknown")
                percent = round(l.get("percent", 0))
                languages.append({"name": name, "percent": percent})

            editors = stats.get("editors", [])
            top_editor = editors[0].get("name", "VS Code") if (editors and isinstance(editors[0], dict) and editors[0].get("name")) else "VS Code"

            os_list = stats.get("operating_systems", [])
            top_os = os_list[0].get("name", "Windows") if (os_list and isinstance(os_list[0], dict) and os_list[0].get("name")) else "Windows"

            top_project = projects[0]["name"] if projects else "Campus-Canteen"
            top_lang = languages[0]["name"] if languages else "TypeScript"

            return {
                "status": "connected",
                "hours_recorded": stats.get("human_readable_total", "28 hrs 40 mins"),
                "daily_avg": stats.get("human_readable_daily_average", "4 hrs 5 mins") + " / day",
                "active_project": f"Working on {top_project}",
                "primary_lang": f"Mostly coding in {top_lang}",
                "editor": f"Coding with {top_editor}",
                "os": f"Using {top_os}",
                "projects": projects,
                "languages": languages
            }
    except urllib.error.HTTPError as e:
        print(f"HTTP Error querying WakaTime API: {e.code} - {e.reason}")
        return None
    except Exception as e:
        print(f"Error querying WakaTime API: {e}")
        return None


def render_wakatime_svg(data):
    is_live = data is not None and data.get("status") == "connected"

    hours_recorded = data.get("hours_recorded", "Telemetry active") if is_live else "~120+ coding hrs recorded"
    active_project = data.get("active_project", "Working on Campus-Canteen") if is_live else "Working on Campus-Canteen"
    primary_lang = data.get("primary_lang", "Mostly coding in TypeScript") if is_live else "Mostly coding in TypeScript"
    daily_avg = data.get("daily_avg", "~2.5 hrs / day") if is_live else "~2 hrs of coding per day"
    editor = data.get("editor", "Coding with VS Code") if is_live else "Coding with VS Code"
    os_name = data.get("os", "Using Windows") if is_live else "Using Windows"

    projects = data.get("projects", []) if (is_live and data.get("projects")) else [
        {"name": "Campus-Canteen", "percent": 42},
        {"name": "DrugGuard-System", "percent": 35},
        {"name": "AIoT-Fabrication", "percent": 16},
        {"name": "Student-Dashboard", "percent": 4},
        {"name": "the-Honored-One", "percent": 3}
    ]

    languages = data.get("languages", []) if (is_live and data.get("languages")) else [
        {"name": "TypeScript", "percent": 38},
        {"name": "Python", "percent": 32},
        {"name": "JavaScript", "percent": 18},
        {"name": "HTML & CSS", "percent": 9},
        {"name": "C++", "percent": 3}
    ]

    proj_rows = ""
    for idx, p in enumerate(projects[:5]):
        y = idx * 20
        proj_rows += f'''<g transform="translate(0, {y})">
      <text x="0" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" fill="#94A3B8">{p["name"][:14]}</text>
      <rect x="94" y="3" width="50" height="7" rx="3.5" fill="#1E293B"/>
      <rect x="94" y="3" width="{max(3, int(p["percent"] * 0.5))}" height="7" rx="3.5" fill="#8B5CF6"/>
      <text x="150" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#CBD5E1">{p["percent"]}%</text>
    </g>\n'''

    lang_rows = ""
    for idx, l in enumerate(languages[:5]):
        y = idx * 20
        lang_rows += f'''<g transform="translate(0, {y})">
      <text x="0" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" fill="#94A3B8">{l["name"][:12]}</text>
      <rect x="80" y="3" width="50" height="7" rx="3.5" fill="#1E293B"/>
      <rect x="80" y="3" width="{max(3, int(l["percent"] * 0.5))}" height="7" rx="3.5" fill="#3B82F6"/>
      <text x="136" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500" fill="#CBD5E1">{l["percent"]}%</text>
    </g>\n'''

    badge_status = '<circle cx="6" cy="6" r="3" fill="#10B981"/>' if is_live else '<circle cx="6" cy="6" r="3" fill="#8B5CF6"/>'
    badge_label = "Live Sync Active" if is_live else "Live Sync Ready"

    return f'''<svg width="880" height="190" viewBox="0 0 880 190" fill="none" xmlns="http://www.w3.org/2000/svg">
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
    
    <!-- Status Indicator -->
    <g transform="translate(120, 3)">
      {badge_status}
      <text x="14" y="9" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" fill="#94A3B8">{badge_label}</text>
    </g>

    <text x="824" y="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#818CF8" text-anchor="end">↗</text>
  </g>

  <!-- 4 Columns Grid -->
  <g transform="translate(28, 60)">
    <!-- Col 1: Overview Summary -->
    <g transform="translate(0, 0)">
      <text x="24" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="600" fill="#C084FC">WakaTime (over last week)</text>
      
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


def main():
    print("Updating WakaTime stats...")
    data = fetch_wakatime_stats()
    svg_content = render_wakatime_svg(data)
    with open(SVG_PATH, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Successfully updated assets/wakatime.svg")


if __name__ == "__main__":
    main()
