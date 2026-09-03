---
name: post-deploy-smoke-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Post-Deploy Smoke Check (standalone prompt)

Runs a fast check against real production right after a deploy — the
Codex-side equivalent of the Claude `post-deploy-smoke-check` skill.
Distinct from `release-smoke-check.md`, which runs before shipping.

## Prompt / instructions

```
Run a post-deploy smoke check for the release that just went out:

1. Identify the smallest set of checks that would catch "this deploy
   broke something important" -- the same critical paths a pre-release
   smoke check would cover, but now run against real, live production
   URLs, not staging.
2. If observability is available (error-rate dashboard, APM, a metrics
   endpoint), check it for a spike right after the deploy timestamp --
   that signal is faster and more comprehensive than synthetic checks
   alone. If nothing is available, say so and rely on synthetic checks
   only.
3. Time-box this aggressively -- tighter than a pre-release smoke
   budget, since the goal is a fast rollback/no-rollback signal. State
   the budget up front (a few minutes).
4. For each check: what was hit (real prod URL), what was expected, what
   was actually observed. Never simulate this against staging and report
   it as a production check.
5. If something looks broken, that's a trigger for a rollback decision --
   report immediately with what's known, and hand off to `bug-report.md`
   in this folder for the actual root-cause work once the immediate
   ship/rollback call is made.
6. If everything passes, report that plainly and briefly.

Never skip this because the pre-release smoke check already passed --
production-only failure modes (bad env config, an incompletely-applied
migration, prod-specific infra) can't be caught pre-deploy.
```

## Notes

Distinct from `release-smoke-check.md` in this folder: that one runs
pre-release to decide whether to ship; this one runs post-release to
catch what only shows up with real traffic and real infrastructure. Use
both.
