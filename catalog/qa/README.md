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
| [`exploratory-tester`](./claude/agents/exploratory-tester.md) | Session-based, charter-driven exploratory testing (SBTM) -- no pre-written cases |
| [`browser-automation-tester`](./claude/agents/browser-automation-tester.md) | Drives a real browser (Playwright) to verify a feature |
| [`visual-regression-tester`](./claude/agents/visual-regression-tester.md) | Pixel-level screenshot comparison against a baseline |
| [`cross-browser-tester`](./claude/agents/cross-browser-tester.md) | Runs a verified scenario across the real browser/device support matrix |
| [`mobile-app-tester`](./claude/agents/mobile-app-tester.md) | Drives a real native iOS/Android app (Appium) |
| [`localization-tester`](./claude/agents/localization-tester.md) | Checks i18n/l10n rendering, layout, and formatting per locale |
| [`test-automation-engineer`](./claude/agents/test-automation-engineer.md) | Writes lasting automated tests into the project's suite |
| [`test-data-engineer`](./claude/agents/test-data-engineer.md) | Realistic/reproducible fixtures, and safe prod-to-test data anonymization |
| [`data-migration-tester`](./claude/agents/data-migration-tester.md) | Verifies a migration/ETL job for real data integrity (row counts, field diffs, referential integrity, rollback) |
| [`coverage-analyst`](./claude/agents/coverage-analyst.md) | Finds which specific undertested code paths actually matter |
| [`api-tester`](./claude/agents/api-tester.md) | Tests REST/GraphQL endpoints against their real contract |
| [`contract-tester`](./claude/agents/contract-tester.md) | Verifies a provider against every real consumer's contract (Pact) |
| [`accessibility-auditor`](./claude/agents/accessibility-auditor.md) | WCAG audit via automated scanning (axe) |
| [`performance-tester`](./claude/agents/performance-tester.md) | Load/stress testing and performance-budget checks with real measurements |
| [`chaos-resilience-tester`](./claude/agents/chaos-resilience-tester.md) | Real fault injection to verify graceful degradation (highest blast-radius role) |
| [`bug-triage-analyst`](./claude/agents/bug-triage-analyst.md) | Reproduces, minimizes, and severity-rates a bug report |
| [`flaky-test-investigator`](./claude/agents/flaky-test-investigator.md) | Tells apart a real flake from a real intermittent bug, fixes or quarantines properly |

| Skill | For |
|---|---|
| [`test-case-writer`](./claude/skills/test-case-writer/SKILL.md) | Generate a test case matrix from a spec |
| [`bug-report-template`](./claude/skills/bug-report-template/SKILL.md) | Format a reproduced bug consistently |
| [`release-smoke-checklist`](./claude/skills/release-smoke-checklist/SKILL.md) | Fast, time-boxed pre-release smoke suite ending in a go/no-go input |
| [`post-deploy-smoke-check`](./claude/skills/post-deploy-smoke-check/SKILL.md) | Fast check against real production right after a deploy |

| MCP / Hook | For |
|---|---|
| [`playwright-mcp`](./claude/mcp/playwright-mcp.md) | Direct structured browser control instead of Bash-run scripts |
| [`issue-tracker-mcp`](./claude/mcp/issue-tracker-mcp.md) | Lets `bug-triage-analyst` file the ticket directly into Jira/Trello/Notion/similar instead of only writing markdown |
| [`test-management-mcp`](./claude/mcp/test-management-mcp.md) | Syncs `test-case-writer`'s matrix and results into TestRail/Xray/Zephyr/Qase/similar (speculative — verify server availability first) |
| [`pre-commit-test-gate`](./claude/hooks/pre-commit-test-gate.md) | Blocks `git commit` until the project's tests pass |

## Team (Codex)

Codex doesn't have persistent named subagents, so each Claude role
becomes a standalone task prompt instead of an installed agent file —
same role, same instructions, invoked per-task rather than by name. One
project-wide `AGENTS.md` convention sits alongside them for the
always-on expectations that don't belong in a one-shot prompt.

