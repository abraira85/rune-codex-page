---
name: write-automated-test
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Write Automated Test (standalone prompt)

Writes a lasting automated test into the project's real suite — the
Codex-side equivalent of the Claude `test-automation-engineer` agent.

## Prompt / instructions

```
Write an automated regression test for the following behavior:

BEHAVIOR: <describe the feature/bugfix/case that needs a lasting test>

1. First inspect the project's existing test suite: framework, file
   naming convention, how fixtures/mocks/setup are typically done. Match
   the existing style -- do not introduce a second testing pattern or
   library into a project that already has one.
2. Decide the right layer for this test:
   - Unit: pure logic, no I/O
   - Integration: touches a real DB/service boundary within the process
   - E2E: exercises the system the way a user/client actually would
   Prefer the lowest layer that would still catch the regression --
   don't reach for E2E when a unit test proves the same thing faster.
3. Write the test to fail first against the pre-fix code if this is a
   bugfix (or write it against the current behavior and confirm it
   fails for the right reason), then confirm it passes against the
   correct/fixed behavior. State both results.
4. Assert on real, meaningful outcomes -- not on implementation details
   that would break on a harmless refactor (e.g. assert on returned
   data/visible state, not on internal call counts unless that's the
   actual thing under test).
5. Run the full affected test file (not just the new test) to confirm no
   regressions were introduced, and report the run output.
6. Name the test so its title alone states the scenario and expected
   outcome.

Never report a test as passing without having actually executed the test
runner and seen the result.
```

## Notes

Pairs with `test-case-matrix.md` in this folder: that prompt produces the
scenarios worth covering, this one turns the highest-value ones into
code that stays in the suite.
