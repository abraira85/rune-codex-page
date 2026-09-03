---
name: cross-browser-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Cross-Browser Check (standalone prompt)

Runs an already-verified scenario across the project's real
browser/device support matrix — the Codex-side equivalent of the Claude
`cross-browser-tester` agent.

## Prompt / instructions

```
Cross-browser-check the following already-verified scenario:

SCENARIO: <feature/flow already confirmed working in one browser>

1. Determine the real support matrix from the project's own stated
   policy (browserslist, a documented support table, analytics) -- don't
   invent "test everything."
2. Use Playwright's built-in multi-engine support (Chromium, Firefox,
   WebKit) first. For matrix entries Playwright can't reach, use a
   configured device farm if one exists; otherwise say explicitly which
   entries couldn't be covered.
3. Run the same scenario per engine/device. For failures, read the
   actual error/rendering difference -- don't guess "probably CSS."
4. Distinguish a genuine cross-browser bug from a known-acceptable
   platform difference (e.g. native date-picker UI), but state the
   distinction explicitly rather than silently excluding either.
5. Prioritize by real usage if browser-share data exists; if not, don't
   invent a weighting -- report by how broken the flow is and note that
   usage-based prioritization wasn't available.
6. Report matrix coverage actually achieved (not the full claimed
   matrix), per-environment pass/fail, and a root-cause hypothesis where
   identifiable.

Never report "cross-browser tested" without naming the exact
browsers/devices actually run.
```

## Notes

Assumes the scenario already has a known-correct baseline (typically
from `browser-e2e-check.md`) -- this checks breadth, not first-time
correctness.
