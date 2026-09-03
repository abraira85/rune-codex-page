---
name: chaos-resilience-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project. Higher blast-radius than the other prompts in this folder by design -- scope carefully."
---

# Chaos & Resilience Check (standalone prompt)

Injects a real fault into a real running system and observes actual
behavior — the Codex-side equivalent of the Claude
`chaos-resilience-tester` agent. The highest blast-radius prompt in this
folder; treat safety scoping as part of the task.

## Prompt / instructions

```
Test resilience to the following fault:

RESILIENCE CLAIM: <e.g. "checkout tolerates the payment provider being slow">
TARGET ENVIRONMENT: <must be explicitly non-production unless the user
                      has explicitly authorized a production run for this
                      specific task>

Hard safety rules, before anything else:
- Never target production without explicit, informed confirmation for
  this specific run. Default to staging/non-critical.
- State the blast radius (what could break, for whom) and the exact
  rollback/abort plan before injecting anything.
- Inject one fault at a time -- stacking faults makes causality
  unreadable.
- If you can't safely construct or remove a fault in this environment,
  say so and don't attempt a version you can't cleanly undo.

1. State the expected behavior precisely before injecting anything
   (retry N times, fail over, degrade to cache, surface a specific
   error). If this isn't specified anywhere, that's a spec gap -- flag
   it instead of inventing the expected behavior.
2. Use existing chaos tooling if the project has it (Toxiproxy, Chaos
   Mesh, Gremlin, a custom harness). Otherwise, minimal manual fault
   injection is acceptable for a narrowly-scoped, confirmed-safe target
   (`tc netem` for latency, a firewall rule to drop traffic, killing a
   specific non-critical process).
3. Inject the fault against the scoped target. Observe and record actual
   behavior: did it match expected, how long did recovery take once the
   fault was removed, what did dependents actually experience during the
   fault window.
4. Remove the fault and verify actual recovery -- don't assume it.
5. Report: fault injected, expected vs actual, recovery time, any
   cascading impact. Divergence from expected behavior is a resilience
   bug -- hand off to `bug-report.md` in this folder.

Never claim resilience to a failure mode you didn't actually inject and
observe in this session.
```

## Notes

When in doubt about whether a target is safe to run against, don't --
ask first rather than proceeding on an assumption.
