---
name: visual-regression-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Visual Regression Check (standalone prompt)

Compares real rendered pixels against a baseline to catch layout/style
regressions functional checks miss — the Codex-side equivalent of the
Claude `visual-regression-tester` agent.

## Prompt / instructions

```
Check the following UI surface for visual regressions:

TARGET: <page, component, or flow>

1. Confirm Playwright (`@playwright/test`) is available or installable.
   If not, say so instead of describing the layout from reading CSS.
2. Neutralize non-determinism before capturing: disable animations,
   freeze/mock anything time-based (dates, relative timestamps), wait
   for fonts/images to finish loading. A diff caused by an unmocked
   timestamp is noise, not a finding.
3. Capture via `expect(page).toHaveScreenshot()` (or equivalent) at the
   viewport size(s) that matter here.
4. No existing baseline: say explicitly "no baseline existed -- this run
   created one," not "passed."
5. Diff found: read the actual diff image before concluding anything.
   Classify as likely-intentional (matches what this change was
   supposed to do) or regression (doesn't match, or hits something the
   change shouldn't have touched). Never auto-promote a diff to the new
   baseline without this classification, and don't dismiss a small diff
   just because it's small.
6. Report: which snapshots diffed, diff region/percentage, the
   classification and why. Baseline promotion is the reviewer's call
   unless told otherwise.

Baselines are only valid for the OS/browser/renderer they were captured
on -- if this project doesn't pin a consistent rendering environment for
baselines, flag that as a setup gap instead of treating the resulting
false diffs as real findings.
```

## Notes

Complements `browser-e2e-check.md` in this folder rather than replacing
it -- that one verifies behavior, this one verifies appearance.
