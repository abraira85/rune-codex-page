# Contributing

This repo has one rule that matters more than any format: **don't add things that don't work.**

## The bar

Every item is tagged `production` or `experimental` in its front-matter:

- **`production`** — it is running somewhere real, right now. Don't mark something `production` because it worked once in a test.
- **`experimental`** — you're still testing it. That's fine, just be honest about it.

Volume is not a goal here. A repo with five things that actually work is more useful than fifty that might.

## Adding an item

1. Copy [`TEMPLATE.md`](./TEMPLATE.md) into the right folder and rename it to a short, lowercase, hyphenated slug (e.g. `catalog/engineering/claude/agents/api-reviewer.md`).
2. Fill in every front-matter field. `context` should say *where* and *how* — "used in production to review backend PRs before merge," not "useful for reviewing code."
3. Run the validator before opening a PR:
   ```
   pip install -r scripts/requirements.txt
   python3 scripts/validate.py
   ```
4. Open a PR using the checklist that's already in the template.

## Where things go

Items live under `catalog/<area>/<tool>/<type>/`.

**Pick the area first** — what the item is *for*:

| Area | For |
|---|---|
| `engineering` | General software development |
| `database` | Data modeling, SQL, query optimization |
| `devops` | Infrastructure, CI/CD, cloud |
| `security` | Security review, hardening |
| `data-ai` | ML, RAG, data pipelines, LLM ops |
| `business` | Leadership, product, strategy |
| `qa` | Testing, quality assurance |

**Then the tool and type** — this part decides where the file goes once someone copies it into their own project:

| Path | For |
|---|---|
| `claude/agents/` | Claude Code subagent definitions |
| `claude/skills/` | Reusable Claude Skills |
| `claude/mcp/` | MCP server configs |
| `claude/hooks/` | Claude Code hook configs |
| `codex/agents-md/` | `AGENTS.md` templates |
| `codex/prompts/` | Codex CLI / custom-instruction prompts that aren't a full `AGENTS.md` |

If your item doesn't fit any of these, open an issue first — it might be a new area, not a bad fit.

## Versioning

Releases follow [Semantic Versioning](https://semver.org/), adapted for a repo of prompts instead of code:

| Bump | When |
|---|---|
| **MAJOR** | An item is removed or renamed, or the folder structure changes in a way that breaks existing links/references |
| **MINOR** | New item(s) added, or an existing item's category changes |
| **PATCH** | A fix or correction to an existing item that doesn't change what it's for |

Every merge to `main` lands in [`CHANGELOG.md`](./CHANGELOG.md) under `[Unreleased]`. Tagged releases move that section under a version heading.

**Cutting a release** (maintainer only):

1. In `CHANGELOG.md`, rename `## [Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD` and add a fresh empty `## [Unreleased]` above it.
2. Commit, then tag and push: `git tag vX.Y.Z && git push origin vX.Y.Z`.
3. `.github/workflows/release.yml` picks up the tag, pulls that exact section out of `CHANGELOG.md`, and publishes it as the GitHub Release body. If the section is missing, the workflow fails on purpose — fix the changelog and re-tag.

## Reporting problems

Something here doesn't work as documented? Open an issue with the item's path and what you saw. See [`SECURITY.md`](./SECURITY.md) if the problem is a security concern rather than a bug.

## Recognition

Contributors are listed in [`CONTRIBUTORS.md`](./CONTRIBUTORS.md) — add yourself in the same PR as your first item.
