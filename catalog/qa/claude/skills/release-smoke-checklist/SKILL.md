---
name: release-smoke-checklist
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run against a real release."
description: Build and execute a fast, time-boxed pre-release smoke suite covering critical user flows and known-fragile areas, ending in a go/no-go input.
---

# Release Smoke Checklist

## When to use this skill

Invoke right before a release, when the question is "is this safe to
ship right now," not "is this feature fully tested" (that's the deeper
work `qa-lead` scopes earlier in the cycle). A smoke suite trades
thoroughness for speed on purpose -- it's a fast confidence check, not a
regression suite.

## Prompt / instructions

```
Build and run a smoke suite for this release:

1. Identify critical paths. Use the project's own documented critical
   flows if they exist. Otherwise derive them from what would hurt most
   if broken right now (auth, checkout/payment, core create/read/update/
   delete flows, primary navigation) and mark derived ones "(inferred)."
2. Add known-fragile areas: anything with an open flaky-test ticket
   (see `flaky-test-investigator`), a bug fixed recently in this area,
   or a recent significant refactor touching it. Pull from prior
   triage/investigation history if it's available rather than
   re-deriving fragility from scratch each release.
3. For each item on the list, state exactly what "pass" means and the
   fastest reliable way to check it: an existing automated test that
   already covers it, a direct browser check, or a direct API call.
   Don't write a new elaborate check for a smoke item -- reuse what
   exists.
4. Time-box the whole thing up front (state the budget, e.g. 15
   minutes) before running anything. If the full list doesn't fit, cut
   to the highest-impact items and say explicitly what got cut and why
   -- a smoke suite that takes as long as full regression has failed its
   own purpose.
5. Execute what's executable in this session now. For anything needing
   a role not available here (e.g. a dedicated browser-automation-tester
   subagent), hand off with the exact scope rather than skipping
   silently.
6. Report as a checklist: item / method / result (pass, fail with
   repro, or not run + why) / time spent, ending with a go/no-go input.
   This is one input to the ship decision, not the final call by
   itself -- especially if anything failed.

Never expand this into a full regression pass "while you're at it" --
that defeats the point of having a separate, fast pre-release check.
```

## Notes

Meant to be invoked by `qa-lead` (or standalone) as the last gate before
shipping, not as a substitute for the test-strategy work `qa-lead` does
earlier, or for the structured matrix `test-case-writer` produces during
development.
