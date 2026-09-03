---
name: coverage-analysis
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Coverage Analysis (standalone prompt)

Turns a raw coverage report into a prioritized list of specific
undertested code that actually matters — the Codex-side equivalent of
the Claude `coverage-analyst` agent. A percentage alone is not the
output.

## Prompt / instructions

```
Analyze test coverage for: <project/module/area>

1. Run the project's real coverage command -- don't estimate. If
   coverage tooling isn't set up, say so and propose the minimal one for
   the stack in use.
2. Read the actual per-file line/branch coverage output, not just the
   summary percentage.
3. Cross-reference low-coverage areas against what actually matters:
   - Recently-changed files (check git log) are higher-risk than
     untouched legacy code at the same coverage number
   - Critical-path files (auth, payments, data mutation) matter more
     than a rarely-hit admin utility regardless of raw percentage
   - An untested branch/error-path inside an otherwise "covered" file
     often matters more than a fully untested trivial file
4. For each finding, state specifically what's untested (function,
   branch/condition) and why it matters (what real scenario hits that
   path). "42% coverage in payment.ts" is not actionable on its own;
   naming the specific untested refund branch and the real flow that
   exercises it is.
5. Order by risk, not by lowest percentage first.
6. Don't recommend chasing 100% coverage for its own sake -- flag
   diminishing-return targets if you see coverage tooling being gamed
   toward a number rather than genuine testing.

Never report a coverage number without having actually run the coverage
tool in this session.
```

## Notes

Produces a prioritized worklist, not the tests themselves -- hand
findings to `write-automated-test.md` in this folder to close the gaps.
