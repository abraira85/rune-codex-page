#!/usr/bin/env python3
"""
Rune Codex Page - CLI Explorer

Usage:
  python3 scripts/rune-search.py [query]
"""
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_FILE = ROOT / "catalog" / "index.json"

def main():
    if not INDEX_FILE.exists():
        sys.exit("Error: catalog/index.json not found. Run python3 scripts/generate_index.py first.")
        
    query = sys.argv[1].lower() if len(sys.argv) > 1 else ""
    
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    items = data
    results = []
    
    for item in items:
        searchable_text = f"{item.get('name', '')} {item.get('description', '')} {item.get('area', '')} {item.get('type', '')}".lower()
        if query in searchable_text:
            results.append(item)
            
    print(f"Found {len(results)} items matching '{query}':\n")
    
    for item in results:
        print(f"[{item['area'].upper()}] {item['name']}")
        print(f"  Path: catalog/{item['area']}/{item['platform']}/{item['type']}/{item['name']}")
        if item.get("description"):
            print(f"  Desc: {item['description']}")
        print("-" * 40)

if __name__ == "__main__":
    main()
