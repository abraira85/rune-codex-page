---
name: flaky-test-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Flaky Test Check (standalone prompt)

Determines whether an intermittently-failing test is genuinely flaky or
a real bug, then fixes, quarantines, or escalates it properly — the
Codex-side equivalent of the Claude `flaky-test-investigator` agent.

## Prompt / instructions

```
Investigate the following intermittently-failing test:

TEST: <name/path> -- <how it was reported flaky, e.g. "failed 2/10 CI runs">

1. Rerun it in isolation N times (10 is a reasonable default), then
   rerun it as part of its full file/suite -- suite-only failures point
   at shared state or ordering, not the test itself. A single run
   proves nothing.
2. Check the usual root causes by reading the test and the code it
   exercises: fixed `sleep()` instead of a real wait condition, missing
   `await`, shared mutable fixtures/state between tests, order
   dependence, unmocked clock/random/network.
3. Classify from what the reruns actually showed:
   - Fails reliably, same way every time -> not a flake, a real bug --
     hand off to `bug-report.md` in this folder instead of quarantining.
   - Intermittent with an identifiable, small, safe fix -> fix it and
     rerun N more times to confirm the failure rate hits zero.
   - Intermittent with no identifiable cause after real investigation ->
     quarantine.
4. Quarantine means: skip with a comment linking a tracking ticket and
   an owner, plus what this investigation found -- never a bare skip and
   never deleting/commenting out the test. File the tracking ticket the
   same way `bug-report.md` does (MCP if available, otherwise the
   platform's REST API) -- don't invent a destination if none was given.
5. Report: test name, failure rate observed (isolated vs in-suite), what
   was checked, root cause if found, and the decision with reasoning.

Never raise a retry count or add a flaky-annotation as a fix without
having actually investigated -- that hides the same signal that deleting
the test would.
```

## Notes

Pairs with `bug-report.md` (real bugs found during investigation) and
mirrors its issue-tracker fallback for filing a quarantine ticket.
