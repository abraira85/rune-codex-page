---
name: mobile-app-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Mobile App Check (standalone prompt)

Drives a real native iOS/Android app via Appium — the Codex-side
equivalent of the Claude `mobile-app-tester` agent. Not for mobile web
(that's `browser-e2e-check.md` with a mobile viewport).

## Prompt / instructions

```
Check the following native app feature/flow:

TARGET: <feature/flow>
PLATFORM(S): <iOS, Android, or both -- test each separately>

1. Confirm Appium plus the relevant driver (XCUITest for iOS,
   UiAutomator2 for Android) and a simulator/emulator are available or
   installable. If not, say so instead of inferring behavior from code.
2. Launch the real app via the project's actual build/install steps.
3. Drive the exact user action via Appium (taps, swipes, text entry,
   platform gestures). Assert on real resulting app state, not just "no
   crash."
4. Specifically check native-platform behaviors:
   - Permission dialogs (camera, location, notifications) -- correct
     prompt, correct behavior on grant and deny
   - App lifecycle: background/foreground, rotation, low-memory if
     simulatable -- does state survive correctly?
   - Deep links / universal links if used
   - Offline/poor-network behavior if the feature depends on network
5. Screenshot on failure, same discipline as browser testing.
6. Report per platform separately: what was driven, what was observed,
   pass/fail with screenshot reference for failures. Never imply a
   result for a platform you didn't actually run the app on.
```

## Notes

Complements `cross-browser-check.md`'s matrix-breadth approach, but for
native platforms instead of browser engines.
