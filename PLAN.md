# Catalog expansion plan

Working plan for what could still go into this catalog — every area, the
roles/skills/MCP/hooks proposed for each, and what's actually built vs
still just an idea. This is a planning doc, not a commitment: nothing
here is `production` until it's real content under `catalog/` that's
passed `scripts/validate.py`.

Legend: ✅ built · 🔲 proposed, not built

---

## `qa/` — largely complete (19 agents/prompts, 4 skills, 3 MCP, 1 hook)

✅ Built, all three tool tracks (Claude / Codex / Antigravity) unless noted:

- **Strategy/orchestration**: `qa-lead`
- **Functional/exploratory**: `functional-tester`, `exploratory-tester` (SBTM)
- **Browser/UI**: `browser-automation-tester`, `visual-regression-tester`,
  `cross-browser-tester`
- **Mobile**: `mobile-app-tester`
- **i18n**: `localization-tester`
- **Automation & data**: `test-automation-engineer`, `test-data-engineer`,
  `data-migration-tester`, `coverage-analyst`
- **API/contracts**: `api-tester`, `contract-tester`
- **Non-functional**: `accessibility-auditor`, `performance-tester`,
  `chaos-resilience-tester`
- **Bugs**: `bug-triage-analyst`, `flaky-test-investigator`
- **Skills**: `test-case-writer`, `bug-report-template`,
  `release-smoke-checklist`, `post-deploy-smoke-check`
- **MCP**: `playwright-mcp`, `issue-tracker-mcp`, `test-management-mcp`
  (speculative — verify server availability)
- **Hook**: `pre-commit-test-gate`

🔲 One remaining gap:

- **`white-box-test-designer`** — designs test cases from the code's
  actual internal structure/branches (as opposed to `functional-tester`,
  which derives cases from a spec) and can run mutation testing to
  measure whether the existing suite would actually catch a real
  regression, not just whether it hits every line. `coverage-analyst`
  finds *where* coverage is thin; this role would be the one that
  designs the case that closes a structurally-identified gap and
  verifies the suite's actual fault-detection strength.

---

## `engineering/` — started (code-review team only, 3 of ~15 proposed roles)

✅ Built:

- `code-reviewer`, `api-design-reviewer`, `dependency-reviewer`
- Skill: `code-review-comment`
- MCP: `vcs-review-mcp`

🔲 Proposed roles — split into "plan/build" and "understand/maintain":

**Plan & build:**
- **`tech-lead`** — orchestrator, mirrors `qa-lead`: scopes a feature,
  decides technical approach and build-vs-buy calls, delegates to the
  roles below. Natural entry point if this area grows a real team.
- **`frontend-architect`** — component architecture, state-management
  patterns, design-system consistency for a UI codebase.
- **`backend-architect`** — service boundaries and system-level API
  design *before* code exists — distinct from `api-design-reviewer`,
  which reviews an interface change that's already in a diff.
- **`build-system-engineer`** — bundler/build-tool config, monorepo
  build graphs, build-time regressions.
- **`api-client-generator`** — generates a typed SDK/client from a real
  schema (OpenAPI/GraphQL), not hand-written and prone to drift.

**Understand & fix:**
- **`debugging-specialist`** — given a bug/failure, finds the actual
  root cause in the code. Distinct from `qa/bug-triage-analyst`, which
  reproduces and severity-rates but doesn't diagnose the code-level
  cause. Most natural next role — direct complement to `code-reviewer`.
- **`refactoring-specialist`** — proactively restructures code without
  changing behavior; needs a strong "verify behavior unchanged"
  discipline (run the existing suite before/after, flag un-tested code
  as higher-risk to refactor rather than proceeding blind).
- **`legacy-code-modernizer`** — strangler-fig-style modernization of
  old, undocumented code specifically — distinct from general
  refactoring in that the starting point is usually "nobody fully
  understands this anymore," not "this works but could be cleaner."
- **`performance-optimizer`** — code-level: algorithmic complexity,
  query patterns, hot-path profiling. Distinct from
  `qa/performance-tester`, which load-tests a *running* service rather
  than reading/profiling code.
- **`migration-upgrade-specialist`** — framework/language major-version
  upgrades (React 17→18, a breaking framework release). Distinct from
  `qa/data-migration-tester`, which is data integrity, not code/
  dependency upgrades.
- **`technical-debt-tracker`** — systematically catalogs and prioritizes
  tech debt across a codebase, not just what one PR touches.

**Explain & maintain:**
- **`documentation-writer`** — writes/maintains README, API docs,
  docstrings, migration guides. `code-reviewer` only *checks* whether
  docs were updated; this role writes them.
