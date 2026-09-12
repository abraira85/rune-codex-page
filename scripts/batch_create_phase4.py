#!/usr/bin/env python3
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

AGENTS = [
    {
        "area": "qa",
        "name": "white-box-test-designer",
        "description": "Designs test cases from the code's actual internal structure/branches and runs mutation testing.",
        "prompt": """You are a White-Box Test Designer.
1. Analyze the internal structure, branches, and cyclomatic complexity of the provided code.
2. Design test cases explicitly targeting uncovered branches and edge cases identified through static analysis.
3. Propose mutation testing strategies (e.g. replacing `>` with `>=`) to verify the suite's actual fault-detection strength.
4. Provide the exact test code needed to close structurally-identified coverage gaps.""",
        "notes": "Focuses on structural gaps, distinct from functional-tester."
    }
]

SKILLS = [
    {
        "area": "engineering",
        "name": "feature-scoping-template",
        "description": "Template for breaking a feature request into a technical plan.",
        "content": """# Feature Scoping Plan: [Feature Name]

## 1. Goal
[What is being built and why?]

## 2. Technical Approach
[High-level architecture, build-vs-buy decisions, main algorithms.]

## 3. Affected Areas & Components
- [Component A: What changes]
- [Component B: What changes]

## 4. Risks & Mitigations
- **Risk:** [e.g. Migration locking the DB]
- **Mitigation:** [e.g. Use a concurrent index creation]

## 5. Rollout Strategy
[Feature flags? Phased rollout? A/B test?]"""
    },
    {
        "area": "engineering",
        "name": "adr-writer",
        "description": "Architecture Decision Record (ADR) template and writing guide.",
        "content": """# ADR: [Short Noun Phrase]

## Context
[What is the problem we are trying to solve? What is the current state?]

## Decision
[What is the change that we are proposing and/or doing?]

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Consequences
[What becomes easier or more difficult because of this change?]"""
    },
    {
        "area": "engineering",
        "name": "onboarding-doc-template",
        "description": "Consistent structure for codebase-onboarding-guide's output.",
        "content": """# Codebase Tour: [Project Name]

## 1. The 10,000 Foot View
[What does this project do in 2 sentences?]

## 2. Key Directories
- `src/api`: [Purpose]
- `src/core`: [Purpose]

## 3. The Critical Path
[Trace a request from the entry point to the database and back.]

## 4. Local Development Gotchas
[What always breaks when setting this up locally?]"""
    },
    {
        "area": "engineering",
        "name": "tech-debt-ticket-template",
        "description": "Consistent write-up for a tracked tech-debt item.",
        "content": """# Tech Debt: [Title]

## The Problem
[Why is this code a liability?]

## Impact of NOT fixing
- **Velocity:** [e.g., adds 2 hours to every frontend PR]
- **Stability:** [e.g., frequent null pointer exceptions here]

## The Solution
[Proposed refactor or replacement]

## Effort Estimate
[T-Shirt size or days]"""
    },
    {
        "area": "security",
        "name": "vulnerability-report-template",
        "description": "Consistent CVE/finding write-up (severity, exploitability, remediation).",
        "content": """# Vulnerability Report: [Vulnerability Name]

## 1. Summary
[Brief description of the finding]

## 2. Severity & Metrics
- **CVSS Score:** [Score]
- **Exploitability:** [High/Medium/Low] (Is it reachable from user input?)

## 3. Proof of Concept / Reproduction
[Steps or script to reproduce the exploit]

## 4. Remediation
[Exact steps, code changes, or patch versions required to fix]"""
    },
    {
        "area": "security",
        "name": "threat-model-template",
        "description": "Consistent STRIDE-style write-up.",
        "content": """# Threat Model: [Feature/System]

## 1. System Overview & Trust Boundaries
[Diagram or description of where data crosses trust boundaries]

## 2. Identified Threats (STRIDE)
### Spoofing
- **Threat:** [Description]
- **Mitigation:** [Control]

### Tampering
- **Threat:** [Description]
- **Mitigation:** [Control]

*(Repeat for Repudiation, Information Disclosure, DoS, Elevation of Privilege)*"""
    },
    {
        "area": "devops",
        "name": "postmortem-template",
        "description": "Blameless incident postmortem format.",
        "content": """# Incident Postmortem: [Date] - [Title]

## 1. Summary
[High-level description of the incident and impact]

## 2. Timeline (UTC)
- `10:00`: [Alert fired]
- `10:05`: [First responder began investigation]
- `10:30`: [Service restored via rollback]

## 3. Root Cause
[The 5 Whys analysis of what structurally failed]

## 4. Action Items
- [ ] [Preventative measure 1]
- [ ] [Detection improvement 2]"""
    },
    {
        "area": "devops",
        "name": "runbook-template",
        "description": "Consistent on-call runbook format for a specific failure mode.",
        "content": """# Runbook: [Alert Name]

## 1. Meaning
[Why did this alert fire? What does it mean for the user?]

## 2. Investigation Steps
1. [Dashboard to check]
2. [Query to run]

## 3. Mitigation Steps
1. [Immediate action to stop the bleeding, e.g. scale up, rollback]

## 4. Escalation Path
[Who to call if step 3 doesn't work]"""
    },
    {
        "area": "devops",
        "name": "dr-drill-checklist",
        "description": "What a real DR drill needs to verify to count as done.",
        "content": """# DR Drill Checklist: [Scenario]

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
- [ ] RPO (Recovery Point Objective) met? [Yes/No]"""
    },
    {
        "area": "database",
        "name": "migration-safety-checklist",
        "description": "Backward-compatibility and reversibility checklist.",
        "content": """# Database Migration Safety Checklist

- [ ] Does this require a table lock? If so, is the table small enough, or are we using concurrent indexing?
- [ ] Is this migration backward-compatible with the currently running application code?
- [ ] Have we separated schema changes from data backfills?
- [ ] Is the `down` (rollback) script tested and perfectly reversible?
- [ ] Does this add a required column without a default value? (If so, it breaks inserts)."""
    },
    {
        "area": "data-ai",
        "name": "eval-dataset-template",
        "description": "Consistent format for a golden eval dataset.",
        "content": """# Golden Eval Dataset: [Prompt/Model Name]

## 1. Purpose
[What specific capability is this dataset evaluating?]

## 2. Test Cases

### Case 1: [Edge Case Name]
**Input:**
```
[User prompt]
```
**Expected Output / Criteria:**
- [Must contain X]
- [Must NOT contain Y]
**Why it matters:** [Reason this case was included]"""
    }
]

