---
name: runbook-template
status: experimental
context: "Initial experimental version."
description: "Consistent on-call runbook format for a specific failure mode."
---

# Runbook: [Alert Name]

## 1. Meaning
[Why did this alert fire? What does it mean for the user?]

## 2. Investigation Steps
1. [Dashboard to check]
2. [Query to run]

## 3. Mitigation Steps
1. [Immediate action to stop the bleeding, e.g. scale up, rollback]

## 4. Escalation Path
[Who to call if step 3 doesn't work]
