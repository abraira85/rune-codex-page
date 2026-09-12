---
name: migration-safety-checklist
status: experimental
context: "Initial experimental version."
description: "Backward-compatibility and reversibility checklist."
---

# Database Migration Safety Checklist

- [ ] Does this require a table lock? If so, is the table small enough, or are we using concurrent indexing?
- [ ] Is this migration backward-compatible with the currently running application code?
- [ ] Have we separated schema changes from data backfills?
- [ ] Is the `down` (rollback) script tested and perfectly reversible?
- [ ] Does this add a required column without a default value? (If so, it breaks inserts).
