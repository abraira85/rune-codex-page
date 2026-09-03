---
name: localization-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Localization Check (standalone prompt)

Checks that a UI renders correctly across locales — the Codex-side
equivalent of the Claude `localization-tester` agent. Not a translation
quality review.

## Prompt / instructions

```
Check the following page/flow for localization correctness:

TARGET: <page/flow>
LOCALES: <the project's real supported locale list -- don't invent one>

1. Confirm Playwright is available or installable.
2. Missing-key check: for each locale, look for UI text that silently
   fell back to the source language instead of the translated string.
3. Text expansion/truncation: check that longer-running locales (German,
   Finnish, etc.) don't clip/overflow/wrap-break the layout, and that
   shorter locales don't leave a layout looking broken/sparse.
4. RTL layout (if RTL locales are supported): check that mirroring is
   correct site-wide, not just that text direction flips.
5. Locale-aware formatting: dates, times, numbers, currency,
   pluralization -- check actual rendered values per locale, don't
   assume the i18n library handles it correctly just because it's wired
   up.
6. Use pseudo-localization if the project supports it, to catch
   hardcoded/non-translatable strings across the whole app at once.

Report per finding: locale, page/element, what's wrong, screenshot if
visual. Name exactly which locales were actually checked -- never imply
coverage for locales you didn't verify.

Scope: technical i18n correctness only. Translation quality/cultural
appropriateness needs a native-speaker review -- flag it as such rather
than judging it yourself.
```

## Notes

Complements `browser-e2e-check.md` (functional behavior) and
`visual-regression-check.md` (pixel diffing) -- this one is specifically
about the locale dimension neither of those covers by default.
