---
name: test-management-mcp
status: experimental
context: "Authored for rune-codex-page's QA team — not yet used against a real TestRail/Xray/Zephyr/Qase project. Speculative on the MCP-availability front specifically -- verify before relying on it."
description: Wires a dedicated test-case-management platform (TestRail, Xray, Zephyr, Qase, or similar) into Claude so test-case-writer's matrix can be synced there and execution results recorded, instead of living only as markdown.
---

# Test Management MCP

The test-case-management counterpart to `issue-tracker-mcp` in this same
folder: that one files *bugs* into Jira/Trello/Notion, this one syncs
*test cases* and their execution results into a dedicated test-management
platform (TestRail, Xray, Zephyr, Qase, or similar) instead of leaving
`test-case-writer`'s matrix as a markdown table nobody re-runs from.

## Prompt / instructions

Unlike Jira and Notion, none of the major test-management platforms
(TestRail, Xray, Zephyr Scale, Qase) had a confirmed **official** MCP
server as of when this was written. Treat any specific package name you
find as unverified until you've checked it against the vendor's current
docs. Two realistic paths, in order of preference:

1. **A maintained community MCP server exists for your platform.** Read
   its source before granting it write access to a real project -- these
   are lower-trust than an official, vendor-published server.

   ```json
   {
     "mcpServers": {
       "test-management": {
         "command": "npx",
         "args": ["-y", "<community-mcp-package-for-your-platform>"],
         "env": {
           "TESTRAIL_URL": "<https://yourorg.testrail.io>",
           "TESTRAIL_USER": "<email>",
           "TESTRAIL_API_KEY": "<key>"
         }
       }
     }
   }
   ```

2. **No trustworthy server exists yet.** All four platforms expose a
   real REST API (TestRail, Xray's Jira/GraphQL API, Zephyr Scale's REST
   API, Qase's REST API). A minimal custom MCP wrapper exposing just
   what this workflow needs is a half-day of work and stays under your
   control:
   - `create_or_update_test_case(section, title, steps, expected)` --
     idempotent on title/external-ID so re-running `test-case-writer`
     doesn't create duplicates every time
   - `record_result(test_case_id, run_id, status, notes)`
   - `get_test_case(id)` -- to check for an existing match before
     creating a new one

## Notes

- This file is more speculative than `playwright-mcp` or
  `issue-tracker-mcp` in this folder -- the MCP ecosystem for
  test-management platforms specifically was young and shifting when
  this was written. Check current state before trusting the JSON above
  as anything more than a shape to expect.
- Field mapping when `test-case-writer` syncs here: each matrix row
  becomes one test case (title, preconditions, steps, expected result);
  the matrix's risk ordering can map to the platform's priority field if
  it has one. Don't invent a section/suite/project to file into -- if
  the target isn't specified, ask.
- Recording execution results (pass/fail per run) is what turns this
  from "test cases live in two places" into an actual regression
  history -- without step 2 (`record_result`), syncing the matrix alone
  just relocates the markdown table.
- As with `issue-tracker-mcp`, this config goes in your MCP client's
  config file (e.g. `.mcp.json`) and `scripts/install.py` does not write
  it for you -- merge it by hand.
