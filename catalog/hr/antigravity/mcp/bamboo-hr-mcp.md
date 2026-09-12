---
name: bamboo-hr-mcp
status: experimental
context: "Initial experimental version."
description: "Context provider for the company org chart and employee directory."
---

# Bamboo Hr Mcp

Context provider for the company org chart and employee directory.

## Configuration

```json
{
  "mcpServers": {
    "bamboohr": {
      "command": "npx",
      "args": ["-y", "@bamboohr/mcp-server", "--api-key", "YOUR_API_KEY", "--subdomain", "YOUR_COMPANY"]
    }
  }
}
```
