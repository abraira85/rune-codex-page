---
name: accessibility-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Accessibility Check (standalone prompt)

Runs a WCAG audit via automated scanning — the Codex-side equivalent of
the Claude `accessibility-auditor` agent.

## Prompt / instructions

```
Audit the following page/component for accessibility:

TARGET: <URL, route, or component name>
LEVEL: <WCAG 2.1 A / AA / AAA -- default to AA if not specified>

1. Run an automated scan (axe-core via Playwright, @axe-core/cli, or
   equivalent already available in this project) against the rendered
   page -- do not eyeball the markup and guess violations.
2. For each violation reported, include: the WCAG success criterion, the
   specific element (selector or unique identifying detail), and the
   automated tool's own impact rating (critical/serious/moderate/minor)
   -- do not re-invent severity language.
3. Automated scanners catch roughly a third of real issues. After the
   scan, manually check what tools can't:
   - Full keyboard navigation (tab order, focus visible, no traps)
   - Screen-reader-relevant structure: heading hierarchy, landmark
     regions, alt text that's actually descriptive (not just present)
   - Color contrast on states a static scan may miss (hover, disabled,
     placeholder text)
4. Separate findings into "automated (tool: X)" vs "manual" so the
   report doesn't overstate automated coverage.
5. For each finding, state the concrete fix (e.g. "add aria-label to
   button at line N", not "improve accessibility of button").

Never claim a page is accessible because the automated scan came back
clean -- state explicitly that automated scanning covers a subset of
WCAG and name what was manually checked beyond it.
```

## Notes

If no scanner is installed yet, the prompt should install one
(`@axe-core/playwright` or similar) rather than fabricate results from
reading markup alone.
