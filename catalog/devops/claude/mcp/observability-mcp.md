---
name: observability-mcp
status: experimental
context: "Initial experimental version."
description: "Datadog, Grafana, or Prometheus integration."
---

# Observability Mcp

Datadog, Grafana, or Prometheus integration.

## Configuration

```json
{
  "mcpServers": {
    "datadog": {
      "command": "npx",
      "args": ["-y", "@datadog/mcp-server", "--api-key", "YOUR_API_KEY", "--app-key", "YOUR_APP_KEY"]
    }
  }
}
```
