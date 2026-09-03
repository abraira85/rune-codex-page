# catalog/

Every item, organized by **area** first — the thing you actually care about when looking for something — then by tool and type, which decides where the file goes once you copy it.

## `~ ❯ ls`

| Area | For |
|---|---|
| [`engineering/`](./engineering) | General software development |
| [`database/`](./database) | Data modeling, SQL, query optimization, migrations |
| [`devops/`](./devops) | Infrastructure, CI/CD, cloud, deployment |
| [`security/`](./security) | Security review, vulnerability assessment, hardening |
| [`data-ai/`](./data-ai) | ML, RAG, data pipelines, LLM ops |
| [`business/`](./business) | Leadership, product, strategy |
| [`qa/`](./qa) | Testing, quality assurance, functional and automated validation |

Inside each area, the same pattern repeats:

```
<area>/
├── claude/
│   ├── agents/       Claude Code subagent definitions
│   ├── skills/       Reusable Claude Skills
│   ├── mcp/          MCP server configs
│   └── hooks/        Claude Code hook configs
├── codex/
│   ├── agents-md/    AGENTS.md templates
│   └── prompts/      Standalone Codex CLI / custom-instruction prompts
└── antigravity/
    ├── agents/       Google Antigravity custom subagent definitions
    ├── skills/       Antigravity Agent Skills
    ├── mcp/          MCP server configs (.agents/mcp_config.json shape)
    └── hooks/        Antigravity hooks.json configs
```

`antigravity/` is new and rolling out area by area rather than all at
once — check an area's own README for what's actually there before
assuming the full tree exists; `qa/` is the first area with it filled
in.

See [`../TEMPLATE.md`](../TEMPLATE.md) for the item format.
