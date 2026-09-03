---
name: dependency-review
status: experimental
context: "Authored for rune-codex-page's engineering team — not yet run in a real project."
---

# Dependency Review (standalone prompt)

Checks a dependency change for necessity, license, and known
vulnerabilities using real tooling — the Codex-side equivalent of the
Claude `dependency-reviewer` agent.

## Prompt / instructions

```
Review the following dependency change:

CHANGE: <added/removed/upgraded package(s)>

1. Necessity: is it actually used in this diff for something meaningfully
   harder without it, or does it pull in a large package for something
   that could be a few lines of project code? Should-fix, not Blocking,
   but worth raising.
2. Run the project's real audit tool (`npm audit`, `pip-audit`,
   `cargo audit`, `bundle audit`, or whatever the stack uses) against the
   new/changed dependency tree. Report actual findings (CVE, package,
   the tool's own severity) -- don't estimate risk from the name/version.
3. License: read the actual license of the new dependency and check
   compatibility with the project's license/use case. A copyleft license
   in a proprietary/permissive project is a real legal issue, not a
   style nit. If you can't determine the license, say so.
4. Version-pinning: does this follow the project's own existing
   convention (exact version, caret/tilde range, lockfile committed)? A
   change that loosens pinning in an otherwise-strict project is worth
   flagging.
5. For an upgrade: check the actual changelog/release notes for the
   version jump, especially across a major bump. If not accessible, say
   so rather than assuming the upgrade is behavior-neutral.
6. Supply-chain sanity for an unfamiliar/new package: maintenance
   activity, download counts, whether it's a typosquat of a well-known
   name -- not a full audit, just the obvious cases.

Report each finding via the format in `code-review.md`'s comment
guidance. Never report a dependency as clean without having actually run
the audit tool in this session.
```

## Notes

For a diff with no dependency changes, this prompt has nothing to add.
