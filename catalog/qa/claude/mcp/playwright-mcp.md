---
name: playwright-mcp
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project. Move to production once a real session has used it to drive a browser."
description: Wires the official Playwright MCP server into Claude, giving direct structured browser control instead of Claude writing and running throwaway Playwright scripts via Bash.
---

# Playwright MCP

Gives Claude direct, structured control of a real browser (navigate,
click, fill, screenshot, read the accessibility tree) through the
official Playwright MCP server, instead of writing and running one-off
Playwright scripts via Bash. Pairs directly with
`browser-automation-tester` and `accessibility-auditor` in this same
folder — either can drive the browser through this MCP connection
instead of Bash-authored scripts, once it's configured.

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

- Requires Node.js available on the machine running Claude (the `npx`
  command fetches and runs the server on demand — no separate install
  step, but the first run downloads it).
- This config block goes in your MCP client's config file — for Claude
  Code that's typically `.mcp.json` at the project root; for the Claude
  desktop app it's `claude_desktop_config.json`. `scripts/install.py`
  intentionally does not write this for you (see the root README) —
  merge it by hand so you don't clobber other servers already configured
  there.
- `browser-automation-tester` and `accessibility-auditor` as written in
  this repo drive the browser via Bash + hand-written Playwright scripts,
  which works with zero extra setup. Once this MCP server is configured,
  the same roles can drive the browser through it directly instead —
  faster iteration, no throwaway script files — but that's an
  environment choice, not something baked into those agents' prompts.
- Full server docs / options: https://github.com/microsoft/playwright-mcp
