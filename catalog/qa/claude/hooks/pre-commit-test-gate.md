---
name: pre-commit-test-gate
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project. Move to production once it's actually blocked a bad commit."
description: Blocks Claude from running `git commit` via the Bash tool until the project's test command passes, so a broken test suite can't get committed silently.
---

# Pre-commit Test Gate

A `PreToolUse` hook on the `Bash` tool: when Claude is about to run a
`git commit`, the hook runs the project's real test command first and
blocks the commit if it fails. Complements `test-automation-engineer` in
this same folder — that role writes tests, this hook makes sure they
actually get run before code lands.

## Prompt / instructions

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/qa-gate.sh"
          }
        ]
      }
    ]
  }
}
```

`.claude/hooks/qa-gate.sh` (create alongside the settings above, `chmod +x` it):

```bash
#!/usr/bin/env bash
# Blocks `git commit` via the Bash tool until tests pass.
# Configure the test command via QA_GATE_TEST_CMD, or drop a
# .qa-gate-cmd file in the repo root containing the command.
set -euo pipefail

input="$(cat)"
command_run="$(echo "$input" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null || true)"

case "$command_run" in
  *"git commit"*) ;;
  *) exit 0 ;;  # not a commit -- allow, nothing to check
esac

test_cmd="${QA_GATE_TEST_CMD:-}"
if [ -z "$test_cmd" ] && [ -f ".qa-gate-cmd" ]; then
  test_cmd="$(cat .qa-gate-cmd)"
fi

if [ -z "$test_cmd" ]; then
  echo "qa-gate: no test command configured (set QA_GATE_TEST_CMD or .qa-gate-cmd) -- skipping, not blocking" >&2
  exit 0
fi

if ! eval "$test_cmd"; then
  echo "qa-gate: '$test_cmd' failed -- commit blocked until tests pass" >&2
  exit 2
fi

exit 0
```

## Notes

- Exit code `2` is what tells Claude Code to block the tool call and show
  the stderr message as the reason; exit `0` allows it. This is the
  documented Claude Code hook contract as of this writing -- if it's
  changed since, check the current hooks docs before relying on this.
- Deliberately fails open (allows the commit) when no test command is
  configured, rather than blocking every commit in projects that haven't
  set `QA_GATE_TEST_CMD` -- a silently-blocking hook with no clear cause
  is worse than one that's just inactive until configured.
- Only gates `git commit`, not every `Bash` call -- other shell commands
  pass through untouched. Adjust the `case` pattern if you also want to
  gate `git push` or similar.
- `$CLAUDE_PROJECT_DIR` is set by Claude Code itself; don't hardcode a
  path.
