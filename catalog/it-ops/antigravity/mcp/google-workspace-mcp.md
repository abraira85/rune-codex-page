---
name: google-workspace-mcp
status: experimental
context: "Enterprise MCP server configuration."
description: "Enables IT and operations agents to manage Google Workspace users, groups, and directory records via official APIs."
---

# Google Workspace Mcp

Enables IT and operations agents to manage Google Workspace users, groups, and directory records via official APIs.

## Configuration

```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-workspace"],
      "env": {
        "GOOGLE_WORKSPACE_CREDENTIALS_JSON": "/path/to/service-account.json",
        "GOOGLE_WORKSPACE_ADMIN_EMAIL": "admin@yourcompany.com"
      }
    }
  }
}
```
