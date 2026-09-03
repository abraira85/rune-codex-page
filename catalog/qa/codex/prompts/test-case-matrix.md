---
name: test-case-matrix
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Test Case Matrix (standalone prompt)

Generates a structured test case matrix from a spec — the Codex-side
equivalent of the Claude `test-case-writer` skill.

## Prompt / instructions

```
Given the following feature description, produce a test case matrix
before any testing happens:

FEATURE DESCRIPTION:
<paste the spec, PR description, or ticket text here>

1. Extract explicit acceptance criteria from the description above. If
   none are stated, derive reasonable ones and mark each as "(inferred)"
   so they're never confused with an actual requirement.
2. For each criterion, produce test cases across:
   - Happy path (primary intended behavior)
   - Boundary/edge (empty, min, max, just-over-the-limit input)
   - Negative (invalid input, unauthorized access, expected errors)
   - State (before/during/after the action, retry/reload behavior)
3. Each case: ID, title (states the exact scenario), preconditions,
   steps, expected result. Do not fill in "actual result" — this
   produces the plan, not the execution.
4. Call out anything untestable as written (vague criteria, undefined
   error behavior) as an open question rather than guessing.
5. Order by risk — highest-impact happy-path and negative cases first.
6. If asked to sync this into a test-management platform (TestRail,
   Xray, Zephyr, Qase, or similar): check for an MCP tool for it first
   and prefer that; otherwise look for an API token/env var and call
   the platform's REST API directly. Match on title/external-ID before
   creating a case so re-runs don't produce duplicates. Never guess
   which project/suite/section to file into -- ask if it isn't
   specified. If no credentials or MCP tool are available, say so and
   hand back the matrix instead of pretending it was synced.

Output as a markdown table: ID | Title | Preconditions | Steps | Expected.
```

## Notes

Produces the plan only. To execute it against a real browser, follow up
with `browser-e2e-check.md` in this same folder for the UI-facing cases.
Step 6 mirrors `bug-report.md`'s issue-tracker fallback, aimed at test-
management platforms instead of bug trackers.