MCPS = [
    {
        "area": "engineering",
        "name": "code-search-mcp",
        "description": "Sourcegraph-style code search for large codebases.",
        "config": """{
  "mcpServers": {
    "code-search": {
      "command": "npx",
      "args": ["-y", "@sourcegraph/mcp-server", "--url", "YOUR_SOURCEGRAPH_URL", "--token", "YOUR_TOKEN"]
    }
  }
}"""
    },
    {
        "area": "security",
        "name": "sast-tool-mcp",
        "description": "Static application security testing (SAST) and vulnerability databases.",
        "config": """{
  "mcpServers": {
    "sast-scanner": {
      "command": "npx",
      "args": ["-y", "@semgrep/mcp-server", "--workspace", "/path/to/repo"]
    }
  }
}"""
    },
    {
        "area": "devops",
        "name": "cloud-provider-mcp",
        "description": "Query real infra state from AWS/GCP/Azure.",
        "config": """{
  "mcpServers": {
    "aws-cli": {
      "command": "npx",
      "args": ["-y", "@aws/mcp-server-cli", "--profile", "production"]
    }
  }
}"""
    },
    {
        "area": "devops",
        "name": "observability-mcp",
        "description": "Datadog, Grafana, or Prometheus integration.",
        "config": """{
  "mcpServers": {
    "datadog": {
      "command": "npx",
      "args": ["-y", "@datadog/mcp-server", "--api-key", "YOUR_API_KEY", "--app-key", "YOUR_APP_KEY"]
    }
  }
}"""
    },
    {
        "area": "database",
        "name": "database-mcp",
        "description": "Run real EXPLAIN plans and schema introspection.",
        "config": """{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@postgres/mcp-server", "postgresql://user:pass@localhost:5432/db"]
    }
  }
}"""
    },
    {
        "area": "data-ai",
        "name": "vector-db-mcp",
        "description": "Query Pinecone, Weaviate, or Qdrant for RAG pipeline review.",
        "config": """{
  "mcpServers": {
    "vector-db": {
      "command": "npx",
      "args": ["-y", "@pinecone/mcp-server", "--api-key", "YOUR_API_KEY"]
    }
  }
}"""
    },
    {
        "area": "data-ai",
        "name": "llm-observability-mcp",
        "description": "LangSmith or similar for real trace/eval data.",
        "config": """{
  "mcpServers": {
    "langsmith": {
      "command": "npx",
      "args": ["-y", "@langchain/mcp-server-langsmith", "--api-key", "YOUR_API_KEY"]
    }
  }
}"""
    }
]

