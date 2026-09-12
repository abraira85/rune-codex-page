#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def create_agent(area, name, context, description, prompt, notes):
    platforms = [
        ("antigravity", "agents", "inherit", "[view_file, grep_search, list_dir, run_command]"),
        ("claude", "agents", "sonnet", "[view_file, grep_search, list_dir, run_command]"),
        ("codex", "prompts", None, None)
    ]

    for platform, type_dir, model, tools in platforms:
        dest_dir = ROOT / "catalog" / area / platform / type_dir
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_dir / f"{name}.md"

        content = []
        if platform != "codex":
            content.append("---")
            content.append(f"name: {name}")
            content.append("status: experimental")
            content.append(f'context: "{context}"')
            content.append(f"description: {description}")
            if tools:
                content.append(f"tools: {tools}")
            if model:
                content.append(f"model: {model}")
            content.append("---\n")
            content.append(f"# {name.replace('-', ' ').title()}\n")
            content.append(f"{description}\n")
            content.append("## Prompt / instructions\n")
            content.append("```")
            content.append(prompt)
            content.append("```\n")
            content.append("## Notes\n")
            content.append(f"{notes}\n")
        else:
            # Codex format (AGENTS.md uses a different format, but codex/prompts/ is simpler)
            content.append("---")
            content.append(f"name: {name}")
            content.append("status: experimental")
            content.append(f'context: "{context}"')
            content.append("---\n")
            content.append(f"# {name.replace('-', ' ').title()}\n")
            content.append(f"{description}\n")
            content.append("## Prompt / instructions\n")
            content.append("```")
            content.append(prompt)
            content.append("```\n")
            content.append("## Notes\n")
            content.append(f"{notes}\n")

        dest_file.write_text("\n".join(content), encoding="utf-8")
        print(f"Created {dest_file.relative_to(ROOT)}")

if __name__ == "__main__":
    area = "engineering"
    name = "debugging-specialist"
    context = "Initial experimental version. Complement to code-reviewer."
    description = "Use when you have a bug or failure and need to find the actual code-level root cause, not just reproduce it."
    prompt = """You are a senior debugging specialist. Your job is to take a reported bug, error trace, or failure description and find the actual root cause in the codebase.

1. Do not guess. Use grep_search, view_file, and list_dir to trace the execution path.
2. If given a stack trace, start at the exact file and line number mentioned.
3. If given a functional bug, identify the entry point (e.g. API endpoint, UI event handler) and trace the logic downwards.
4. Look for common root causes: null references, race conditions, type mismatches, swallowed errors, logic errors.
5. Once you find the root cause, explain *why* it happens, not just *where* it is.
6. Provide a concrete fix or recommendation for the `code-reviewer` or developer to implement. Do not modify the code yourself unless explicitly asked."""
    notes = "Works alongside `qa/bug-triage-analyst`. The QA role finds and reports the bug; this role digs into the code to find the root cause."

    create_agent(area, name, context, description, prompt, notes)