| Item | Claude equivalent | For |
|---|---|---|
| [`qa-conventions`](./codex/agents-md/qa-conventions.md) | — | AGENTS.md section: testing expectations for any coding agent in the project |
| [`qa-strategy`](./codex/prompts/qa-strategy.md) | `qa-lead` | One-shot: scope test strategy and make the ship/no-ship call |
| [`test-case-matrix`](./codex/prompts/test-case-matrix.md) | `functional-tester` | One-shot: generate a test case matrix from a spec |
| [`exploratory-session`](./codex/prompts/exploratory-session.md) | `exploratory-tester` | One-shot: session-based, charter-driven exploratory testing (SBTM) |
| [`browser-e2e-check`](./codex/prompts/browser-e2e-check.md) | `browser-automation-tester` | One-shot: verify a feature by actually driving a browser |
| [`visual-regression-check`](./codex/prompts/visual-regression-check.md) | `visual-regression-tester` | One-shot: pixel-level screenshot comparison against a baseline |
| [`cross-browser-check`](./codex/prompts/cross-browser-check.md) | `cross-browser-tester` | One-shot: run a verified scenario across the real browser/device matrix |
| [`mobile-app-check`](./codex/prompts/mobile-app-check.md) | `mobile-app-tester` | One-shot: drive a real native iOS/Android app (Appium) |
| [`localization-check`](./codex/prompts/localization-check.md) | `localization-tester` | One-shot: check i18n/l10n rendering, layout, and formatting per locale |
| [`write-automated-test`](./codex/prompts/write-automated-test.md) | `test-automation-engineer` | One-shot: write a lasting automated test into the project's suite |
| [`test-data-setup`](./codex/prompts/test-data-setup.md) | `test-data-engineer` | One-shot: realistic/reproducible fixtures, safe prod-to-test anonymization |
| [`data-migration-check`](./codex/prompts/data-migration-check.md) | `data-migration-tester` | One-shot: verify a migration/ETL job for real data integrity |
| [`coverage-analysis`](./codex/prompts/coverage-analysis.md) | `coverage-analyst` | One-shot: find which specific undertested code paths actually matter |
| [`api-contract-check`](./codex/prompts/api-contract-check.md) | `api-tester` | One-shot: test an endpoint against its real contract |
| [`contract-check`](./codex/prompts/contract-check.md) | `contract-tester` | One-shot: verify a provider against every real consumer's contract (Pact) |
| [`accessibility-check`](./codex/prompts/accessibility-check.md) | `accessibility-auditor` | One-shot: WCAG audit via automated scanning |
| [`performance-check`](./codex/prompts/performance-check.md) | `performance-tester` | One-shot: load/stress test against a performance budget |
| [`chaos-resilience-check`](./codex/prompts/chaos-resilience-check.md) | `chaos-resilience-tester` | One-shot: real fault injection to verify graceful degradation |
| [`bug-report`](./codex/prompts/bug-report.md) | `bug-triage-analyst` | One-shot: reproduce and write up a bug report |
| [`flaky-test-check`](./codex/prompts/flaky-test-check.md) | `flaky-test-investigator` | One-shot: tell apart a real flake from a real intermittent bug |
| [`release-smoke-check`](./codex/prompts/release-smoke-check.md) | `release-smoke-checklist` | One-shot: fast pre-release smoke suite ending in a go/no-go input |
| [`post-deploy-smoke-check`](./codex/prompts/post-deploy-smoke-check.md) | `post-deploy-smoke-check` | One-shot: fast check against real production right after a deploy |

## Team (Antigravity)

Google Antigravity turned out to have real persistent subagents — a
`.md` file with YAML frontmatter per agent, auto-discovered from
`.agents/agents/`, delegated to by description — much closer to Claude
Code's model than to Codex's. So this side mirrors `claude/` 1:1 rather
than getting the Codex treatment: same 19 agents, 4 skills, 3 MCP
configs, and 1 hook, re-packaged for Antigravity's frontmatter fields,
tool names (`view_file`/`run_command`/etc. instead of `Read`/`Bash`), and
file locations (`.agents/agents/`, `.agents/skills/`, `.agents/mcp_config.json`,
`.agents/hooks.json`). The hook is a real re-implementation, not just a
config translation — see its file for why. `qa/` is piloting this tool
track before it rolls out to the other 6 areas; verify specifics against
current Antigravity docs before relying on any of this in production, as
noted per-file.

