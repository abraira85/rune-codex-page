---
name: bug-report
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Bug Report (standalone prompt)

Reproduces a raw bug report and writes it up consistently — the
Codex-side equivalent of the Claude `bug-triage-analyst` agent /
`bug-report-template` skill.

## Prompt / instructions

```
Given this raw bug report, reproduce it and write it up properly:

RAW REPORT:
<paste the user complaint, failing test output, or stack trace here>

1. Try to actually reproduce it by running the relevant code/command —
   don't write up a report for something you only read about. If you
   can't reproduce it, state exactly what you tried and say "could not
   reproduce" rather than guessing at a repro that sounds plausible.
2. Once reproduced, minimize it to the smallest steps that still trigger
   the issue.
3. Rate severity by actual impact:
   - Blocker: breaks a core flow for most/all users, no workaround
   - Major: breaks a real flow for some users, or has an ugly workaround
   - Minor: cosmetic/edge-case, easy workaround
   - Trivial: no functional impact
4. Identify the likely responsible file/module by reading the relevant
   code — enough to point a fixer in the right direction.
5. Write up as: Title (specific) / Environment / Steps to reproduce
   (numbered, minimal) / Expected result / Actual result (exact error
   text if any) / Severity (with one-line justification) / Suspected
   area.
6. If asked to file this in Jira, Trello, Notion, Linear, or a similar
   tracker: first check whether an MCP tool for it is already available
   in this session and prefer that. Otherwise, look for an API
   token/env var for that platform (e.g. JIRA_API_TOKEN, TRELLO_KEY +
   TRELLO_TOKEN, NOTION_API_KEY) and call the platform's REST API
   directly (curl or the project's existing scripts) -- don't invent
   a client library that isn't already in the project. Map severity to
   whatever priority scale the target project/board/database actually
   uses (check its existing values, don't assume a 1:1 match), and put
   the repro/expected/actual into the ticket's description field.
   Never guess which project, board, or database to file into -- if
   it isn't specified, ask. If no credentials or MCP tool are
   available, say so plainly and hand back the written report instead
   of pretending it was filed.

Never present a guess as a confirmed fact. "Environment: not specified
in the original report" is a valid, honest field value.
```

## Notes

For a project that's adopted `qa-conventions.md` (`../agents-md/`), this
report should reference whether a regression test was added for the bug
once it's fixed — that's a testing-convention concern, not part of triage
itself, so it's not baked into this prompt.

Step 6 mirrors what `issue-tracker-mcp.md` (Claude side, `../../claude/mcp/`)
sets up as a persistent MCP connection — Codex doesn't have that same
mcp/ catalog type, so the same capability is expressed as a per-task
fallback (MCP-if-available, REST API otherwise) instead of a standing
config.
