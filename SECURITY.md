# Security Policy

This repository contains prompts, agent definitions, MCP configs and hooks —
content that gets fed directly into AI tools with real permissions. Treat
security reports here seriously, even though it's "just markdown."

## What counts as a security issue

- A published item contains a prompt-injection vector, or instructions that
  could cause an agent to take unintended destructive actions
  (e.g. an MCP config or hook that grants broader access than documented)
- Malicious content submitted through a PR that isn't caught by review
- Anything in `scripts/` or `.github/workflows/` that could be abused to run
  arbitrary code in CI

## Reporting

Do **not** open a public issue for security concerns. Email
**rober@outboss.io** with:

- The affected file/path
- What the risk is and how it could be triggered
- A suggested fix, if you have one

You'll get a response within a few days. Confirmed issues are fixed and
credited (unless you'd rather stay anonymous) before any public disclosure.
