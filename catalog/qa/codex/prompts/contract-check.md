---
name: contract-check
status: experimental
context: "Authored for rune-codex-page's QA team — not yet run in a real project."
---

# Contract Check (standalone prompt)

Verifies a provider against every real consumer's actual contract
expectations, not just its own spec — the Codex-side equivalent of the
Claude `contract-tester` agent.

## Prompt / instructions

```
Check the following provider change against its real consumers' contracts:

PROVIDER CHANGE: <endpoint/service and what changed>

1. Check whether the project already uses a contract-testing tool (Pact
   is most common; a broker like Pactflow may be configured) and use it
   as-is. If none exists, say so -- don't fabricate a contract from
   reading the provider's own code, since a contract test's value comes
   from the consumer's real expectations, not the provider's
   self-description.
2. Find every real consumer of this provider. If this relationship isn't
   captured in any existing contract, that's a finding worth reporting on
   its own.
3. Run the actual provider verification against a real running instance
   of the provider (not a mock), for each consumer contract found.
4. Report per interaction: which consumer, what was expected, what the
   provider actually returned, and precisely what would break for that
   consumer if this shipped.
5. For a deliberate breaking change, check whether a real
   versioning/deprecation strategy exists -- flag if none does.
6. Never treat "the endpoint's own tests pass" as evidence the contract
   is satisfied -- those are different questions.

Hand off a broken contract to `bug-report.md` in this folder, naming the
specific consumer(s) affected.
```

## Notes

Complements `api-contract-check.md` in this folder -- that one verifies
a single endpoint against its own declared spec; this one verifies it
against every real consumer's actual expectations.
