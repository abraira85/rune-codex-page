---
name: llm-observability-mcp
status: experimental
context: "Initial experimental version."
description: "LangSmith or similar for real trace/eval data."
---

# Llm Observability Mcp

LangSmith or similar for real trace/eval data.

## Configuration

```json
{
  "mcpServers": {
    "langsmith": {
      "command": "npx",
      "args": ["-y", "@langchain/mcp-server-langsmith", "--api-key", "YOUR_API_KEY"]
    }
  }
}
```
