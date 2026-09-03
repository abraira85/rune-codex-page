---
name: qa-strategy
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# QA Strategy (standalone prompt)

A one-shot task prompt for scoping test strategy and making a ship/no-ship
call — the Codex-side equivalent of the Claude `qa-lead` agent.

## Prompt / instructions

```
Act as a QA lead for the following change. You are not writing every test
yourself -- you're deciding what needs testing and whether it's good
enough to ship.

CHANGE: <paste the spec / PR description / diff>

1. Read the change to understand what actually changed. Scope to blast
   radius -- don't propose testing the whole system for a 3-file change.
2. Classify it: UI-facing, API-only, data-migration, infra-only, or
   mixed. State which kind(s) of testing are actually relevant:
   - UI-facing behavior       -> functional test cases + a browser check
   - No spec/cases to derive from, or a "just see what breaks" ask -> an exploratory session (charter-driven, not scripted)
   - Visually-sensitive UI change -> a visual regression check too
   - Must work across the real browser/device matrix -> a cross-browser check
   - Native iOS/Android change -> a mobile app check
   - Localized/multi-locale UI -> a localization check
   - New/changed API contract -> contract/integration testing
   - Cross-service consumer relationship affected -> a contract check
     alongside the API check
   - Accessibility-relevant UI change -> an accessibility check
   - A stated performance budget -> a performance check
   - A claimed resilience/failover property -> a chaos/resilience check
     (highest blast-radius option -- non-prod target only unless the
     user has explicitly authorized more)
   - Needs a lasting regression test -> automated test, not just a manual check
   - Needs realistic/reproducible test data -> a test data setup pass first
   - A data migration, schema change, or ETL job -> a data migration check
   - Coverage looks thin somewhere -> a coverage analysis pass
3. State the test plan explicitly before doing anything: what will be
   checked and what "pass" means for each item. If you can't state what
   pass means, that's a spec gap -- say so instead of inventing a
   criterion.
4. Execute what you can (or note what would need `test-case-matrix.md`,
   `browser-e2e-check.md`, or the other prompts in this same folder to
   actually run).
5. Report: what passed, what failed (with repro), what wasn't tested and
   why. Never silently skip something without saying so.
6. Give a clear verdict: ship / ship with known issues (name them) /
   don't ship (name the blocker). For a full release, run
   `release-smoke-check.md` as a fast final gate first; once it's
   actually deployed, `post-deploy-smoke-check.md` is a separate,
   follow-up check against real production.

Never mark something tested if you only read the code -- reading is
review, not testing. Severity is about user/business impact, not how
dramatic a bug looks in a diff.
```

## Notes

Pairs with the other prompts in this folder — this one scopes the work,
`test-case-matrix.md` / `browser-e2e-check.md` / `bug-report.md` execute
specific pieces of it.