- **`codebase-onboarding-guide`** — generates a real tour/onboarding doc
  for an unfamiliar codebase (entry points, key modules, where things
  live), for a new engineer or a fresh agent session.
- **`git-workflow-specialist`** — commit-message quality, branch
  strategy, and merge-conflict-resolution assistance.

🔲 Proposed skills:

- **`feature-scoping-template`** — breaks a feature request into a
  technical plan (approach, affected areas, risks, rollout). Pairs with
  `tech-lead`.
- **`adr-writer`** — Architecture Decision Record template, for *why* a
  decision was made, not just what.
- **`onboarding-doc-template`** — consistent structure for
  `codebase-onboarding-guide`'s output.
- **`tech-debt-ticket-template`** — consistent write-up for a tracked
  tech-debt item (impact, effort, risk of not doing it).

🔲 Proposed MCP:

- A code-search/navigation MCP (Sourcegraph-style) for large codebases
  — useful to `debugging-specialist`, `codebase-onboarding-guide`, and
  `code-reviewer` alike once a codebase is too big for `grep`/`glob`
  alone to be efficient.

---

## `security/` — empty, proposed (~12 roles)

The natural next area — `code-reviewer` and `bug-triage-analyst` (qa/)
both explicitly punt deep security concerns here rather than duplicating
them.

🔲 Proposed roles:

- **`security-reviewer`** — the deep counterpart to `code-reviewer`'s
  security *sanity check*: real SAST-style review of a diff (injection,
  auth/authz, crypto misuse, OWASP Top 10 classes), ideally backed by a
  real static-analysis tool (Semgrep or similar). Natural first role —
  closes the loop `code-reviewer` already points at.
- **`threat-modeler`** — design-time analysis (STRIDE or similar) before
  code exists, for a new feature/service with a meaningful trust
  boundary.
- **`penetration-tester`** — active, authorized exploitation testing
  against a real running app/environment. Needs the same safety-gating
  discipline as `qa/chaos-resilience-tester`: explicit scope, non-prod
  by default, confirmed authorization before anything destructive.
- **`authentication-reviewer`** — deep review of auth/authz flows
  specifically (SSO, OAuth/OIDC, session management, MFA) — narrow and
  high-stakes enough to deserve its own role rather than being one bullet
  inside `security-reviewer`.
- **`cryptography-reviewer`** — key management and algorithm-choice
  review (custom crypto, weak algorithms, improper IV/nonce reuse) —
  same reasoning as `authentication-reviewer`: narrow, high-stakes,
  easy to get subtly wrong.
- **`secrets-auditor`** — a *deep*, whole-repo/whole-history scan for
  leaked credentials (git history, config files, container images) —
  distinct from `code-reviewer`'s lightweight per-diff sanity check.
- **`dependency-vulnerability-auditor`** — periodic, whole-tree SCA scan
  with exploitability assessment. Distinct from
  `engineering/dependency-reviewer`, which is a lightweight per-PR check
  on *new* dependencies only.
- **`container-security-scanner`** — Docker/Kubernetes image
  vulnerability and misconfiguration scanning.
- **`iac-security-reviewer`** — security misconfiguration in
  Terraform/CloudFormation/Kubernetes manifests (public buckets, overly
  broad IAM, missing network policies). Sits at the security/devops
  boundary; cross-link from `devops/iac-reviewer`, which reviews the
  same files for correctness/cost instead.
- **`privacy-reviewer`** — data-privacy-impact review: PII handling,
  data minimization, retention -- GDPR/CCPA-adjacent, distinct from a
  full legal compliance mapping.
- **`compliance-auditor`** — maps real controls to a framework
  (SOC2/PCI/HIPAA) and gathers evidence, rather than asserting
  compliance from a checklist read once.
- **`security-incident-responder`** — breach-specific incident response
  (containment, forensics, disclosure timeline) — distinct from
  `devops/incident-responder`'s general production-incident scope.

🔲 Proposed skills:

- **`vulnerability-report-template`** — consistent CVE/finding write-up
  (severity via CVSS or similar, exploitability, remediation), parallel
  to `qa/bug-report-template`.
- **`threat-model-template`** — consistent STRIDE-style write-up, pairs
  with `threat-modeler`.

🔲 Proposed MCP:

- A SAST tool MCP (e.g. Semgrep) and/or a vulnerability-database MCP
  (OSV, NVD) so `security-reviewer`/`dependency-vulnerability-auditor`
  query real, current data instead of relying on training-data
  knowledge of CVEs, which goes stale immediately.

---

## `devops/` — empty, proposed (~10 roles)

🔲 Proposed roles:

