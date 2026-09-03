#!/usr/bin/env python3
"""Install one catalog item into a target project.

    python3 scripts/install.py catalog/qa/claude/agents/qa-lead.md
    python3 scripts/install.py catalog/qa/claude/agents/qa-lead.md --target ../my-project
    python3 scripts/install.py catalog/qa/claude/skills/test-case-writer/SKILL.md

This does NOT just copy the file. Items in this repo carry catalog-only
metadata (status, context, a "## Notes" section) that isn't part of what
Claude/Codex actually reads. This script extracts the real payload --
front-matter fields a tool understands (name, description, tools, model)
plus the fenced block under "## Prompt / instructions" -- and writes (or
prints) it in the shape the target tool expects.

Placement rules, by source path:
  .../claude/agents/<slug>.md        -> <target>/.claude/agents/<slug>.md
  .../claude/skills/<slug>/SKILL.md  -> <target>/.claude/skills/<slug>/SKILL.md
  .../claude/mcp/<slug>.md           -> printed only (JSON configs need a
                                         human to merge them, never auto-written)
  .../claude/hooks/<slug>.md         -> printed only (same reasoning)
  .../codex/agents-md/<slug>.md      -> <target>/AGENTS.md (refuses to
                                         overwrite an existing one without --force)
  .../codex/prompts/<slug>.md        -> printed only (no fixed destination --
                                         it goes wherever your agent's custom
                                         instructions config lives)
"""
import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: pip install -r scripts/requirements.txt")

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
PROMPT_BLOCK_RE = re.compile(
    r"## Prompt / instructions\s*\n```[a-zA-Z]*\n(.*?)\n```", re.DOTALL
)
CLAUDE_FIELDS = ("name", "description", "tools", "model")


def parse_item(path: Path):
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        sys.exit(f"{path}: missing front-matter, can't install")
    data = yaml.safe_load(m.group(1)) or {}

    body_m = PROMPT_BLOCK_RE.search(m.group(2))
    if not body_m:
        sys.exit(f"{path}: couldn't find a '## Prompt / instructions' code block")
    prompt = body_m.group(1).strip() + "\n"
    return data, prompt


def claude_frontmatter(data: dict) -> str:
    lines = ["---"]
    for key in CLAUDE_FIELDS:
        if key in data and data[key] not in (None, [], ""):
            value = data[key]
            if isinstance(value, list):
                value = ", ".join(value)
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def write_file(dest: Path, content: str, force: bool):
    if dest.exists() and not force:
        sys.exit(f"{dest} already exists -- pass --force to overwrite, "
                  f"or merge by hand.")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")
    print(f"Installed -> {dest}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("item", help="Path to the catalog item, e.g. "
                                  "catalog/qa/claude/agents/qa-lead.md")
    ap.add_argument("--target", default=".", help="Target project root (default: cwd)")
    ap.add_argument("--force", action="store_true", help="Overwrite an existing destination file")
    args = ap.parse_args()

    src = Path(args.item).resolve()
    target = Path(args.target).resolve()
    if not src.is_file():
        sys.exit(f"Not a file: {src}")

    parts = src.parts
    if "claude" not in parts and "codex" not in parts:
        sys.exit(f"{src}: doesn't look like a catalog item (no claude/ or codex/ in path)")

    data, prompt = parse_item(src)

    if "claude" in parts:
        tool_idx = parts.index("claude")
        item_type = parts[tool_idx + 1]  # agents | skills | mcp | hooks

        if item_type == "agents":
            dest = target / ".claude" / "agents" / f"{src.stem}.md"
            write_file(dest, claude_frontmatter(data) + prompt, args.force)

        elif item_type == "skills":
            slug = parts[tool_idx + 2]  # .../skills/<slug>/SKILL.md
            dest = target / ".claude" / "skills" / slug / "SKILL.md"
            write_file(dest, claude_frontmatter(data) + prompt, args.force)

        elif item_type in ("mcp", "hooks"):
            label = "MCP server config" if item_type == "mcp" else "hook config"
            print(f"# {label} -- not auto-installed (needs merging into JSON by hand)\n")
            print(prompt)
            if item_type == "mcp":
                print("# Merge the relevant block into your MCP client config "
                      "(.mcp.json, claude_desktop_config.json, etc.)")
            else:
                print("# Merge the relevant block into .claude/settings.json's "
                      "\"hooks\" section.")

        else:
            sys.exit(f"Unknown claude/ item type: {item_type}")

    else:  # codex
        tool_idx = parts.index("codex")
        item_type = parts[tool_idx + 1]  # agents-md | prompts

        if item_type == "agents-md":
            dest = target / "AGENTS.md"
            write_file(dest, prompt, args.force)

        elif item_type == "prompts":
            print("# Codex prompt -- no fixed destination file, paste this into "
                  "your agent's custom-instruction config:\n")
            print(prompt)

        else:
            sys.exit(f"Unknown codex/ item type: {item_type}")


if __name__ == "__main__":
    main()