| Item | Claude equivalent | For |
|---|---|---|
| [`qa-lead`](./antigravity/agents/qa-lead.md) | `qa-lead` | Test strategy, scope, and the ship/no-ship call |
| [`functional-tester`](./antigravity/agents/functional-tester.md) | `functional-tester` | Manual/exploratory test cases against a spec |
| [`exploratory-tester`](./antigravity/agents/exploratory-tester.md) | `exploratory-tester` | Session-based, charter-driven exploratory testing (SBTM) |
| [`browser-automation-tester`](./antigravity/agents/browser-automation-tester.md) | `browser-automation-tester` | Drives a real browser (Playwright) to verify a feature |
| [`visual-regression-tester`](./antigravity/agents/visual-regression-tester.md) | `visual-regression-tester` | Pixel-level screenshot comparison against a baseline |
| [`cross-browser-tester`](./antigravity/agents/cross-browser-tester.md) | `cross-browser-tester` | Runs a verified scenario across the real browser/device support matrix |
| [`mobile-app-tester`](./antigravity/agents/mobile-app-tester.md) | `mobile-app-tester` | Drives a real native iOS/Android app (Appium) |
| [`localization-tester`](./antigravity/agents/localization-tester.md) | `localization-tester` | Checks i18n/l10n rendering, layout, and formatting per locale |
| [`test-automation-engineer`](./antigravity/agents/test-automation-engineer.md) | `test-automation-engineer` | Writes lasting automated tests into the project's suite |
| [`test-data-engineer`](./antigravity/agents/test-data-engineer.md) | `test-data-engineer` | Realistic/reproducible fixtures, and safe prod-to-test data anonymization |
| [`data-migration-tester`](./antigravity/agents/data-migration-tester.md) | `data-migration-tester` | Verifies a migration/ETL job for real data integrity |
| [`coverage-analyst`](./antigravity/agents/coverage-analyst.md) | `coverage-analyst` | Finds which specific undertested code paths actually matter |
| [`api-tester`](./antigravity/agents/api-tester.md) | `api-tester` | Tests REST/GraphQL endpoints against their real contract |
| [`contract-tester`](./antigravity/agents/contract-tester.md) | `contract-tester` | Verifies a provider against every real consumer's contract (Pact) |
| [`accessibility-auditor`](./antigravity/agents/accessibility-auditor.md) | `accessibility-auditor` | WCAG audit via automated scanning (axe) |
| [`performance-tester`](./antigravity/agents/performance-tester.md) | `performance-tester` | Load/stress testing and performance-budget checks with real measurements |
| [`chaos-resilience-tester`](./antigravity/agents/chaos-resilience-tester.md) | `chaos-resilience-tester` | Real fault injection to verify graceful degradation (highest blast-radius role) |
| [`bug-triage-analyst`](./antigravity/agents/bug-triage-analyst.md) | `bug-triage-analyst` | Reproduces, minimizes, and severity-rates a bug report |
| [`flaky-test-investigator`](./antigravity/agents/flaky-test-investigator.md) | `flaky-test-investigator` | Tells apart a real flake from a real intermittent bug |
| [`test-case-writer`](./antigravity/skills/test-case-writer/SKILL.md) | `test-case-writer` (skill) | Generate a test case matrix from a spec |
| [`bug-report-template`](./antigravity/skills/bug-report-template/SKILL.md) | `bug-report-template` (skill) | Format a reproduced bug consistently |
| [`release-smoke-checklist`](./antigravity/skills/release-smoke-checklist/SKILL.md) | `release-smoke-checklist` (skill) | Fast pre-release smoke suite ending in a go/no-go input |
| [`post-deploy-smoke-check`](./antigravity/skills/post-deploy-smoke-check/SKILL.md) | `post-deploy-smoke-check` (skill) | Fast check against real production right after a deploy |
| [`playwright-mcp`](./antigravity/mcp/playwright-mcp.md) | `playwright-mcp` (mcp) | Direct structured browser control |
| [`issue-tracker-mcp`](./antigravity/mcp/issue-tracker-mcp.md) | `issue-tracker-mcp` (mcp) | File bugs directly into Jira/Trello/Notion/similar |
| [`test-management-mcp`](./antigravity/mcp/test-management-mcp.md) | `test-management-mcp` (mcp) | Sync test cases/results into TestRail/Xray/Zephyr/Qase/similar |
| [`pre-commit-test-gate`](./antigravity/hooks/pre-commit-test-gate.md) | `pre-commit-test-gate` (hook) | Blocks `git commit` until tests pass — re-implemented for Antigravity's Decide-hook JSON contract |

## `~ ❯ ls`

| Path | For |
|---|---|
| [`claude/agents/`](./claude/agents) | Claude Code subagent definitions |
| [`claude/skills/`](./claude/skills) | Reusable Claude Skills |
| [`claude/mcp/`](./claude/mcp) | MCP server configs |
| [`claude/hooks/`](./claude/hooks) | Claude Code hook configs |
| [`codex/agents-md/`](./codex/agents-md) | `AGENTS.md` templates |
| [`codex/prompts/`](./codex/prompts) | Standalone Codex CLI / custom-instruction prompts |
| [`antigravity/agents/`](./antigravity/agents) | Antigravity custom subagent definitions |
| [`antigravity/skills/`](./antigravity/skills) | Antigravity Agent Skills |
| [`antigravity/mcp/`](./antigravity/mcp) | MCP server configs (Antigravity's `mcp_config.json` shape) |
| [`antigravity/hooks/`](./antigravity/hooks) | Antigravity `hooks.json` configs |

Each item follows the format in [`../../TEMPLATE.md`](../../TEMPLATE.md) and must pass [`../../scripts/validate.py`](../../scripts/validate.py). Install a Claude/Codex-writable item with `python3 scripts/install.py <path>` — see the root [`README.md`](../../README.md#-❯-man-install).
