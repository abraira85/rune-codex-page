---
name: jira-mcp
status: experimental
context: "Enterprise MCP server configuration."
description: "Connects agents to Jira Cloud to read user stories, manage epics, update sprint statuses, and file tickets."
---

# Jira Mcp

Connects agents to Jira Cloud to read user stories, manage epics, update sprint statuses, and file tickets.

## Configuration

```json
{
  "mcpServers": {
    "jira": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-jira"],
      "env": {
        "JIRA_INSTANCE_URL": "https://yourorg.atlassian.net",
        "JIRA_EMAIL": "your-email@company.com",
        "JIRA_API_TOKEN": "YOUR_JIRA_API_TOKEN"
      }
    }
  }
}
```
