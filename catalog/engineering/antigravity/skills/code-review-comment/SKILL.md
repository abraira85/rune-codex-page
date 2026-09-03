---
name: code-review-comment
status: experimental
context: "Ported from the Claude code-review-comment skill (../../../claude/skills/code-review-comment/SKILL.md) — not yet run against a real PR."
description: Format a single code review finding consistently -- location, what's wrong, why it matters, severity, and a concrete suggestion -- so every finding from every reviewer role reads the same way.
---

# Code Review Comment

## When to use this skill

Invoke once a finding has actually been identified (by `code-reviewer`,
`api-design-reviewer`, `dependency-reviewer`, or manual review) and needs
to be written up consistently -- either as plain text or as the body of
an inline PR comment via `vcs-review-mcp`. This skill formats a finding
someone already found; it doesn't do the finding itself.

## Prompt / instructions

```
Given a code review finding, format it as:

**[Severity] file:line** -- one-line summary of what's wrong

What's wrong: the specific problem, precise enough that the author
doesn't have to guess what you mean by re-reading the whole function.

Why it matters: the concrete failure scenario or consequence -- "this
throws a null-reference error when the optional `discount` field is
omitted, which the checkout API allows" is a reason; "this could cause
issues" is not.

Suggestion: a specific, actionable fix or direction -- not required to
be a full diff, but specific enough that the author knows what "fixed"
looks like. If you're not sure of the right fix, say what you'd
investigate rather than inventing a confident-sounding one.

Severity (pick one, don't invent a new scale):
- Blocking: real bug, security issue, or breaks something that works
  today -- must be fixed before merge
- Should-fix: a real problem but not merge-blocking
- Nit: minor/stylistic, optional

Never phrase a Nit as if it were Blocking to make it more likely to get
addressed, and never soften a real Blocking finding into a Nit to avoid
seeming harsh -- severity reflects actual impact, not how it'll land.
```

## Notes

Pairs with `code-reviewer`, `api-design-reviewer`, and
`dependency-reviewer` in `../../agents/` -- they find issues, this skill
is the consistent output format once a finding is confirmed. If
`vcs-review-mcp` (`../../mcp/`) is configured, this is also the format
for the body of an inline PR comment, not just a plain-text report.
Ported unchanged in substance from
`../../../claude/skills/code-review-comment/SKILL.md`.
