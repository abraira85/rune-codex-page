---
name: pre-commit-test-gate
status: experimental
context: "Ported from the Claude pre-commit-test-gate hook (../../claude/hooks/pre-commit-test-gate.md) — not yet run in a real project. The hook mechanism itself (Decide hooks, JSON decision on stdout) differs from Claude's exit-code model, so this is a real re-implementation, not just a config translation -- verify against current Antigravity hooks docs before relying on it."
description: Blocks an Antigravity agent from running `git commit` via run_command until the project's test command passes, so a broken test suite can't get committed silently.
---

# Pre-commit Test Gate

A `PreToolUse` **Decide hook** (read-only, blocking: it can allow or deny
a pending tool call, but not modify it) on the `run_command` tool: when
an agent is about to run `git commit`, the hook runs the project's real
test command first and denies the commit if it fails. Complements
`test-automation-engineer` in `../agents/` — that role writes tests, this
hook makes sure they actually get run before code lands.

Unlike Claude Code's hook contract (a shell script that signals
allow/block via its **exit code**), Antigravity's Decide hooks signal
their decision via a **JSON object on stdout** (`{"decision": "allow" |
"deny", "reason": "..."}`) — see the example in Antigravity's own hooks
docs. This file re-implements the gate's logic for that contract; it
isn't a drop-in copy of the Claude version's script.

## Prompt / instructions

`.agents/hooks.json`:

```json
{
  "qa-gate": {
    "PreToolUse": [
      {
        "matcher": "run_command",
        "hooks": [
          {
            "type": "command",
            "command": "./.agents/hooks/qa-gate.sh",
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

`.agents/hooks/qa-gate.sh` (create alongside the config above, `chmod +x` it):

```bash
#!/usr/bin/env bash
# Blocks `git commit` via run_command until tests pass.
# Configure the test command via QA_GATE_TEST_CMD, or drop a
# .qa-gate-cmd file in the repo root containing the command.
#
# NOTE: this reads the raw stdin payload as text (like Antigravity's own
# documented hook example does) rather than parsing a specific JSON field
# for the command string, since the exact PreToolUse payload shape for
# run_command wasn't confirmed at the time this was written. If your
# Antigravity build's payload is structured differently, adjust the
# case/grep below to match the real field.
set -euo pipefail

input="$(cat)"

case "$input" in
  *"git commit"*) ;;
  *) echo '{"decision": "allow"}'; exit 0 ;;  # not a commit -- allow
esac

test_cmd="${QA_GATE_TEST_CMD:-}"
if [ -z "$test_cmd" ] && [ -f ".qa-gate-cmd" ]; then
  test_cmd="$(cat .qa-gate-cmd)"
fi

if [ -z "$test_cmd" ]; then
  echo '{"decision": "allow", "reason": "qa-gate: no test command configured (set QA_GATE_TEST_CMD or .qa-gate-cmd) -- skipping, not blocking"}'
  exit 0
fi

if eval "$test_cmd" >/tmp/qa-gate-output.$$ 2>&1; then
  echo '{"decision": "allow"}'
else
  reason="qa-gate: '$test_cmd' failed -- commit blocked until tests pass"
  # Keep the reason on one line -- it goes into a JSON string.
  echo "{\"decision\": \"deny\", \"reason\": \"$(echo "$reason" | tr '\n' ' ')\"}"
fi
rm -f /tmp/qa-gate-output.$$
```

## Notes

- This mirrors the Claude-side `pre-commit-test-gate` hook's *intent*
  (block a commit until tests pass) exactly, but the mechanism is a real
  port, not a copy — Antigravity's Decide hooks communicate allow/deny
  via a JSON stdout payload rather than an exit code, and this script's
  input-parsing (raw text match instead of a parsed JSON field) is
  deliberately conservative because the exact `run_command` PreToolUse
  payload shape wasn't confirmed when this was written. Check current
  Antigravity hooks docs and adjust the parsing if the real payload
  structure differs.
- Deliberately fails open (allows the commit) when no test command is
  configured, rather than blocking every commit in projects that haven't
  set `QA_GATE_TEST_CMD` — same reasoning as the Claude version: a
  silently-blocking hook with no clear cause is worse than one that's
  just inactive until configured.
- Only gates commands containing `git commit`, not every `run_command`
  call — other shell commands pass through untouched (`{"decision":
  "allow"}` on the first non-matching branch). Adjust the `case` pattern
  if you also want to gate `git push` or similar.
- See `../../claude/hooks/pre-commit-test-gate.md` for the Claude-side
  original this was ported from.
