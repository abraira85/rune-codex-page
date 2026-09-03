---
name: issue-tracker-mcp
status: experimental
context: "Ported from the Claude issue-tracker-mcp config (../../claude/mcp/issue-tracker-mcp.md) — not yet used against a real Jira/Trello/Notion workspace."
description: Wires an issue-tracker MCP server (Jira/Confluence, Notion, Trello, or similar) into Antigravity so bug-triage-analyst and flaky-test-investigator can file the ticket directly instead of only producing a markdown write-up.
---

# Issue Tracker MCP

Gives Antigravity's agents direct, structured access to an issue tracker
(create a ticket/card/page, set fields, attach a label) through an MCP
server, instead of a human copy-pasting the markdown report from
`bug-triage-analyst` into Jira/Trello/Notion by hand. Pairs directly with
`bug-triage-analyst`, `flaky-test-investigator`, and the
`bug-report-template` skill in `../agents/` / `../skills/` — once
configured, the last step of triage becomes "file it" instead of "hand
this to someone who will file it."

## Prompt / instructions

Jira & Confluence — Atlassian's official remote MCP server (OAuth,
hosted, no local install):

```json
{
  "mcpServers": {
    "atlassian": {
      "url": "https://mcp.atlassian.com/v1/sse"
    }
  }
}
```

Notion — official MCP server (remote, or run locally with an internal
integration token):

```json
{
  "mcpServers": {
    "notion": {
      "url": "https://mcp.notion.com/mcp"
    }
  }
}
```

Trello — no official MCP server as of this writing; several
community-maintained ones exist on npm. Verify the package is still
maintained and read its source before trusting it with write access to
a real board:

```json
{
  "mcpServers": {
    "trello": {
      "command": "npx",
      "args": ["-y", "<community-trello-mcp-package>"],
      "env": {
        "TRELLO_API_KEY": "<key>",
        "TRELLO_TOKEN": "<token>"
      }
    }
  }
}
```

Same pattern for Linear, Asana, GitHub Issues, or anything similar:
check the vendor's docs for an official server first, fall back to a
vetted community one, and add it as another entry under `mcpServers`.

## Notes

- Exact server URLs, package names, and auth flows change — this file
  captures the shape as of when it was written, not a guarantee. Check
  the vendor's current MCP docs before wiring this into a real project.
- This config block goes in `.agents/mcp_config.json` (workspace) or
  `~/.gemini/config/mcp_config.json` (global). `scripts/install.py`
  intentionally does not write this for you — merge it by hand, same as
  `playwright-mcp` in this folder.
- Field mapping when `bug-triage-analyst` or `flaky-test-investigator`
  files a ticket through this: severity maps to the tracker's priority
  field (check the target project's actual priority values, don't
  assume a 1:1 match), the write-up's title/repro/expected/actual
  become the ticket description, and "suspected area" becomes a
  label/component if the project has one.
- If no issue-tracker MCP is configured, both agents still produce the
  same markdown report as before — filing a ticket is an additional
  step this enables, not a replacement for the write-up.
- Never invent a project, board, or space to file into. If the target
  destination isn't specified, ask or use whatever the user already
  pointed at — don't guess and create the ticket somewhere
  plausible-sounding.
- Ported from `../../claude/mcp/issue-tracker-mcp.md` — same servers,
  only the config file's location/scoping differs between Claude and
  Antigravity.
