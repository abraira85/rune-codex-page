---
name: sast-tool-mcp
status: experimental
context: "Initial experimental version."
description: "Static application security testing (SAST) and vulnerability databases."
---

# Sast Tool Mcp

Static application security testing (SAST) and vulnerability databases.

## Configuration

```json
{
  "mcpServers": {
    "sast-scanner": {
      "command": "npx",
      "args": ["-y", "@semgrep/mcp-server", "--workspace", "/path/to/repo"]
    }
  }
}
```
