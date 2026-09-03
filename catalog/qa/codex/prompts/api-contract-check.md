---
name: api-contract-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# API Contract Check (standalone prompt)

Tests a REST/GraphQL endpoint against its actual contract — the
Codex-side equivalent of the Claude `api-tester` agent.

## Prompt / instructions

```
Test the following endpoint against its real contract, not just the
happy path:

ENDPOINT: <method + path, e.g. POST /api/orders>
CONTRACT: <paste the OpenAPI/GraphQL schema fragment, or the request/
           response types from the code, if no formal spec exists>

1. If no formal contract is given, derive it by reading the
   handler/resolver and its request/response types directly -- don't
   assume from the endpoint name alone.
2. Send real requests (curl, httpie, or the project's test client) and
   check actual responses. Never report a status/schema as correct
   without having actually seen the response.
3. Cover:
   - Valid request -> correct status code + response shape (types,
     required fields, no undocumented fields silently dropped/added)
   - Missing/invalid required fields -> correct 4xx + error shape
   - Auth: unauthenticated and under-privileged requests -> 401/403,
     not a silent 200 or a leaking 500
   - Boundary values on any typed/ranged field
   - Idempotency where the contract implies it (repeat a GET/PUT and
     compare)
4. Report each check as PASS/FAIL with the actual request sent and the
   actual response received (status + body), not a paraphrase.
5. Flag any contract mismatch found in the code itself (e.g. handler
   returns a field the schema doesn't declare) as a separate finding,
   not folded into a test result.

Do not mark auth or error-path checks as "assumed fine" -- these are the
highest-value cases and must be actually executed.
```

## Notes

If the project has a Playwright/HTTP MCP or similar structured client
configured, prefer it over raw `curl` in a shell for reproducibility.
