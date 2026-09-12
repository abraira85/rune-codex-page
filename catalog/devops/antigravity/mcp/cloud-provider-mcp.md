---
name: cloud-provider-mcp
status: experimental
context: "Initial experimental version."
description: "Query real infra state from AWS/GCP/Azure."
---

# Cloud Provider Mcp

Query real infra state from AWS/GCP/Azure.

## Configuration

```json
{
  "mcpServers": {
    "aws-cli": {
      "command": "npx",
      "args": ["-y", "@aws/mcp-server-cli", "--profile", "production"]
    }
  }
}
```
