---
name: playwright-mcp
status: experimental
context: "Ported from the Claude playwright-mcp config (../../claude/mcp/playwright-mcp.md) — not yet run in a real project."
description: Wires the official Playwright MCP server into Antigravity, giving direct structured browser control instead of writing and running throwaway Playwright scripts via run_command.
---

# Playwright MCP

Gives Antigravity's agents direct, structured control of a real browser
(navigate, click, fill, screenshot, read the accessibility tree) through
the official Playwright MCP server, instead of writing and running one-off
Playwright scripts via `run_command`. Pairs directly with
`browser-automation-tester`, `visual-regression-tester`, and
`accessibility-auditor` in `../agents/` — any of them can drive the
browser through this MCP connection instead of shell-authored scripts,
once it's configured.

## Prompt / instructions

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

## Notes

- Requires Node.js available on the machine running Antigravity (the
  `npx` command fetches and runs the server on demand — no separate
  install step, but the first run downloads it).
- This config block goes in `.agents/mcp_config.json` at the workspace
  root (or `~/.gemini/config/mcp_config.json` for a server available
  globally, across projects). `scripts/install.py` intentionally does
  not write this for you (see the root README) — merge it by hand so you
  don't clobber other servers already configured there.
- To actually use it, a custom agent's frontmatter needs to list it
  under `mcpServers` (or the agent needs `call_mcp_tool` access and the
  server needs to be enabled workspace-wide) — check current Antigravity
  MCP docs for the exact scoping mechanism, since this is a newer surface
  than Claude's equivalent.
- `browser-automation-tester`, `visual-regression-tester`, and
  `accessibility-auditor` as written in this repo drive the browser via
  `run_command` + hand-written Playwright scripts, which works with zero
  extra setup. Once this MCP server is configured, the same roles can
  drive the browser through it directly instead — faster iteration, no
  throwaway script files — but that's an environment choice, not
  something baked into those agents' prompts.
- Full server docs / options: https://github.com/microsoft/playwright-mcp
- Ported from `../../claude/mcp/playwright-mcp.md` — same server, only
  the config file's location/scoping differs between Claude and
  Antigravity.