- **`release-manager`** — orchestrates an actual deployment and owns the
  rollback decision. Connects directly to `qa/release-smoke-checklist`
  and `qa/post-deploy-smoke-check`, which currently have no
  deployment-side counterpart actually triggering/monitoring the deploy.
- **`iac-reviewer`** — Terraform/CloudFormation/Pulumi review for
  correctness and cost, not security (that's `security/
  iac-security-reviewer` — the two should cross-reference each other).
- **`ci-pipeline-engineer`** — writes/maintains CI/CD pipeline configs,
  including making sure a pipeline change doesn't silently skip a
  required check.
- **`kubernetes-specialist`** — cluster config review: resource
  requests/limits, autoscaling policy, pod disruption budgets.
- **`observability-engineer`** — sets up/reviews logging, metrics, and
  tracing coverage, and whether alerting actually fires on the failure
  modes that matter.
- **`incident-responder`** — general production incident response
  (not security-breach-specific): triage, mitigation, driving toward
  resolution during an active incident.
- **`disaster-recovery-planner`** — backup/restore strategy and DR-drill
  design, verified by actually running a drill, not just documenting one.
- **`secrets-management-specialist`** — vault/secrets-rotation setup
  (the execution side) — distinct from `security/secrets-auditor`,
  which finds leaks after the fact.
- **`feature-flag-manager`** — rollout/kill-switch strategy and
  execution for a staged release.
- **`cost-optimizer`** — analyzes real cloud billing/usage data for
  waste (idle resources, oversized instances) rather than guessing.

🔲 Proposed skills:

- **`postmortem-template`** — blameless incident postmortem format
  (timeline, root cause, action items).
- **`runbook-template`** — consistent on-call runbook format for a
  specific failure mode.
- **`dr-drill-checklist`** — pairs with `disaster-recovery-planner`:
  what a real DR drill needs to verify to count as done.

🔲 Proposed MCP:

- A cloud provider MCP (AWS/GCP/Azure) for querying real infra state
  rather than guessing from IaC files alone.
- A monitoring/observability MCP (Datadog, Grafana, etc.) — also
  directly useful to `qa/post-deploy-smoke-check`, which already wants
  one and doesn't have it.

---

## `database/` — empty, proposed (~7 roles)

🔲 Proposed roles:

- **`schema-designer`** — data modeling for a new feature
  (normalization, indexing strategy, constraints decided up front).
- **`query-optimizer`** — analyzes slow queries against real `EXPLAIN`
  output, not guessed query plans.
- **`migration-author`** — writes an actual migration script safely
  (backward-compatible, reversible where possible). The "doing"
  counterpart to `qa/data-migration-tester`, which verifies a migration
  someone already wrote.
- **`database-reviewer`** — reviews a schema-change PR specifically
  (index strategy, migration safety, normalization) — the DB-specific
  sibling to `engineering/code-reviewer`.
- **`capacity-planner`** — sharding/partitioning strategy for a dataset
  approaching real scale limits.
- **`backup-recovery-specialist`** — backup strategy and *tested*
  restore procedures, specific to database recovery (as opposed to
  `devops/disaster-recovery-planner`'s broader infra scope).
- **`replication-specialist`** — read-replica setup and replication-lag
  troubleshooting.

🔲 Proposed skill:

- **`migration-safety-checklist`** — backward-compatibility and
  reversibility checklist, pairs with `migration-author` and
  `database-reviewer`.

🔲 Proposed MCP:

- A database MCP (Postgres, MySQL, etc.) for running real `EXPLAIN`
  plans and schema introspection instead of reasoning about SQL blind.

---

## `data-ai/` — empty, proposed (~8 roles)

🔲 Proposed roles:

- **`prompt-engineer`** — designs and iterates on prompts for an
  LLM-backed feature, with actual eval runs, not just "this reads well."
- **`rag-pipeline-reviewer`** — reviews chunking/embedding/retrieval
  quality for a RAG system against real retrieval results.
- **`ml-model-evaluator`** — offline evaluation against real metrics/
  held-out data, not impressions from a few manual prompts.
- **`data-pipeline-reviewer`** — ongoing ETL/data-pipeline correctness
  review, distinct from `qa/data-migration-tester`'s one-time migration
  focus.
- **`fine-tuning-specialist`** — dataset curation and the fine-tuning
  workflow itself (not just evaluating the result after).
- **`ai-safety-reviewer`** — jailbreak/prompt-injection resistance
  testing for an LLM-backed feature — cross-links to `security/`, but
  the specific failure mode (a model doing something its prompt told it
  not to) is distinct enough to live here.
- **`model-monitoring-specialist`** — production ML drift detection
  (data drift, prediction drift) using real monitoring signals.
- **`data-quality-auditor`** — validation/quality checks on a dataset
  before it's used for training or analytics (nulls, duplicates, label
  noise, distribution shift from what's expected).

🔲 Proposed skill:

- **`eval-dataset-template`** — consistent format for a golden eval
  dataset (input, expected output, why it's a meaningful case).

🔲 Proposed MCP:

- A vector-DB MCP and/or an LLM-observability MCP (LangSmith-style) for
  real trace/eval data instead of guessing at model behavior.

---

## `business/` — empty, proposed (~6 roles)

Lowest natural fit for a coding-agent catalog — these roles lean on
Read/Write more than Bash, and the "verify against something real"
discipline this repo prizes is harder to apply (there's no test suite
for a product spec). Still worth having, just a different flavor.

🔲 Proposed roles:

- **`product-spec-writer`** — turns a rough idea into a structured PRD
  with explicit open questions flagged, not invented answers.
- **`okr-planner`** — structures goals/key-results with real, checkable
  success criteria.
- **`stakeholder-comms-writer`** — status updates / exec summaries from
  real project state (commits, tickets), not a vague narrative.
- **`competitive-analysis-writer`** — structured comparison against
  named competitors from real, sourced information, not assumption.
- **`user-research-synthesizer`** — turns raw interview notes/feedback
  into structured themes/insights, sourced back to the original quotes.
- **`pricing-analyst`** — pricing-model analysis grounded in real
  cost/usage data rather than a gut-feel number.

---

## Cross-cutting / infra, not tied to one area

- **Antigravity rollout** — only `qa/` and `engineering/` have an
  `antigravity/` tool track so far; every area above would need it too
  once/if it gets built out, following the same pattern.
- **Housekeeping** — stale roadmap line in the root `README.md`
  ("qa/ team: 6 agents, 2 skills"), stale `assets/hero.svg` alt text
  (mentions only `claude/`/`codex/`, not `antigravity/`).
- **`index.json`** — a generated, machine-readable catalog index
  (already on the README roadmap, unchecked).
- **`v0.1.0` tag** — once there's enough here to call a first release
  (already on the README roadmap, unchecked).

## Possible future areas (not in the current 7, not scoped here)

Raised for completeness, not proposed for immediate build — adding a
whole new area is a bigger decision than adding a role to an existing
one, and each of these would dilute focus if built shallowly:

- **Design/UX** — wireframing, user-flow design, design-system authoring.
  Deliberately excluded from `qa/` (usability testing needs real humans),
  but the *design* side (as opposed to testing it) is a real, distinct
  discipline this catalog doesn't touch at all yet.
- **Content/technical writing for external audiences** — blog posts,
  marketing copy, external-facing docs. Distinct from `engineering/
  documentation-writer`, which is internal/developer-facing.
- **Legal/compliance (broader than `security/compliance-auditor`)** —
  contract review, terms of service, general regulatory questions
  outside the security-control-mapping scope already proposed.

---

## Scale, if all of the above gets built

At full 3-tool-track parity (Claude + Codex + Antigravity, matching the
"do it completely" rule established in `qa/` and `engineering/`):

| | Roles | Skills | MCP |
|---|---|---|---|
| `qa/` remaining | 1 | 0 | 0 |
| `engineering/` remaining | 12 | 4 | 1 |
| `security/` | 12 | 2 | 1 |
| `devops/` | 10 | 3 | 2 |
| `database/` | 7 | 1 | 1 |
| `data-ai/` | 8 | 1 | 2 |
| `business/` | 6 | 0 | 0 |
| **Total** | **56** | **11** | **7** |

56 roles × 3 files + 11 skills × 2 files + 7 MCP × 2 files ≈ **210 new
files**, on top of the ~130 already built. This is a multi-session,
probably multi-week effort at the depth/rigor this repo has held so far
— not something to batch into one sitting.

## Suggested build order (opinionated)

1. Finish `engineering/`: `debugging-specialist` next (direct complement
   to `code-reviewer`), then `tech-lead`, `refactoring-specialist`,
   `documentation-writer` — the four with the clearest immediate use.
2. `security/`: `security-reviewer` first (closes the loop `code-reviewer`
   and `bug-triage-analyst` both already point at), then
   `secrets-auditor` and `dependency-vulnerability-auditor`.
3. `devops/`: `release-manager` first (closes the loop `qa/
   release-smoke-checklist`/`post-deploy-smoke-check` already point at),
   then `iac-reviewer` and `incident-responder`.
4. `database/`, `data-ai/`, `business/` — lower urgency, no existing
   loop pointing at them yet; pick based on what's actually needed for
   real work rather than completeness for its own sake.
5. Housekeeping and infra items whenever there's a natural pause — cheap,
   don't block anything else.