def create_agent(agent):
    area, name, description, prompt, notes = agent["area"], agent["name"], agent["description"], agent["prompt"], agent["notes"]
    platforms = [
        ("antigravity", "agents", "inherit", "[view_file, grep_search, list_dir, run_command]"),
        ("claude", "agents", "sonnet", "[view_file, grep_search, list_dir, run_command]"),
        ("codex", "prompts", None, None)
    ]

    for platform, type_dir, model, tools in platforms:
        dest_dir = ROOT / "catalog" / area / platform / type_dir
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_dir / f"{name}.md"

        content = []
        if platform != "codex":
            content.append("---")
            content.append(f"name: {name}")
            content.append("status: experimental")
            content.append(f"context: {json.dumps('Initial experimental version.')}")
            content.append(f"description: {json.dumps(description)}")
            if tools:
                content.append(f"tools: {tools}")
            if model:
                content.append(f"model: {model}")
            content.append("---\n")
            content.append(f"# {name.replace('-', ' ').title()}\n")
            content.append(f"{description}\n")
            content.append("## Prompt / instructions\n")
            content.append("```")
            content.append(prompt)
            content.append("```\n")
            content.append("## Notes\n")
            content.append(f"{notes}\n")
        else:
            content.append("---")
            content.append(f"name: {name}")
            content.append("status: experimental")
            content.append(f"context: {json.dumps('Initial experimental version.')}")
            content.append(f"description: {json.dumps(description)}")
            content.append("---\n")
            content.append(f"# {name.replace('-', ' ').title()}\n")
            content.append(f"{description}\n")
            content.append("## Prompt / instructions\n")
            content.append("```")
            content.append(prompt)
            content.append("```\n")
            content.append("## Notes\n")
            content.append(f"{notes}\n")

        dest_file.write_text("\n".join(content), encoding="utf-8")
        print(f"Created {dest_file.relative_to(ROOT)}")

def create_skill(skill):
    area, name, description, content_body = skill["area"], skill["name"], skill["description"], skill["content"]
    platforms = ["antigravity", "claude"]
    
    for platform in platforms:
        dest_dir = ROOT / "catalog" / area / platform / "skills" / name
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_dir / "SKILL.md"

        content = []
        content.append("---")
        content.append(f"name: {name}")
        content.append("status: experimental")
        content.append(f"context: {json.dumps('Initial experimental version.')}")
        content.append(f"description: {json.dumps(description)}")
        content.append("---\n")
        content.append(content_body)
        content.append("")

        dest_file.write_text("\n".join(content), encoding="utf-8")
        print(f"Created {dest_file.relative_to(ROOT)}")

def create_mcp(mcp):
    area, name, description, config_body = mcp["area"], mcp["name"], mcp["description"], mcp["config"]
    platforms = ["antigravity", "claude"]
    
    for platform in platforms:
        dest_dir = ROOT / "catalog" / area / platform / "mcp"
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_dir / f"{name}.md"

        content = []
        content.append("---")
        content.append(f"name: {name}")
        content.append("status: experimental")
        content.append(f"context: {json.dumps('Initial experimental version.')}")
        content.append(f"description: {json.dumps(description)}")
        content.append("---\n")
        content.append(f"# {name.replace('-', ' ').title()}\n")
        content.append(f"{description}\n")
        content.append("## Configuration\n")
        content.append("```json")
        content.append(config_body)
        content.append("```\n")

        dest_file.write_text("\n".join(content), encoding="utf-8")
        print(f"Created {dest_file.relative_to(ROOT)}")

if __name__ == "__main__":
    for agent in AGENTS:
        create_agent(agent)
    for skill in SKILLS:
        create_skill(skill)
    for mcp in MCPS:
        create_mcp(mcp)
