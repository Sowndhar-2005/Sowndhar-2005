"""
update-languages.py
Fetches actual language statistics from GitHub API for user Sowndhar-2005,
calculates percentages, file sizes, and updates assets/languages.svg.
"""

import os
import sys
import json
import urllib.request

USERNAME = "Sowndhar-2005"
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SVG_PATH = os.path.join(ASSETS_DIR, "languages.svg")

# GitHub language colors palette
LANG_COLORS = {
    "TypeScript": "#3178C6",
    "JavaScript": "#F7DF1E",
    "Python": "#3776AB",
    "HTML": "#E34F26",
    "Jupyter Notebook": "#DA5B0B",
    "CSS": "#563D7C",
    "Java": "#B07219",
    "C++": "#F34B7D",
    "C": "#555555",
    "Rust": "#DEA584",
    "Go": "#00ADD8",
    "C#": "#178600",
    "SCSS": "#C6538C",
    "Shell": "#89E051",
    "Dockerfile": "#384D54"
}

FALLBACK_LANGS = [
    {"name": "TypeScript", "bytes": 1195966, "color": "#3178C6", "lines": "4.2k lines"},
    {"name": "JavaScript", "bytes": 1041693, "color": "#F7DF1E", "lines": "3.8k lines"},
    {"name": "Python", "bytes": 911704, "color": "#3776AB", "lines": "3.2k lines"},
    {"name": "HTML", "bytes": 375237, "color": "#E34F26", "lines": "1.3k lines"},
    {"name": "Jupyter Notebook", "bytes": 258377, "color": "#DA5B0B", "lines": "920 lines"},
    {"name": "CSS", "bytes": 253238, "color": "#563D7C", "lines": "890 lines"},
    {"name": "Java", "bytes": 14341, "color": "#B07219", "lines": "180 lines"}
]


def fmt_bytes(b):
    if b >= 1048576:
        return f"{b/1048576:.2f} MB"
    elif b >= 1024:
        return f"{b/1024:.1f} KB"
    return f"{b} bytes"


def fetch_github_languages():
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"User-Agent": "GitHub-Profile-Updater"}
    if token:
        headers["Authorization"] = f"token {token}"

    repos_url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
    req = urllib.request.Request(repos_url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            repos = json.loads(resp.read().decode())
    except Exception as e:
        print(f"Failed to fetch repos: {e}. Using verified data.")
        return None

    lang_totals = {}
    for r in repos:
        # Skip forks if any
        if r.get("fork"):
            continue
        l_url = r.get("languages_url")
        if not l_url:
            continue
        req_l = urllib.request.Request(l_url, headers=headers)
        try:
            with urllib.request.urlopen(req_l, timeout=10) as resp_l:
                langs = json.loads(resp_l.read().decode())
                for name, b in langs.items():
                    lang_totals[name] = lang_totals.get(name, 0) + b
        except Exception:
            pass

    if not lang_totals:
        return None

    total_bytes = sum(lang_totals.values())
    sorted_langs = sorted(lang_totals.items(), key=lambda x: x[1], reverse=True)

    result = []
    for name, b in sorted_langs:
        # Approximate lines from bytes (~35 bytes per line average in code)
        est_lines = max(10, round(b / 35))
        if est_lines >= 1000:
            lines_str = f"{est_lines/1000:.1f}k lines"
        else:
            lines_str = f"{est_lines} lines"

        result.append({
            "name": name,
            "bytes": b,
            "color": LANG_COLORS.get(name, "#8B5CF6"),
            "lines": lines_str
        })

    return {
        "total_bytes": total_bytes,
        "total_languages": len(sorted_langs),
        "repos_count": len(repos),
        "languages": result
    }


def render_languages_svg(data):
    total_bytes = data["total_bytes"]
    top_langs = data["languages"][:6]

    bar_width = 824
    segments_svg = ""
    curr_x = 0
    for idx, l in enumerate(top_langs):
        w = max(4, round((l["bytes"] / total_bytes) * bar_width))
        if curr_x + w > bar_width or idx == len(top_langs) - 1:
            w = bar_width - curr_x
        segments_svg += f'<rect x="{curr_x}" y="0" width="{w}" height="10" fill="{l["color"]}" />\n'
        curr_x += w
        if curr_x >= bar_width:
            break

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
    repos_cnt = data.get("repos_count", 14)

    return f'''<svg width="880" height="210" viewBox="0 0 880 210" fill="none" xmlns="http://www.w3.org/2000/svg">
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
    <path d="M1 2C1 1.45 1.45 1 2 1H14C14.55 1 15 1.45 15 2V12C15 12.55 14.55 13 14 13H2C1.45 13 1 12.55 1 12V2ZM3.5 4.5L6.5 7L3.5 9.5M8 9.5H12.5" stroke="#E2E8F0" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <text x="26" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="600" fill="#FFFFFF">Most Used Languages</text>
    <text x="824" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#818CF8" text-anchor="end">{total_count} Languages ↗</text>
  </g>

  <!-- Subtitle -->
  <text x="28" y="62" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400" fill="#94A3B8">Estimation from {size_formatted} of code across {repos_cnt} repositories</text>

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


def main():
    print("Updating language statistics...")
    data = fetch_github_languages()
    if not data:
        data = {
            "total_bytes": sum(l["bytes"] for l in FALLBACK_LANGS),
            "total_languages": len(FALLBACK_LANGS),
            "repos_count": 14,
            "languages": FALLBACK_LANGS
        }
    svg_content = render_languages_svg(data)
    with open(SVG_PATH, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Successfully updated assets/languages.svg")


if __name__ == "__main__":
    main()
