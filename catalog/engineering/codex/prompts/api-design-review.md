---
name: api-design-review
status: experimental
context: "Authored for rune-codex-page's engineering team — not yet run in a real project."
---

# API Design Review (standalone prompt)

Reviews a change to a public interface for breaking-change risk,
versioning, and interface design — the Codex-side equivalent of the
Claude `api-design-reviewer` agent. Not a re-check of implementation
correctness (that's `code-review.md`).

## Prompt / instructions

```
Review the following public-interface change:

CHANGE: <diff or description of the API/library/schema/CLI change>

1. Identify what's actually public here -- real external callers this
   interface has, from actual usage (other services, documented
   consumers) rather than assumption.
2. Classify: additive (new optional field/endpoint/function with a
   default -- generally safe, but check it doesn't silently change
   existing behavior) vs breaking (removed/renamed field or endpoint,
   changed required params, changed response shape, changed error
   codes/semantics, changed default behavior).
3. For a breaking change: check whether the project has a real
   versioning/deprecation strategy and whether this change follows it.
   No strategy + a silent breaking change = Blocking, regardless of how
   clean the implementation is.
4. Check interface design on its own terms: consistency with the rest of
   the API (naming, error format, pagination style), whether it leaks
   internal implementation details it shouldn't, whether a new required
   field forces every caller to change immediately with no migration
   path.
5. Check documentation: does the actual API spec (OpenAPI/GraphQL
   schema/whatever is source of truth) get updated in this diff, or does
   it now disagree with real behavior? Undocumented interface change is
   itself a finding.
6. If a schema-diff tool or contract tests exist in the project, run
   them rather than eyeballing compatibility.

Report each finding via the format in `code-review.md`'s comment
guidance: location, what's wrong, why it matters (name the specific
caller/scenario that breaks), severity. A breaking change with no
versioning strategy is Blocking by default.
```

## Notes

For a change with no public interface involved, this prompt has nothing
to add -- `code-review.md` alone is sufficient.
