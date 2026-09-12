---
name: slack-mcp
status: experimental
context: "Initial experimental version."
description: "Connects agents to Slack workspaces to post notifications, read channel messages, and monitor incidents."
---

# Slack Mcp

Connects agents to Slack workspaces to post notifications, read channel messages, and monitor incidents.

## Configuration

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-YOUR-BOT-TOKEN",
        "SLACK_TEAM_ID": "T012345678"
      }
    }
  }
}
```
