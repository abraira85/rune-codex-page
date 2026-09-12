---
name: code-search-mcp
status: experimental
context: "Initial experimental version."
description: "Sourcegraph-style code search for large codebases."
---

# Code Search Mcp

Sourcegraph-style code search for large codebases.

## Configuration

```json
{
  "mcpServers": {
    "code-search": {
      "command": "npx",
      "args": ["-y", "@sourcegraph/mcp-server", "--url", "YOUR_SOURCEGRAPH_URL", "--token", "YOUR_TOKEN"]
    }
  }
}
```
