#!/usr/bin/env python3
"""
Validate research JSON and print the output path for mobile app plans.
"""
import json
import sys

def main():
    try:
        data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, IndexError):
        print("❌ Invalid JSON input", file=sys.stderr)
        sys.exit(1)

    required = ["app_name"]
    missing = [k for k in required if k not in data]
    if missing:
        print(f"❌ Missing fields: {missing}", file=sys.stderr)
        sys.exit(1)

    name_slug = data["app_name"].lower().replace(" ", "-").replace(":", "")
    output_path = f"steve_app_ideas/{name_slug}.md"
    print(json.dumps({
        "valid": True,
        "app_name": data["app_name"],
        "output_path": output_path
    }))

if __name__ == "__main__":
    main()
