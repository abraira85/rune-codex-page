---
name: notion-mcp
status: experimental
context: "Initial experimental version."
description: "Integrates with Notion to search documentation, read databases, and update product requirement pages."
---

# Notion Mcp

Integrates with Notion to search documentation, read databases, and update product requirement pages.

## Configuration

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_KEY": "secret_YOUR_NOTION_API_KEY"
      }
    }
  }
}
```
