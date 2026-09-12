# Changelog

All notable changes to this project are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project follows [Semantic Versioning](https://semver.org/) — see
[`CONTRIBUTING.md`](./CONTRIBUTING.md#versioning) for what MAJOR/MINOR/PATCH
mean for a repo of prompts rather than code.

## [0.4.0] - 2026-09-12

### Added
- **Deep Enterprise Expansion (26 New In-Depth Roles)**:
  - **`it-ops/`** (New Department): `it-admin`, `helpdesk-specialist`, `identity-governance-lead` (Zero Trust, PAM, Jamf/InTune compliance, Okta/Google Workspace lifecycle).
  - **`operations/`** (New Department): `revops-architect`, `procurement-manager`, `bizops-analyst` (revenue attribution, SaaS contract negotiation, cross-functional OKRs).
  - **`communications/`** (New Department): `pr-specialist`, `internal-comms-lead`, `crisis-comms-manager` (press releases, executive All-Hands scripts, emergency crisis holding statements).
  - **`sales/`**: `account-executive` (MEDDPICC qualification, business case ROI), `sales-enablement` (competitive battlecards, objection handling), `proposal-writer` (formal RFP/tender responses).
  - **`product/`**: `product-ops` (feature flag governance, feedback taxonomy), `growth-pm` (activation funnels, viral loops, A/B testing), `user-story-author` (epics decomposition, Gherkin acceptance criteria).
  - **`customer-success/`**: `tam-architect` (Technical Account Management, TQBRs, architecture reviews), `implementation-specialist` (onboarding, legacy data migration, go-live checklists).
  - **`marketing/`**: `product-marketing-manager` (PMM positioning, GTM launches), `content-strategist` (full-funnel editorial calendar, whitepapers), `performance-marketer` (Google/LinkedIn Ads, CAC/LTV attribution).
  - **`finance/`**: `fp-and-a-analyst` (rolling 3-statement models, OpEx budgets, variance analysis), `cash-flow-planner` (13-week cash forecasting, FX hedging, payment gateways).
  - **`hr/`**: `compensation-analyst` (Radford/Pave salary bands, equity grants, pay parity), `performance-coach` (360 feedback reviews, PIP plans, manager coaching).
  - **`legal/`**: `contract-negotiator` (commercial redlining, MSA/DPA fallback library), `ip-patent-analyst` (prior art searches, patent disclosures, open source copyleft audit).
- **New Enterprise MCP Servers**:
  - `hubspot-mcp` (`sales`): CRM pipeline inspection and lead lifecycle automation.
  - `jira-mcp` (`product`): Epics, user stories, and sprint tracking in Jira Cloud.
  - `google-workspace-mcp` (`it-ops`): Automated directory management, groups, and identity governance.
- **Frontend Web UI Upgraded**:
  - Added support for 19 areas, color palettes for IT-Ops, Operations, and Communications, and updated counters for 454 catalog items.
- **Catalog Scale Milestone**:
  - Reached **454 total validated catalog items** across **19 areas** and **3 platforms** with 100% strict prompt linter compliance.

## [0.3.0] - 2026-09-12

### Added
- **Interactive Web UI (`docs/`)**: Zero-dependency static explorer ready for GitHub Pages hosting, with instant live search (<5ms), faceted filtering (by platform, area, tool type, status), modal prompt inspect, and one-click copy buttons.
- **Prompt Quality Linter (`scripts/lint_prompts.py`)**: Strict heuristic validation checking prompt length, placeholder detection (`TODO`, `FIXME`), actionability directives, and valid JSON structure inside MCP configurations.
- **New Business Domains**:
  - `sales/`: `sales-engineer`, `sdr-outreach` (across Claude, Codex, Antigravity).
  - `customer-success/`: `support-engineer`, `churn-analyst` (across Claude, Codex, Antigravity).
  - `product/`: `scrum-master`, `product-manager` (across Claude, Codex, Antigravity).
- **Core MCP Servers**:
  - `github-mcp` (Engineering): API integration for PR reviews and repository operations.
  - `slack-mcp` (Business): Workspace communication and incident notification dispatch.
  - `notion-mcp` (Product): Notion database and PRD page synchronization.
- **Catalog Index Sync**: `scripts/generate_index.py` now populates both `catalog/index.json` and `docs/data/index.json` with prompt payloads.
- Reached **370 total validated catalog items** across **16 areas** and **3 platforms**.

## [0.2.0] - 2026-09-12

### Added
- New business areas: `hr/` (`talent-sourcer`, `onboarding-buddy`, `bamboo-hr-mcp`), `finance/` (`expense-auditor`, `burn-rate-analyst`), and `marketing/` (`seo-optimizer`, `social-media-manager`).
- CLI search utility `scripts/rune-search.py` for terminal-based catalog browsing.
- Unit testing suite `scripts/test_install.py` covering installation edge cases and nested code fences.
- Fixed nested markdown fence extraction in `scripts/install.py`.

## [0.1.0] - 2026-09-12

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
- First real catalog items: a `qa/` team of 8 Claude Code subagents
  (qa-lead, functional-tester, browser-automation-tester,
  test-automation-engineer, api-tester, accessibility-auditor,
  performance-tester, bug-triage-analyst), 2 Skills (test-case-writer,
  bug-report-template), an MCP config (playwright-mcp), and a hook
  (pre-commit-test-gate) — all `experimental` until run against a real
  project
- Codex side of the `qa/` team: an `AGENTS.md` testing-conventions
  template plus a standalone prompt mirroring each of the 8 Claude
  agents 1:1 (qa-strategy, test-case-matrix, browser-e2e-check,
  write-automated-test, api-contract-check, accessibility-check,
  performance-check, bug-report)
- `scripts/install.py` — extracts an item's real payload and writes (or
  prints, for MCP/hooks/prompts) it in the shape the target tool expects
- `issue-tracker-mcp` (Claude): wires Jira/Confluence, Notion, Trello, or
  similar issue trackers into Claude via MCP so `bug-triage-analyst` can
  file the ticket directly, with severity-to-priority field mapping;
  `bug-report` (Codex) gets the equivalent capability as a per-task
  MCP-if-available/REST-API-otherwise fallback, since Codex has no `mcp/`
  catalog type
- Three more gaps closed in the `qa/` team, each with a Claude + Codex
  side: `visual-regression-tester` / `visual-regression-check` (pixel
  screenshot comparison against a baseline, complementing
  `browser-automation-tester`'s behavioral checks), `flaky-test-investigator`
  / `flaky-test-check` (tells apart a genuine flake from a real
  intermittent bug, fixes or quarantines with a tracked ticket instead
  of silently retrying), and `release-smoke-checklist` /
  `release-smoke-check` (fast, time-boxed pre-release smoke suite as a
  final gate)
- `test-management-mcp` (Claude, speculative): syncs `test-case-writer`'s
  matrix and execution results into TestRail/Xray/Zephyr/Qase/similar;
  `test-case-matrix` (Codex) gets the same MCP-if-available/REST-API
  fallback
- `qa-lead` updated to route to the three new specialists and to
  `release-smoke-checklist` as a pre-ship gate
- New `antigravity/` catalog tool track (`agents`, `skills`, `mcp`,
  `hooks`), piloted in `qa/` before rolling out to the other 6 areas:
  Google Antigravity turned out to have real persistent subagents
  (`.md` + YAML frontmatter, auto-discovered from `.agents/agents/`) much
  closer to Claude Code's model than to Codex's, so `qa/antigravity/`
  mirrors `qa/claude/` 1:1 — all 10 agents, 3 skills, 3 MCP configs, and
  the hook, re-packaged for Antigravity's frontmatter fields, tool names,
  and config file locations. The hook (`pre-commit-test-gate`) is a real
  re-implementation rather than a config translation, since Antigravity's
  Decide hooks signal allow/deny via a JSON stdout payload instead of
  Claude's exit-code contract
- Infra to support the new tool track: `scripts/validate.py` and
  `scripts/install.py` now handle `antigravity/*`, `TEMPLATE.md` notes
  its frontmatter differences, and the root/`catalog/` READMEs document
  the pilot-rollout status
- Full QA-specialty coverage: 7 more roles closing the remaining gaps,
  each with a Claude agent/skill, a Codex prompt, and an Antigravity
  port — `contract-tester` / `contract-check` (consumer-driven contract
  testing via Pact, catching cross-service breaks `api-tester` can't
  see), `localization-tester` / `localization-check` (i18n/l10n
  rendering, layout, and locale-formatting correctness, not translation
  quality), `cross-browser-tester` / `cross-browser-check` (runs a
  verified scenario across the real browser/device support matrix),
  `mobile-app-tester` / `mobile-app-check` (native iOS/Android via
  Appium, distinct from mobile web), `test-data-engineer` /
  `test-data-setup` (realistic/reproducible fixtures, and mandatory PII
  anonymization before any prod data reaches a test environment),
  `coverage-analyst` / `coverage-analysis` (prioritizes undertested code
  by what actually matters, not raw percentage), and
  `chaos-resilience-tester` / `chaos-resilience-check` (real fault
  injection to verify graceful degradation -- the highest blast-radius
  role in the team, with hard safety rules: non-prod by default, stated
  blast radius and rollback plan before injecting, one fault at a time).
  Plus `post-deploy-smoke-check` (Claude skill + Codex prompt +
  Antigravity skill), the production-side complement to
  `release-smoke-checklist`: a fast synthetic check against real prod
  right after a deploy, distinct from the pre-ship gate
- Final two QA gaps closed, same three-tool-track treatment:
  `exploratory-tester` / `exploratory-session` (session-based, charter-
  driven exploratory testing -- no pre-written cases, meant to catch the
  unknown-unknowns spec-derived testing misses) and
  `data-migration-tester` / `data-migration-check` (verifies a migration
  or ETL job for real data integrity -- row counts, sampled field-level
  diffs, referential integrity, idempotency, and rollback -- since "the
  script didn't error" isn't evidence the data survived correctly)
- `qa-lead` (all three tool tracks) and `qa-strategy` (Codex) updated to
  route to all nine new specialists and both smoke-check skills. QA team
  is now 19 agents/prompts, 4 skills, 3 MCP configs, and 1 hook, across
  Claude, Codex, and Antigravity
- First item in `engineering/`, across all three tool tracks:
  `code-reviewer` (Claude agent + Antigravity port) / `code-review`
  (Codex prompt) -- real diff review (correctness, security sanity, test
  coverage, readability) with severity-tagged findings (Blocking /
  Should-fix / Nit), scoped to what actually changed. Deep security
  review is explicitly deferred to a future `security/` role, not
  duplicated here. `engineering/` also gets its `antigravity/` scaffold
  (previously only `qa/` had one) and drops the now-redundant
  `.gitkeep` placeholders in the folders that got real content
- `engineering/` code-review team rounded out, all three tool tracks:
  `code-reviewer` deepened significantly (diff-size sanity, error
  handling/observability, AI-generated-code smells, documentation
  checks, and hand-offs to the two new specialist roles instead of
  covering their ground shallowly) and two new roles added --
  `api-design-reviewer` / `api-design-review` (breaking-change risk,
  versioning, and interface design for public API/schema changes) and
  `dependency-reviewer` / `dependency-review` (necessity, license, and
  known vulnerabilities for a dependency change, via real audit tooling)
- `code-review-comment` (Claude + Antigravity skill, folded into the
  Codex prompt): consistent finding format -- location, what's wrong,
  why it matters, severity, suggestion -- shared across all three
  reviewer roles
- `vcs-review-mcp` (Claude + Antigravity): posts a review directly on a
  real GitHub/GitLab PR/MR instead of only returning text; `code-review`
  (Codex) gets the same MCP-if-available/REST-API-otherwise fallback
