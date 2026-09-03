---
name: release-smoke-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Release Smoke Check (standalone prompt)

Builds and runs a fast, time-boxed pre-release smoke suite over critical
flows — the Codex-side equivalent of the Claude `release-smoke-checklist`
skill.

## Prompt / instructions

```
Build and run a smoke suite for this release:

1. Identify critical paths: use the project's documented critical flows
   if they exist, otherwise derive them from what would hurt most if
   broken right now (auth, checkout/payment, core CRUD, primary nav) and
   mark derived ones "(inferred)."
2. Add known-fragile areas: anything with an open flaky-test ticket, a
   recently-fixed bug in that area, or a recent significant refactor
   touching it.
3. For each item, state exactly what "pass" means and the fastest
   reliable way to check it -- reuse an existing automated test, a
   direct browser check, or a direct API call. Don't write an elaborate
   new check for a smoke item.
4. State a time budget up front (e.g. 15 minutes) before running
   anything. If the full list doesn't fit, cut to the highest-impact
   items and say explicitly what got cut and why.
5. Execute what's executable now; for anything out of reach in this
   session, hand off with the exact scope instead of skipping silently.
6. Report as a checklist: item / method / result (pass, fail with
   repro, or not run + why) / time spent, ending with a go/no-go input
   -- this feeds the ship decision, it isn't the final call by itself.

Never expand this into a full regression pass "while you're at it" --
that defeats the purpose of a separate, fast pre-release check.
```

## Notes

Meant as the last gate before shipping, not a substitute for
`qa-strategy.md`'s earlier scoping or `test-case-matrix.md`'s deeper
coverage during development.
