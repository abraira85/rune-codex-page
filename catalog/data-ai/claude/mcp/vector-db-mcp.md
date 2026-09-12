---
name: vector-db-mcp
status: experimental
context: "Initial experimental version."
description: "Query Pinecone, Weaviate, or Qdrant for RAG pipeline review."
---

# Vector Db Mcp

Query Pinecone, Weaviate, or Qdrant for RAG pipeline review.

## Configuration

```json
{
  "mcpServers": {
    "vector-db": {
      "command": "npx",
      "args": ["-y", "@pinecone/mcp-server", "--api-key", "YOUR_API_KEY"]
    }
  }
}
```
