---
name: data-migration-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Data Migration Check (standalone prompt)

Verifies a data migration or ETL job for real data integrity — the
Codex-side equivalent of the Claude `data-migration-tester` agent. "The
script didn't error" is not evidence of correctness here.

## Prompt / instructions

```
Verify data integrity for the following migration/ETL job:

JOB: <what's migrating, source -> destination>

Setup: needs read access to both source and destination. Never run
against production data without explicit confirmation this specific run
is authorized against that target -- default to a snapshot/staging copy.

1. Row counts: compare source vs destination per affected table, after
   getting explicit confirmation of any *expected* filtering/dedup --
   don't assume exact-match is the right expectation without checking.
2. Field-level sampling: pull a real sample including boundary/edge
   records (nulls, max-length strings, unusual characters, extreme
   numbers) and compare field-by-field. Watch for silent truncation,
   precision loss (rounded decimals, dropped timezone info), encoding
   issues.
3. Referential integrity: verify foreign keys/relationships still
   resolve post-migration -- an orphaned reference is a bug even if every
   row "migrated" individually.
4. Idempotency: if the job might run more than once, verify a second run
   doesn't duplicate/corrupt data. State explicitly if you only tested a
   single run.
5. Rollback: if a rollback exists, actually run it against a test copy
   and verify it restores prior state -- don't assume it works because it
   exists.
6. For large datasets: use checksums/hashes rather than skipping
   verification, and state your real coverage (e.g. "100% via checksum,
   50 records spot-checked field-by-field") rather than implying full
   verification from a small sample.

Report: what was compared, what matched, specific discrepancies (record
+ field, not "some records differ"), and whether rollback was verified.
Never report a migration as safe without having actually compared real
before/after data.
```

## Notes

Distinct from `test-data-setup.md` (prepares/anonymizes data for
testing) -- this checks whether data stayed correct across an actual
transformation, independent of whether the app built on it still works.
