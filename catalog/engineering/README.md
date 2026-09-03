# engineering/

General software development — backend, frontend, full-stack. Starts
with a code-review team: `code-reviewer` handles correctness/security-
sanity/tests/readability, and hands off to `api-design-reviewer` and
`dependency-reviewer` for the two things a generalist pass shouldn't try
to cover shallowly. All `experimental`: written for this repo, not yet
run against a real PR — see each file's `context` field.

## Team (Claude)

| Agent | Role |
|---|---|
| [`code-reviewer`](./claude/agents/code-reviewer.md) | Correctness, security sanity, test coverage, readability -- the generalist pass |
| [`api-design-reviewer`](./claude/agents/api-design-reviewer.md) | Breaking-change risk, versioning, and design for public interface changes |
| [`dependency-reviewer`](./claude/agents/dependency-reviewer.md) | Necessity, license, and known vulnerabilities for a dependency change |

| Skill | For |
|---|---|
| [`code-review-comment`](./claude/skills/code-review-comment/SKILL.md) | Format a single finding consistently across all three reviewer roles |

| MCP | For |
|---|---|
| [`vcs-review-mcp`](./claude/mcp/vcs-review-mcp.md) | Post the review directly on the real GitHub/GitLab PR instead of only returning text |

## Team (Codex)

| Item | Claude equivalent | For |
|---|---|---|
| [`code-review`](./codex/prompts/code-review.md) | `code-reviewer` | One-shot: correctness/security-sanity/tests/readability review, folds in the comment-format + MCP-or-REST-API posting fallback |
| [`api-design-review`](./codex/prompts/api-design-review.md) | `api-design-reviewer` | One-shot: breaking-change/versioning/design review for a public interface change |
| [`dependency-review`](./codex/prompts/dependency-review.md) | `dependency-reviewer` | One-shot: necessity/license/vulnerability review for a dependency change |

## Team (Antigravity)

| Item | Claude equivalent | For |
|---|---|---|
| [`code-reviewer`](./antigravity/agents/code-reviewer.md) | `code-reviewer` | Correctness, security sanity, test coverage, readability |
| [`api-design-reviewer`](./antigravity/agents/api-design-reviewer.md) | `api-design-reviewer` | Breaking-change risk, versioning, and design for public interface changes |
| [`dependency-reviewer`](./antigravity/agents/dependency-reviewer.md) | `dependency-reviewer` | Necessity, license, and known vulnerabilities for a dependency change |
| [`code-review-comment`](./antigravity/skills/code-review-comment/SKILL.md) | `code-review-comment` (skill) | Format a single finding consistently |
| [`vcs-review-mcp`](./antigravity/mcp/vcs-review-mcp.md) | `vcs-review-mcp` (mcp) | Post the review directly on the real GitHub/GitLab PR |

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

Each item follows the format in [`../../TEMPLATE.md`](../../TEMPLATE.md) and must pass [`../../scripts/validate.py`](../../scripts/validate.py).
