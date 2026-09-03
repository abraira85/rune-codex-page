---
name: qa-conventions
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project. Move to production once a real coding agent has followed it correctly."
---

# QA Conventions (AGENTS.md)

An `AGENTS.md` section establishing testing expectations for any coding
agent (Codex, Copilot, etc.) working in a project — how to run tests,
what "done" means, and what not to do. Unlike the Claude subagents in
`../../claude/agents/`, this isn't a persona — it's project-wide
guidance a coding agent reads before touching anything.

## Prompt / instructions

```
## Testing

Before considering any change complete:

1. Run the project's actual test command (see below) — never assume
   passing tests, always run them.
2. If you added or changed behavior, add or update a test that would
   have caught the bug/regression you're fixing, or that exercises the
   new behavior. A change with no corresponding test change is not done.
3. If a test fails and you don't understand why, stop and investigate
   before "fixing" it by weakening the assertion or adding a skip.
   A test that's disabled to make CI green is a regression, not a fix.
4. Do not mark a task complete if tests are failing, even ones unrelated
   to your change — either fix them or explicitly flag them as
   pre-existing and out of scope, but don't silently ignore red tests.

Test command: <FILL IN — e.g. `npm test`, `pytest`, `make test`>
Coverage expectation: <FILL IN if the project enforces a minimum, e.g.
  "new code must not drop overall coverage below 80%">
Test locations: <FILL IN — e.g. `tests/`, `**/*.test.ts`, colocated
  `*_test.py` files>

## What "tested" does NOT mean here

- Reading the code and reasoning it looks correct is not testing.
- A test that always passes regardless of the implementation (e.g.
  asserting `true == true`) is not a real test — remove or fix it if
  you find one.
- Manual testing you performed but didn't automate should be described
  in the PR/commit description, not silently assumed to be repeatable.
```

## Notes

This is a template with `<FILL IN>` placeholders — it's project-agnostic
on purpose. Fill in the actual test command and coverage bar for the
project you're adding this to before relying on it; a coding agent
following a placeholder command will just fail step 1 every time.
