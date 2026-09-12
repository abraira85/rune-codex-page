---
name: hubspot-mcp
status: experimental
context: "Enterprise MCP server configuration."
description: "Provides direct integration with HubSpot CRM to search contacts, inspect deals, and manage sales pipelines."
---

# Hubspot Mcp

Provides direct integration with HubSpot CRM to search contacts, inspect deals, and manage sales pipelines.

## Configuration

```json
{
  "mcpServers": {
    "hubspot": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-hubspot"],
      "env": {
        "HUBSPOT_ACCESS_TOKEN": "YOUR_HUBSPOT_PRIVATE_APP_TOKEN"
      }
    }
  }
}
```
