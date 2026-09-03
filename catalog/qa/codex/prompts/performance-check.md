---
name: performance-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Performance Check (standalone prompt)

Runs load/stress testing against a performance budget with real
measurements — the Codex-side equivalent of the Claude
`performance-tester` agent.

## Prompt / instructions

```
Performance-test the following target against a real budget:

TARGET: <endpoint, page, or operation>
BUDGET: <paste the stated budget, e.g. "p95 < 300ms at 50 rps", or state
         "none given -- derive a reasonable one and mark it inferred">

1. If no budget is given, propose one based on the nature of the
   operation (interactive API vs batch job vs page load) and label it
   "(inferred budget)" so it's never confused with a real SLA.
2. Run an actual load tool already available in this project (k6,
   autocannon, Artillery, Lighthouse for page loads, etc.) -- do not
   estimate performance from reading the code.
3. Report real measured numbers: p50/p95/p99 latency, error rate,
   throughput achieved, resource usage if observable (CPU/memory) --
   never a qualitative "seems fast" without numbers.
4. Test at a few load levels if relevant (baseline, expected peak,
   stress) rather than a single arbitrary run -- one number from one run
   is not a performance profile.
5. Compare each measured number explicitly against the budget: PASS/FAIL
   per metric.
6. If something fails, look for the likely bottleneck (slow query, N+1,
   missing index, unbounded payload) by reading the relevant code path,
   and name it as a hypothesis, not a confirmed root cause unless
   actually profiled.

Never report a budget as met without having actually run the load tool
and captured real numbers.
```

## Notes

For page-load performance specifically, Lighthouse (CLI or the
Playwright integration) is usually the right tool over a generic load
generator.
