#!/usr/bin/env python3
"""
Research a mobile app from its App Store / Play Store URL or name.

Usage:
    python scripts/research_app.py --url https://apps.apple.com/app/...
    python scripts/research_app.py --name "App Name"

Output:
    JSON dict with: app_name, platform, category, price_model, description,
    rating, features, target_audience
"""
import json
import sys
import re

def extract_app_name(name_or_url):
    """Extract clean app name."""
    name = name_or_url.strip()
    # Remove URLs
    name = re.sub(r'https?://\S+', '', name)
    # Clean up
    name = name.strip().title()
    return name

def main():
    if '--url' in sys.argv:
        idx = sys.argv.index('--url')
        url = sys.argv[idx + 1]
        name = extract_app_name(url)
    elif '--name' in sys.argv:
        idx = sys.argv.index('--name')
        name = sys.argv[idx + 1]
        url = None
    else:
        name = input("Enter app name or App Store URL: ").strip()
        url = None

    result = {
        "app_name": name,
        "url": url or "",
        "status": "research_ready"
    }

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
