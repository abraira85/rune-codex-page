# Changelog

All notable changes to this project are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project follows [Semantic Versioning](https://semver.org/) — see
[`CONTRIBUTING.md`](./CONTRIBUTING.md#versioning) for what MAJOR/MINOR/PATCH
mean for a repo of prompts rather than code.

## [Unreleased]

### Added

- Initial project scaffold: `catalog/<area>/<tool>/<type>/` — seven
  areas (engineering, database, devops, security, data-ai, business, qa),
  each with `claude/` (agents, skills, mcp, hooks) and `codex/`
  (agents-md, prompts)
- Contribution workflow: issue template, PR template, front-matter
  validator, CI (`validate.yml`)
- Governance docs: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`,
  `CONTRIBUTORS.md`
- MIT license
- First real catalog items: a `qa/` team of 6 Claude Code subagents
  (qa-lead, functional-tester, browser-automation-tester,
  test-automation-engineer, api-tester, bug-triage-analyst) and 2 Skills
  (test-case-writer, bug-report-template) — all `experimental` until run
  against a real project
- `scripts/install.py` — extracts an item's real payload and writes (or
  prints, for MCP/hooks/prompts) it in the shape the target tool expects
