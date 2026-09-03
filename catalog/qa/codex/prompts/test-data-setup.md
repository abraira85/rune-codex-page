---
name: test-data-setup
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Test Data Setup (standalone prompt)

Generates realistic, reproducible test data, or safely anonymizes real
data moving into a test environment — the Codex-side equivalent of the
Claude `test-data-engineer` agent.

## Prompt / instructions

```
Set up test data for the following need:

NEED: <what needs data -- a test suite, a demo environment, a
       prod-to-staging data refresh, etc.>

1. Find the project's existing fixture/factory/seed pattern and match
   it -- don't introduce a second data-generation approach. If none
   exists, propose the smallest reasonable one for the stack in use.
2. Generate data that actually exercises the relevant validation/logic
   -- realistic-shaped values and real boundary cases, not uniform
   placeholder strings that would pass regardless of whether validation
   is wired up.
3. Seed randomness so output is deterministic across runs, unless the
   task is specifically about randomness/fuzzing -- non-deterministic
   test data creates flaky-looking failures that waste debugging time.
4. If sourcing from a real environment: identify every PII/sensitive
   field first and mask or synthesize-replace it *before* the data
   leaves the production boundary. Never copy real PII into a non-prod
   environment "temporarily" and mask it after. If you can't verify
   masking actually happened, say so and stop.
5. Make cleanup deterministic -- a teardown step or a known test-data
   marker/prefix, so generated data doesn't silently accumulate.
6. Document what the dataset actually contains (shape, volume, edge
   cases represented) so whoever consumes it isn't guessing.

Never present synthetic data as representative of real production
volume/shape unless you've actually checked that against something real.
```

## Notes

Feeds `test-case-matrix.md`, `browser-e2e-check.md`, `api-contract-check.md`,
and `performance-check.md` in this folder -- they consume the data this
prompt produces or makes safe. The anonymization step is a hard
requirement, not optional.
