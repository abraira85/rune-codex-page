---
name: bug-report-template
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run against a real bug backlog."
description: Format a reproduced bug into a consistent, actionable report — title, repro, severity, suspected area.
---

# Bug Report Template

## When to use this skill

Invoke after a bug has actually been reproduced (by you or another QA
role) and needs to be written up consistently for engineering to act on.
This skill formats a *confirmed* bug — it doesn't investigate or
reproduce one itself.

## Prompt / instructions

```
Given a reproduced bug (repro steps, observed behavior, expected
behavior), format it as:

## Title
Specific and scenario-based. "Checkout fails when cart has 0 items" not
"Checkout is broken."

## Environment
Where this was observed: browser/OS, app version/commit, environment
(local/staging/prod). Omit fields you don't actually know rather than
guessing.

## Steps to reproduce
Numbered, minimal (remove any step that isn't necessary to trigger it),
starting from a known state.

## Expected result
What should happen, per spec or reasonable user expectation.

## Actual result
What actually happens. Include exact error text/status codes if any --
paraphrasing an error message loses debugging signal.

## Severity
- Blocker: breaks a core flow for most/all users, no workaround
- Major: breaks a real flow for some users, or has an ugly workaround
- Minor: cosmetic or edge-case, easy workaround exists
- Trivial: no functional impact

State the one-line reason for the severity chosen -- don't just label it.

## Suspected area
File/module/service most likely responsible, if identifiable from the
repro -- not a full root-cause analysis, just a pointer.

Never fill in a section with a guess presented as fact. "Environment:
unknown, not captured in the original report" is a valid, honest entry.
```

## Notes

Pairs with the `bug-triage-analyst` agent in `../../agents/` — that agent
does the reproduction and severity judgment; this skill is the consistent
output format once that judgment is made.
