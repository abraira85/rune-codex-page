---
name: dr-drill-checklist
status: experimental
context: "Initial experimental version."
description: "What a real DR drill needs to verify to count as done."
---

# DR Drill Checklist: [Scenario]

## Pre-requisites
- [ ] Stakeholders notified of drill.
- [ ] War room channel created.

## Execution
- [ ] Simulated failure triggered.
- [ ] Alerting fired within expected timeframe.
- [ ] Failover / Restore procedure executed from runbook.

## Validation
- [ ] Data integrity verified post-restore.
- [ ] RTO (Recovery Time Objective) met? [Yes/No]
- [ ] RPO (Recovery Point Objective) met? [Yes/No]
