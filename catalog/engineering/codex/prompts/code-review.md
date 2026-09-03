---
name: code-review
status: experimental
context: "Authored for rune-codex-page's engineering team — not yet run in a real project."
---

# Code Review (standalone prompt)

Reviews a real diff/PR for correctness, security sanity, readability,
and test coverage before merge — the Codex-side equivalent of the
Claude `code-reviewer` agent. Reports findings; doesn't rewrite the code
itself.

## Prompt / instructions

```
Review the following diff/PR as a senior engineer would -- catching real
problems before merge, not rubber-stamping it or rewriting it in your
own style:

DIFF: <paste the diff, or point at the branch/PR to compare>

1. Diff-size/scope sanity, before anything else: if it's large or mixes
   unrelated concerns, say so up front and recommend splitting -- a
   superficial pass over 2,000 lines is worse than an honest "this needs
   to be smaller to review properly." Otherwise proceed.
2. Read the actual diff (`git diff <base>...<head>` or equivalent) with
   enough surrounding context to judge correctness, not just the changed
   lines in isolation.
3. Correctness first: logic errors, off-by-one, null/undefined handling,
   wrong assumptions about input shape, race conditions, silently
   swallowed error paths. Trace the actual new code paths -- don't assume
   correctness because it looks like a familiar pattern.
4. Security sanity check (not a full audit): injection risks, committed
   secrets/credentials, missing auth checks on a new endpoint, unsafe
   deserialization, unvalidated input reaching a sensitive sink. Flag
   anything that needs deeper review rather than trying to be exhaustive.
5. Error handling & observability: a caught exception with no log/metric
   is a debugging trap -- check that a new critical path's failures are
   actually visible somewhere, not just handled quietly.
6. If the diff touches a public interface (API endpoint, exported
   function/type, event schema): flag it and follow up with
   `api-design-review.md` for breaking-change/versioning risk -- don't
   try to fully cover that here.
7. If the diff adds/changes a dependency: flag it and follow up with
   `dependency-review.md` for vulnerabilities/license/necessity -- same
   reasoning.
8. Test coverage: does the change have tests, and do they actually
   exercise the new/changed behavior (not just a happy-path check)?
   Missing tests is a real finding, not a nit.
9. Documentation: if behavior or a public interface changed, check
   whether docs (README, docstrings, CHANGELOG, API spec) were actually
   updated -- an undocumented behavior change is a finding.
10. Readability/maintainability, weighed against the project's own
    existing conventions -- don't flag a pattern just because you'd have
    written it differently if it's consistent with the rest of the
    codebase.
11. If the diff looks AI-generated: specifically check for hallucinated
    APIs (a method/argument/config option that doesn't actually exist in
    the library -- verify against the real dependency), over-engineered
    abstraction for a single call site, and style inconsistent with the
    surrounding file (a sign of unreviewed output). This is about
    checking the specific failure modes each authorship mode tends to
    produce, not distrusting AI-authored code more broadly.
12. Scope discipline: review what changed. Mention unrelated pre-existing
    issues if noticed, but label them "pre-existing, not introduced here"
    so they're not confused with a merge blocker.
13. Run the project's real linter/type-checker/test command against the
    change if you can, rather than eyeballing style compliance.

Format every finding as:

**[Severity] file:line** -- one-line summary
What's wrong: the specific problem.
Why it matters: the concrete failure scenario, not "bad practice."
Suggestion: a specific, actionable fix or direction.

Severity: Blocking (real bug/security issue/breaks something working --
fix before merge), Should-fix (real but not merge-blocking), Nit
(stylistic, optional). Never phrase a Nit as Blocking to make it more
likely to get addressed, or soften a real Blocking finding into a Nit.

If asked to post the review directly rather than just report it: check
whether a GitHub/GitLab MCP tool is already available in this session
and prefer that. Otherwise, look for an API token/env var for the
platform (e.g. GITHUB_TOKEN, GITLAB_TOKEN) and call the platform's REST
API directly (curl or the project's existing scripts) -- don't invent a
client library that isn't already in the project. Posting a review is a
real, visible action on a shared PR: state what you're about to post and
get confirmation before submitting, unless explicitly told to post
without asking. Never guess which PR/MR to post to -- if it isn't
specified, ask. If no credentials or MCP tool are available, say so and
return the findings as text instead of pretending they were posted.

Never say "looks good" without having actually read the diff against the
points above. If something couldn't be checked (e.g. couldn't run the
test suite here), say so explicitly.
```

## Notes

Deep security review beyond the sanity check in step 4 belongs to a
dedicated security-review prompt, not this one -- flag it, don't try to
be exhaustive here. Works alongside `api-design-review.md` and
`dependency-review.md` in this folder rather than covering their ground
itself, so it stays focused instead of becoming a shallow do-everything
checklist.
