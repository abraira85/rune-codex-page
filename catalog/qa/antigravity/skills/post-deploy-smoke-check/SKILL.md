---
name: post-deploy-smoke-check
status: experimental
context: "Ported from the Claude post-deploy-smoke-check skill (../../../claude/skills/post-deploy-smoke-check/SKILL.md) — not yet run against a real production deploy."
description: Run a fast, time-boxed check against real production right after a deploy to catch a broken release before users report it -- distinct from release-smoke-checklist, which runs before shipping.
---

# Post-Deploy Smoke Check

## When to use this skill

Invoke immediately after a deploy has already gone out to production.
The question here is "did this deploy just break something in the
wild," not "should we ship" (that's `release-smoke-checklist`, which
runs *before* the deploy). This is the fastest possible check, aimed at
triggering a rollback decision quickly if something's wrong -- not a
full investigation.

## Prompt / instructions

```
Run a post-deploy smoke check against production:

1. Identify the smallest set of checks that would catch "this deploy
   broke something important" -- the same critical paths
   `release-smoke-checklist` would have flagged pre-release (auth,
   checkout/payment, core CRUD, primary nav), but now run as synthetic
   checks against the real, live production URLs, not staging.
2. If the project has observability in place (an error-rate dashboard,
   APM, a metrics endpoint), check it for a spike immediately after the
   deploy timestamp -- a real signal is faster and more comprehensive
   than a handful of synthetic checks alone. If nothing is available,
   say so and rely on the synthetic checks only.
3. Time-box this aggressively -- tighter than a pre-release smoke suite,
   since the goal is a fast rollback/no-rollback signal, not thoroughness.
   State the budget (a few minutes) up front.
4. For each check: what was hit (real prod URL/endpoint), what was
   expected, what was actually observed. Never simulate this against
   staging and report it as a production check.
5. If something looks broken: this is a trigger for a rollback decision,
   not a full investigation -- report it immediately with what's known,
   and hand off to `bug-triage-analyst` for the actual root-cause work
   once the immediate ship/rollback call is made.
6. If everything passes, report that plainly and briefly -- this isn't
   the place for a long write-up when nothing's wrong.

Never skip this because "the release-smoke-checklist already passed
pre-deploy" -- a deploy can fail for reasons the pre-release check
couldn't see (bad config in the real environment, a migration that
didn't apply cleanly, an infra issue specific to production).
```

## Notes

Distinct from `release-smoke-checklist` in this same folder: that one
runs pre-release against staging/a release candidate to decide whether
to ship; this one runs post-release against real production to catch
what only shows up once real traffic and real infrastructure are
involved. Use both -- neither substitutes for the other. Ported unchanged
in substance from `../../../claude/skills/post-deploy-smoke-check/SKILL.md`.
