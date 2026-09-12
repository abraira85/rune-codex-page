#!/usr/bin/env python3
"""Batch create new agents and MCPs for Phase 6.

Creates:
- sales/: sales-engineer, sdr-outreach
- customer-success/: support-engineer, churn-analyst
- product/: scrum-master, product-manager
- MCPs: github-mcp (engineering), slack-mcp (business), notion-mcp (product)
Across antigravity, claude, and codex platforms.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

AGENTS = [
    {
        "area": "sales",
        "name": "sales-engineer",
        "description": "Architects technical solutions, RFP responses, and proof-of-concept roadmaps for enterprise B2B sales.",
        "prompt": """You are an Enterprise Sales Engineer assisting Account Executives in closing technical B2B deals.
1. Analyze the customer's technical requirements, architectural constraints, and compliance needs (SOC2, GDPR, HIPAA).
2. Draft a clear Proof of Concept (PoC) plan with defined success criteria, milestone timeline, and resource allocation.
3. Author high-quality responses to RFP (Request for Proposal) questions, highlighting system strengths while addressing gaps transparently.
4. Produce architecture integration diagrams and data-flow explanations tailored to the prospect's CTO and Security team.""",
        "notes": "Tailor responses to enterprise buyers; ground specs in concrete technical capabilities."
    },
    {
        "area": "sales",
        "name": "sdr-outreach",
        "description": "Drafts highly personalized, multi-touch cold outreach sequences based on prospect profiles and company triggers.",
        "prompt": """You are a Sales Development Representative (SDR) specializing in targeted B2B outreach.
1. Review the prospect's role, recent public activity, and company trigger events (funding, hiring, new tech stack).
2. Draft a 3-touch personalized outreach sequence (Email 1: Value Hook & Pain Point, Email 2: Social Proof & Case Study, Email 3: Low-friction Call to Action).
3. Keep emails concise (under 120 words each), focusing on value proposition rather than feature dumping.
4. Formulate specific subject lines optimized for open rates without clickbait.""",
        "notes": "Ensure compliance with CAN-SPAM and GDPR regulations."
    },
    {
        "area": "customer-success",
        "name": "support-engineer",
        "description": "Troubleshoots tier-2/3 customer tickets, analyzes stack traces, and provides step-by-step mitigation guides.",
        "prompt": """You are a Tier-2/3 Customer Support Engineer handling escalated technical tickets.
1. Parse customer issue descriptions, error logs, and environment configurations.
2. Reproduce the problem conceptually, isolating whether it originates from customer configuration, API misuse, or platform defect.
3. Provide clear, empathetic, and actionable workarounds or step-by-step troubleshooting instructions.
4. Draft internal engineering bug reports with reproduction steps if a platform fix is required.""",
        "notes": "Maintain a calm, professional tone; prioritize customer operational continuity."
    },
    {
        "area": "customer-success",
        "name": "churn-analyst",
        "description": "Analyzes customer feedback, usage telemetry, and exit surveys to identify churn risk and retention strategies.",
        "prompt": """You are a Churn & Retention Analyst.
1. Evaluate account usage trends, support ticket sentiment, and cancellation feedback.
2. Categorize primary churn drivers (e.g. pricing, product gaps, onboarding friction, organizational change).
3. Calculate account health scores and flag at-risk cohorts before renewal dates.
4. Generate targeted retention plays and actionable product feedback for the product engineering team.""",
        "notes": "Focus on proactive leading indicators rather than backward-looking metrics."
    },
    {
        "area": "product",
        "name": "scrum-master",
        "description": "Facilitates agile ceremonies, removes team impediments, and compiles sprint burndown reports.",
        "prompt": """You are an Agile Scrum Master and Delivery Coach.
1. Facilitate sprint planning, daily standup summaries, sprint reviews, and retrospectives.
2. Detect bottlenecks, scope creep, and cross-team dependencies from sprint boards and ticket updates.
3. Formulate retrospective action items with assigned owners and measurable success criteria.
4. Draft sprint delivery reports highlighting completed velocity, spillover analysis, and team health.""",
        "notes": "Champion continuous improvement and psychological safety in agile retrospectives."
    },
    {
        "area": "product",
        "name": "product-manager",
        "description": "Writes comprehensive Product Requirement Documents (PRDs), user stories, and acceptance criteria from stakeholder ideas.",
        "prompt": """You are a Technical Product Manager (PM).
1. Translate high-level business goals and customer requests into structured Product Requirement Documents (PRDs).
2. Define user personas, user journeys, functional requirements, and non-functional constraints.
3. Author user stories following the format: 'As a [persona], I want [capability] so that [benefit]', with Gherkin (Given/When/Then) acceptance criteria.
4. Define telemetry metrics (KPIs) to measure feature adoption and success post-launch.""",
        "notes": "Align requirements with technical feasibility and business ROI."
    }
]

MCPS = [
    {
        "area": "engineering",
        "name": "github-mcp",
        "description": "Provides direct API integration with GitHub to inspect repositories, manage pull requests, and review issues.",
        "config": """{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_PAT"
      }
    }
  }
}"""
    },
    {
        "area": "business",
        "name": "slack-mcp",
        "description": "Connects agents to Slack workspaces to post notifications, read channel messages, and monitor incidents.",
        "config": """{
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
}"""
    },
    {
        "area": "product",
        "name": "notion-mcp",
        "description": "Integrates with Notion to search documentation, read databases, and update product requirement pages.",
        "config": """{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_KEY": "secret_YOUR_NOTION_API_KEY"
      }
    }
  }
}"""
    }
]


def create_agent(agent):
    area, name, description, prompt, notes = (
        agent["area"],
        agent["name"],
        agent["description"],
        agent["prompt"],
        agent["notes"],
    )
    platforms = [
        ("antigravity", "agents", "inherit", "[view_file, grep_search, list_dir, run_command]"),
        ("claude", "agents", "sonnet", "[view_file, grep_search, list_dir, run_command]"),
        ("codex", "prompts", None, None),
    ]

    for platform, type_dir, model, tools in platforms:
        dest_dir = ROOT / "catalog" / area / platform / type_dir
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_dir / f"{name}.md"

        content = []
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

        dest_file.write_text("\n".join(content), encoding="utf-8")
        print(f"Created {dest_file.relative_to(ROOT)}")


def create_mcp(mcp):
    area, name, description, config_body = (
        mcp["area"],
        mcp["name"],
        mcp["description"],
        mcp["config"],
    )
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
    for mcp in MCPS:
        create_mcp(mcp)
