---
name: database-mcp
status: experimental
context: "Initial experimental version."
description: "Run real EXPLAIN plans and schema introspection."
---

# Database Mcp

Run real EXPLAIN plans and schema introspection.

## Configuration

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@postgres/mcp-server", "postgresql://user:pass@localhost:5432/db"]
    }
  }
}
```
