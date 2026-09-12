#!/usr/bin/env python3
"""Generate a machine-readable index of the catalog.

Extracts the front-matter from every valid catalog item and compiles it into
`catalog/index.json`.

Usage:
    python3 scripts/generate_index.py
"""
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: pip install -r scripts/requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"
INDEX_FILE = CATALOG / "index.json"
AREAS = ["engineering", "database", "devops", "security", "data-ai", "business", "qa", "design-ux", "content", "legal"]
TOOL_TYPES = [
    "claude/agents", "claude/skills", "claude/mcp", "claude/hooks",
    "codex/agents-md", "codex/prompts",
    "antigravity/agents", "antigravity/skills", "antigravity/mcp", "antigravity/hooks"
]
SKIP_FILES = {"README.md", ".gitkeep"}
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def find_items():
    for area in AREAS:
        for t in TOOL_TYPES:
            d = CATALOG / area / t
            if not d.is_dir():
                continue
            for f in sorted(d.rglob("*.md")):
                if f.name in SKIP_FILES:
                    continue
                yield f, area, t


def extract_data(path, area, t):
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None

    try:
        data = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None

    if not isinstance(data, dict):
        return None
        
    tool_platform, item_type = t.split("/", 1)
    
    # Standardize data structure
    entry = {
        "id": f"{area}/{tool_platform}/{item_type}/{path.stem}",
        "name": data.get("name", path.stem),
        "area": area,
        "platform": tool_platform,
        "type": item_type,
        "status": data.get("status", "experimental"),
        "context": data.get("context", ""),
        "description": data.get("description", ""),
        "file": str(path.relative_to(ROOT))
    }
    
    if "tools" in data:
        entry["tools"] = data["tools"]
    if "model" in data:
        entry["model"] = data["model"]
    
    return entry


def main():
    items = list(find_items())
    catalog_index = []
    
    for path, area, t in items:
        data = extract_data(path, area, t)
        if data:
            catalog_index.append(data)

    with INDEX_FILE.open("w", encoding="utf-8") as f:
        json.dump(catalog_index, f, indent=2, ensure_ascii=False)
        
    print(f"Generated {INDEX_FILE.relative_to(ROOT)} with {len(catalog_index)} items.")


if __name__ == "__main__":
    main()
