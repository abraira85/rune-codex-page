#!/usr/bin/env python3
"""Validate front-matter on every item under claude/ and codex/.

Runs in CI on every push/PR (see .github/workflows/validate.yml) and can be
run locally with `python3 scripts/validate.py` before opening a PR.
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: pip install -r scripts/requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
CATALOG = "catalog"
AREAS = ["engineering", "database", "devops", "security", "data-ai", "business", "qa"]
TOOL_TYPES = ["claude/agents", "claude/skills", "claude/mcp", "claude/hooks",
              "codex/agents-md", "codex/prompts"]
ITEM_DIRS = [f"{CATALOG}/{area}/{t}" for area in AREAS for t in TOOL_TYPES]
SKIP_FILES = {"README.md", ".gitkeep"}
REQUIRED_KEYS = {"name", "status", "context"}
VALID_STATUS = {"production", "experimental"}
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def find_items():
    for rel in ITEM_DIRS:
        d = ROOT / rel
        if not d.is_dir():
            continue
        for f in sorted(d.rglob("*.md")):
            if f.name in SKIP_FILES:
                continue
            yield f


def validate_file(path):
    errors = []
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return [f"{path}: missing YAML front-matter (must start with '---')"]

    try:
        data = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return [f"{path}: invalid YAML front-matter ({e})"]

    if not isinstance(data, dict):
        return [f"{path}: front-matter must be a mapping"]

    missing = REQUIRED_KEYS - data.keys()
    if missing:
        errors.append(f"{path}: missing required key(s): {', '.join(sorted(missing))}")

    status = data.get("status")
    if status is not None and status not in VALID_STATUS:
        errors.append(f"{path}: status must be one of {sorted(VALID_STATUS)}, got {status!r}")

    context = data.get("context")
    if context is not None and (not isinstance(context, str) or not context.strip()):
        errors.append(f"{path}: context must be a non-empty string")

    return errors


def main():
    items = list(find_items())
    all_errors = []
    for item in items:
        all_errors.extend(validate_file(item))

    print(f"Checked {len(items)} item(s) across {len(AREAS)} area(s) x {len(TOOL_TYPES)} type(s).")
    if all_errors:
        print(f"\n{len(all_errors)} problem(s) found:\n")
        for err in all_errors:
            print(f"  - {err}")
        sys.exit(1)

    print("All good.")


if __name__ == "__main__":
    main()
