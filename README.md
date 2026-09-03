# rune codex page

[![validate](https://github.com/abraira85/rune-codex-page/actions/workflows/validate.yml/badge.svg)](https://github.com/abraira85/rune-codex-page/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-38BDF8.svg)](./CONTRIBUTING.md)
[![Contributor Covenant](https://img.shields.io/badge/code_of_conduct-Contributor_Covenant-8B5CF6.svg)](./CODE_OF_CONDUCT.md)

> Production-tested prompts, roles and configs for **Claude** and **Codex** — private by default, public when ready.

Everything here has actually been used somewhere real. Every item is tagged `production` or `experimental` — nothing ships just to pad the count.

## `~ ❯ ls`

| Directory | For | Contains |
|---|---|---|
| [`claude/`](./claude) | Claude & Claude Code | agents, skills, MCP configs, hooks |
| [`codex/`](./codex) | OpenAI Codex, Codex CLI, Copilot-style agents | `AGENTS.md` templates, standalone prompts |

## `~ ❯ cat CONVENTIONS.md`

Every item carries the same front-matter:

```yaml
---
name: short-identifier
status: production | experimental
context: "where and how it's actually used"
---
```

- **`production`** — running somewhere real, right now.
- **`experimental`** — still being tested, not yet trusted.

Full format in [`TEMPLATE.md`](./TEMPLATE.md). Every PR is checked automatically by [`scripts/validate.py`](./scripts/validate.py) in CI — see the badge above.

## `~ ❯ man contributing`

Contributions are welcome — this isn't a solo drop, it's meant to grow. Start with [`CONTRIBUTING.md`](./CONTRIBUTING.md) for the workflow, [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md) for how we treat each other, and [`SECURITY.md`](./SECURITY.md) if what you found is a security issue rather than a bug. Everyone who lands an item gets listed in [`CONTRIBUTORS.md`](./CONTRIBUTORS.md).

Releases follow [Semantic Versioning](https://semver.org/) and are tracked in [`CHANGELOG.md`](./CHANGELOG.md).

## `~ ❯ roadmap`

- [ ] First real items in `claude/` and `codex/`
- [ ] A generated `index.json` so the catalog is machine-readable
- [ ] Tagged `v0.1.0` once there's enough here to call a first release

## `~ ❯ whoami`

Built by [Rober de Ávila Abraira](https://github.com/abraira85) — [outboss.io](https://outboss.io)
