#!/usr/bin/env python3
"""Lint prompt and configuration quality across the entire catalog.

Evaluates:
- Front-matter extraction & markdown structure
- Minimum content length (no stubs or empty prompts)
- Absence of unfinished placeholder markers (TODO, FIXME, YOUR_PROMPT_HERE)
- Valid JSON inside MCP configurations
- Actionability & clarity in agent prompts and skills

Usage:
    python3 scripts/lint_prompts.py
    python3 scripts/lint_prompts.py --strict
    python3 scripts/lint_prompts.py catalog/sales/claude/agents/sales-engineer.md
"""
import argparse
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
SKIP_FILES = {"README.md", ".gitkeep"}
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
FENCED_BLOCK_RE = re.compile(r"^[ \t]*```(?:\w+)?\n(.*?)\n[ \t]*```", re.DOTALL | re.MULTILINE)

FORBIDDEN_PROMPT_PLACEHOLDERS = [
    r"\bTODO\b",
    r"\bFIXME\b",
    r"YOUR_PROMPT_HERE",
    r"\[insert\b",
    r"<insert\b",
    r"\[replace with\b",
]

ACTION_VERB_RE = re.compile(
    r"\b(analyze|review|create|generate|identify|ensure|verify|evaluate|design|draft|"
    r"audit|facilitate|inspect|monitor|build|check|translate|calculate|suggest|answer|"
    r"troubleshoot|prioritize|produce|document|test|run|deploy|investigate|parse)\b",
    re.IGNORECASE
)


class LintResult:
    def __init__(self, file_path):
        self.file_path = file_path
        self.errors = []
        self.warnings = []

    def error(self, msg):
        self.errors.append(msg)

    def warning(self, msg):
        self.warnings.append(msg)

    @property
    def passed(self):
        return len(self.errors) == 0


def lint_item(path: Path) -> LintResult:
    res = LintResult(path)
    text = path.read_text(encoding="utf-8")

    # 1. Front-matter structure
    m = FRONTMATTER_RE.match(text)
    if not m:
        res.error("File does not start with valid '---' front-matter block.")
        return res

    fm_raw, body = m.group(1), m.group(2).strip()

    try:
        fm = yaml.safe_load(fm_raw)
        if not isinstance(fm, dict):
            res.error("Front-matter does not parse as a dictionary.")
            return res
    except yaml.YAMLError as exc:
        res.error(f"Invalid YAML in front-matter: {exc}")
        return res

    # 2. Check title
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    h1_lines = [l for l in lines if l.startswith("# ")]
    if not h1_lines:
        res.error("Missing top-level H1 header ('# Title').")

    # 3. Payload inspection
    is_mcp = "mcp" in path.parts
    is_skill = "skills" in path.parts
    is_agent_or_prompt = "agents" in path.parts or "prompts" in path.parts

    if is_mcp:
        # Check MCP configuration JSON
        m_code = FENCED_BLOCK_RE.search(body)
        if not m_code:
            res.error("MCP file missing configuration code block (```json ... ```).")
        else:
            code_str = m_code.group(1).strip()
            try:
                parsed = json.loads(code_str)
                if "mcpServers" not in parsed:
                    res.warning("MCP configuration does not include top-level 'mcpServers' key.")
            except json.JSONDecodeError as err:
                res.error(f"Malformed JSON in MCP configuration: {err}")

    elif is_skill:
        # Skill templates should have meaningful instructions / checklists
        word_count = len(body.split())
        if word_count < 15:
            res.error(f"Skill instructions too short ({word_count} words; minimum 15 required).")

        for pattern in FORBIDDEN_PROMPT_PLACEHOLDERS:
            if re.search(pattern, body, re.IGNORECASE):
                res.error(f"Unfinished placeholder detected matching: {pattern}")

    elif is_agent_or_prompt:
        # Find ## Prompt / instructions
        if "## Prompt / instructions" not in body:
            res.error("Missing '## Prompt / instructions' heading in agent/prompt.")
            return res

        # Extract prompt text
        prompt_section = body.split("## Prompt / instructions", 1)[1]
        m_code = FENCED_BLOCK_RE.search(prompt_section)
        prompt_text = m_code.group(1).strip() if m_code else prompt_section.strip()

        word_count = len(prompt_text.split())
        if word_count < 12:
            res.error(f"Prompt content is too short ({word_count} words; minimum 12 required).")

        # Check for placeholder markers
        for pattern in FORBIDDEN_PROMPT_PLACEHOLDERS:
            if re.search(pattern, prompt_text, re.IGNORECASE):
                res.error(f"Unfinished placeholder detected matching: {pattern}")

        # Check for directive actionability
        has_numbered_steps = bool(re.search(r"^\s*\d+\.\s+", prompt_text, re.MULTILINE))
        has_bullet_steps = bool(re.search(r"^\s*[-*]\s+", prompt_text, re.MULTILINE))
        has_action_verbs = bool(ACTION_VERB_RE.search(prompt_text))

        if not (has_numbered_steps or has_bullet_steps or has_action_verbs):
            res.warning("Prompt lacks structured instructions (no steps, bullets, or clear action verbs).")

    return res


def main():
    parser = argparse.ArgumentParser(description="Lint prompt quality across the catalog.")
    parser.add_argument("target", nargs="?", help="Specific file or directory to lint (defaults to catalog/)")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors.")
    args = parser.parse_args()

    target_path = Path(args.target) if args.target else CATALOG
    if target_path.is_file():
        files = [target_path]
    elif target_path.is_dir():
        files = sorted([
            f for f in target_path.rglob("*.md")
            if f.name not in SKIP_FILES
        ])
    else:
        sys.exit(f"Target not found: {target_path}")

    total = len(files)
    passed = 0
    failed = 0
    warnings_count = 0

    print(f"Linting {total} catalog item(s)...")

    for f in files:
        res = lint_item(f)
        if args.strict and res.warnings:
            res.errors.extend(res.warnings)

        if not res.passed:
            failed += 1
            rel_path = f.relative_to(ROOT) if f.is_relative_to(ROOT) else f
            print(f"\n[FAIL] {rel_path}:")
            for err in res.errors:
                print(f"  - ERROR: {err}")
            for w in res.warnings:
                print(f"  - WARNING: {w}")
        else:
            passed += 1
            if res.warnings:
                warnings_count += len(res.warnings)
                rel_path = f.relative_to(ROOT) if f.is_relative_to(ROOT) else f
                print(f"\n[WARN] {rel_path}:")
                for w in res.warnings:
                    print(f"  - WARNING: {w}")

    print("\n" + "=" * 50)
    print(f"Summary: {passed}/{total} passed. {failed} failed. {warnings_count} warning(s).")

    if failed > 0:
        sys.exit(1)
    else:
        print("All prompts and configurations passed quality linting!")
        sys.exit(0)


if __name__ == "__main__":
    main()
