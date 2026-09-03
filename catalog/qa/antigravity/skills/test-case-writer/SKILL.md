---
name: test-case-writer
status: experimental
context: "Ported from the Claude test-case-writer skill (../../../claude/skills/test-case-writer/SKILL.md) — not yet run against a real spec."
description: Turn a feature spec, PR description, or ticket into a structured test case matrix covering happy path, edge cases, and negative cases.
---

# Test Case Writer

## When to use this skill

Invoke when you're given a feature description, spec, or PR and need a
structured set of test cases before any testing happens — this produces
the plan, not the execution.

## Prompt / instructions

```
Given a feature description (spec text, PR diff, or ticket), produce a
test case matrix:

1. Extract explicit acceptance criteria. If the input doesn't state them,
   derive reasonable ones and mark them "(inferred)" so they're never
   confused with an actual requirement.
2. For each criterion, generate test cases across four categories:
   - Happy path: the primary intended behavior
   - Boundary/edge: empty, min, max, just-over-the-limit inputs
   - Negative: invalid input, unauthorized access, expected error states
   - State: what happens before/during/after, and on retry/reload
3. Each test case gets: ID, title (specific, states the scenario),
   preconditions, steps, expected result. No "actual result" yet -- this
   skill produces the plan, execution happens separately.
4. Flag anything untestable as written -- vague acceptance criteria,
   missing error-handling spec, undefined edge-case behavior -- as an
   open question rather than guessing and testing against your guess.
5. Order cases by risk: highest-impact happy-path and negative cases
   first, cosmetic edge cases last, so a time-constrained tester knows
   what to run first.
6. If a test-management MCP is configured (`../../mcp/test-management-mcp.md`),
   sync the matrix there: create or update each case (match on
   title/external-ID first so re-running this doesn't create
   duplicates), don't invent which project/suite/section to file into --
   ask if it isn't specified. Otherwise, output the matrix only; syncing
   is an addition, not a requirement.

Output as a markdown table: ID | Title | Preconditions | Steps | Expected.
```

## Notes

Pairs naturally with the `functional-tester` and `browser-automation-tester`
subagents in `../../agents/` — this skill produces the case list, they
execute it. Syncing (step 6) depends on `test-management-mcp` in
`../../mcp/` being configured — that file is more speculative than the
others in this folder about what's actually available; check it before
assuming a sync target exists. Ported unchanged in substance from
`../../../claude/skills/test-case-writer/SKILL.md`.
