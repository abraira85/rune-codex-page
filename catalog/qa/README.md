# qa/

Testing, quality assurance, functional and automated validation.

## Team (Claude)

`qa-lead` decides strategy and scope; the specialists execute; `bug-triage-analyst`
turns findings into actionable reports. All `experimental`: written for this
repo, not yet run against a real project — see each file's `context` field.

| Agent | Role |
|---|---|
| [`qa-lead`](./claude/agents/qa-lead.md) | Test strategy, scope, and the ship/no-ship call |
| [`functional-tester`](./claude/agents/functional-tester.md) | Manual/exploratory test cases against a spec |
| [`browser-automation-tester`](./claude/agents/browser-automation-tester.md) | Drives a real browser (Playwright) to verify a feature |
| [`test-automation-engineer`](./claude/agents/test-automation-engineer.md) | Writes lasting automated tests into the project's suite |
| [`api-tester`](./claude/agents/api-tester.md) | Tests REST/GraphQL endpoints against their real contract |
| [`accessibility-auditor`](./claude/agents/accessibility-auditor.md) | WCAG audit via automated scanning (axe) |
| [`performance-tester`](./claude/agents/performance-tester.md) | Load/stress testing and performance-budget checks with real measurements |
| [`bug-triage-analyst`](./claude/agents/bug-triage-analyst.md) | Reproduces, minimizes, and severity-rates a bug report |

| Skill | For |
|---|---|
| [`test-case-writer`](./claude/skills/test-case-writer/SKILL.md) | Generate a test case matrix from a spec |
| [`bug-report-template`](./claude/skills/bug-report-template/SKILL.md) | Format a reproduced bug consistently |

| MCP / Hook | For |
|---|---|
| [`playwright-mcp`](./claude/mcp/playwright-mcp.md) | Direct structured browser control instead of Bash-run scripts |
| [`pre-commit-test-gate`](./claude/hooks/pre-commit-test-gate.md) | Blocks `git commit` until the project's tests pass |

## Team (Codex)

Codex doesn't have persistent named subagents, so the same QA function is
split differently: one project-wide `AGENTS.md` convention, plus
standalone task prompts for the parts that don't fit "always-on
convention."

| Item | For |
|---|---|
| [`qa-conventions`](./codex/agents-md/qa-conventions.md) | AGENTS.md section: testing expectations for any coding agent in the project |
| [`test-case-matrix`](./codex/prompts/test-case-matrix.md) | One-shot: generate a test case matrix from a spec |
| [`browser-e2e-check`](./codex/prompts/browser-e2e-check.md) | One-shot: verify a feature by actually driving a browser |
| [`bug-report`](./codex/prompts/bug-report.md) | One-shot: reproduce and write up a bug report |

## `~ ❯ ls`

| Path | For |
|---|---|
| [`claude/agents/`](./claude/agents) | Claude Code subagent definitions |
| [`claude/skills/`](./claude/skills) | Reusable Claude Skills |
| [`claude/mcp/`](./claude/mcp) | MCP server configs |
| [`claude/hooks/`](./claude/hooks) | Claude Code hook configs |
| [`codex/agents-md/`](./codex/agents-md) | `AGENTS.md` templates |
| [`codex/prompts/`](./codex/prompts) | Standalone Codex CLI / custom-instruction prompts |

Each item follows the format in [`../../TEMPLATE.md`](../../TEMPLATE.md) and must pass [`../../scripts/validate.py`](../../scripts/validate.py). Install a Claude/Codex-writable item with `python3 scripts/install.py <path>` — see the root [`README.md`](../../README.md#-❯-man-install).
