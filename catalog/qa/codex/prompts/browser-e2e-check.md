---
name: browser-e2e-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Browser E2E Check (standalone prompt)

A one-shot task prompt for verifying a specific feature by actually
driving a browser — the Codex-side equivalent of the Claude
`browser-automation-tester` agent, phrased as a standalone instruction
rather than a persistent role.

## Prompt / instructions

```
Verify the following feature by actually running it in a browser, not by
reading the code and inferring behavior:

FEATURE: <describe the feature/flow to check>
EXPECTED BEHAVIOR: <what should happen>

Steps:
1. Confirm Playwright is available (`npx playwright --version`); install
   it if missing and you're able to (`npm i -D playwright && npx
   playwright install`). If you can't install it, stop and say so instead
   of guessing at the result.
2. Start the app using the project's real dev/start script if it isn't
   already running.
3. Write a short, throwaway Playwright script that navigates to the
   relevant page, performs the exact action described above, and asserts
   on the resulting DOM state.
4. Run it. On failure, take a screenshot and read it before concluding
   what went wrong.
5. Delete the throwaway script when done — don't leave test scaffolding
   in the repo unless asked to.
6. Report: what you did, what you observed, and whether it matched
   EXPECTED BEHAVIOR. Include the failure screenshot reference if there
   was one. Never report success without having actually run the browser.
```

## Notes

Fill in FEATURE and EXPECTED BEHAVIOR before using. For a lasting
automated test instead of a one-time check, see the project's existing
test suite conventions (or `qa-conventions.md` in `../agents-md/`).
