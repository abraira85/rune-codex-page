---
name: github-mcp
status: experimental
context: "Initial experimental version."
description: "Provides direct API integration with GitHub to inspect repositories, manage pull requests, and review issues."
---

# Github Mcp

Provides direct API integration with GitHub to inspect repositories, manage pull requests, and review issues.

## Configuration

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_PAT"
      }
    }
  }
}
```
