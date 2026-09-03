---
name: vcs-review-mcp
status: experimental
context: "Authored for rune-codex-page's engineering team — not yet used against a real GitHub/GitLab PR. Move to production once it's actually posted a review that stuck."
description: Wires a GitHub/GitLab MCP server into Claude so code-reviewer, api-design-reviewer, and dependency-reviewer can post review comments directly on the real PR/MR instead of only returning text.
---

# VCS Review MCP

Gives Claude direct, structured access to the actual pull/merge request
(read the diff with full PR context, post inline comments on specific
lines, submit a review with an overall verdict) through a GitHub/GitLab
MCP server, instead of a human copy-pasting `code-reviewer`'s findings
into the PR by hand. Pairs directly with `code-reviewer`,
`api-design-reviewer`, and `dependency-reviewer` in `../agents/` — once
configured, "review this PR" can end with the review actually posted,
not just printed.

## Prompt / instructions

GitHub — official GitHub MCP server (hosted remote server, or a local
binary/Docker image; check current docs for the exact install path since
this has moved around):

```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

GitLab — check for GitLab's own current official MCP offering first (the
GitLab Duo ecosystem has been adding MCP support); if unavailable or
unclear, a community MCP server for the GitLab API is the fallback --
verify it's maintained and read its source before granting it write
access to real merge requests:

```json
{
  "mcpServers": {
    "gitlab": {
      "command": "npx",
      "args": ["-y", "<community-gitlab-mcp-package>"],
      "env": {
        "GITLAB_PERSONAL_ACCESS_TOKEN": "<token>",
        "GITLAB_API_URL": "<https://gitlab.example.com/api/v4>"
      }
    }
  }
}
```

## Notes

- Exact server URLs, package names, and auth flows change -- this file
  captures the shape as of when it was written, not a guarantee. Check
  the vendor's current MCP docs before wiring this into a real project.
- This config block goes in your MCP client's config file (`.mcp.json`
  for Claude Code). `scripts/install.py` intentionally does not write
  this for you -- merge it by hand so you don't clobber other servers
  already configured there.
- Posting a review is a real, visible action on a shared PR -- a review
  agent using this MCP should state what it's about to post and get
  confirmation before submitting, the same way any other
  visible-to-others action gets confirmed first. Don't wire this up to
  auto-submit reviews without a human in the loop unless that's a
  deliberate, explicit setup choice.
- If no VCS MCP is configured, `code-reviewer` and friends still produce
  the same findings as plain text -- posting them is an addition, not a
  requirement.
- Never invent which PR/MR to review or post to. If it isn't already
  specified (a URL, a branch, "the current PR"), ask rather than guessing.
