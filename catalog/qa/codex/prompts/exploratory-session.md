---
name: exploratory-session
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Exploratory Session (standalone prompt)

Runs a time-boxed, charter-driven, free-form investigation session
(SBTM) — the Codex-side equivalent of the Claude `exploratory-tester`
agent. No pre-written test cases; this is where unknown-unknowns get
caught.

## Prompt / instructions

```
Run a session-based exploratory testing session:

CHARTER: <mission/area/risk to explore -- if only a vague topic was
          given, turn it into a real charter yourself and say so>

1. State the charter explicitly before starting: mission, scope
   (in/out), and a time box (45-90 minutes is typical; state whatever
   you're actually using).
2. Use the feature/area like an investigator, not a script: try the
   obvious path, then deliberately deviate -- unexpected input order,
   back button, double-submission, interrupting a flow partway,
   combining features in ways the spec doesn't address.
3. Log as you go: what you tried, what you noticed -- bugs, but also
   things that seem risky or worth a follow-up charter even if not a
   clear bug.
4. If you go on a productive tangent outside the charter, that's fine --
   note it as "opportunistic" separately from on-charter coverage.
5. Reproduce a suspected bug once more before logging it as confirmed,
   then hand it to `bug-report.md` in this folder for the full write-up
   rather than doing that inline.

Session report: charter, time spent (on-charter vs opportunistic), areas
actually covered (specific enough to show what wasn't explored), bugs
found (reference their write-up), open questions/risks worth a follow-up
charter, and your honest confidence level (thorough / partial / barely
scratched it).

Never report "explored X" without the specific paths/actions taken.
```

## Notes

Complements `test-case-matrix.md` rather than overlapping it: that
produces cases from a spec and checks conformance; this has no spec to
check against and is explicitly hunting for what nobody specified.
