# claude/

Prompts, subagents, skills, MCP configs and hooks for Claude and Claude Code.

## `~ ❯ ls`

| Path | What goes here |
|---|---|
| [`agents/`](./agents) | Claude Code subagent definitions (`.claude/agents/*.md`) |
| [`skills/`](./skills) | Reusable Claude Skills |
| [`mcp/`](./mcp) | MCP server configs actually wired into a project |
| [`hooks/`](./hooks) | Claude Code hook configs (`settings.json` snippets) |

Each item follows the format in [`../TEMPLATE.md`](../TEMPLATE.md) and must pass [`../scripts/validate.py`](../scripts/validate.py).

*Empty for now — items land here once they're clean and worth showing.*
