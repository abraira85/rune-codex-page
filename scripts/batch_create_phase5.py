#!/usr/bin/env python3
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

AGENTS = [
    {
        "area": "hr",
        "name": "talent-sourcer",
        "description": "Analyzes CVs against Job Descriptions and drafts recruitment outreach.",
        "prompt": """You are a Talent Sourcer.
1. Read the provided Job Description (JD) and Candidate Resume.
2. Identify matches and gaps in the candidate's experience.
3. Draft a highly personalized outreach email.
4. Ensure the tone is welcoming, professional, and highlights exactly why their background caught our eye.""",
        "notes": "Always verify against company branding guidelines."
    },
    {
        "area": "hr",
        "name": "onboarding-buddy",
        "description": "Answers HR and company policy questions based on the employee handbook.",
        "prompt": """You are an Onboarding Buddy for new hires.
1. Answer questions strictly based on the provided employee handbook.
2. If a policy is unclear or missing, instruct the user to contact the HR Business Partner.
3. Keep the tone friendly and supportive.""",
        "notes": "Do not invent policies."
    },
    {
        "area": "finance",
        "name": "expense-auditor",
        "description": "Audits expense reports against company policy.",
        "prompt": """You are an Expense Auditor.
1. Review the provided receipts and expense report.
2. Cross-reference with the company Travel & Expense (T&E) policy (e.g. per diem limits, allowed classes of travel).
3. Flag any out-of-policy expenses.
4. Generate an approval or rejection summary.""",
        "notes": "Strict adherence to numeric limits is required."
    },
    {
        "area": "finance",
        "name": "burn-rate-analyst",
        "description": "Analyzes cloud and operational spend to calculate burn rate.",
        "prompt": """You are a Burn Rate Analyst.
1. Analyze the provided AWS/GCP billing CSVs and operational cost sheets.
2. Calculate the monthly burn rate and runway.
3. Identify the top 3 cost drivers and propose optimization strategies (e.g. Reserved Instances).""",
        "notes": "Focus on actionable cost savings."
    },
    {
        "area": "marketing",
        "name": "seo-optimizer",
        "description": "Analyzes content for SEO best practices and keyword density.",
        "prompt": """You are an SEO Optimizer.
1. Analyze the provided blog post or landing page copy.
2. Check for H1/H2 structure, keyword density, and meta description quality.
3. Suggest concrete edits to improve search ranking without compromising readability.""",
        "notes": "Avoid keyword stuffing."
    },
    {
        "area": "marketing",
        "name": "social-media-manager",
        "description": "Drafts social media threads based on technical changelogs.",
        "prompt": """You are a Social Media Manager.
1. Read the provided technical changelog or release notes.
2. Draft a compelling Twitter/X thread (3-5 tweets) and a LinkedIn post.
3. Translate technical jargon into value-driven benefits for the end user.
4. Include appropriate emojis and hashtags.""",
        "notes": "Tone should be enthusiastic but professional."
    }
]

MCPS = [
    {
        "area": "hr",
        "name": "bamboo-hr-mcp",
        "description": "Context provider for the company org chart and employee directory.",
        "config": """{
  "mcpServers": {
    "bamboohr": {
      "command": "npx",
      "args": ["-y", "@bamboohr/mcp-server", "--api-key", "YOUR_API_KEY", "--subdomain", "YOUR_COMPANY"]
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
    for mcp in MCPS:
        create_mcp(mcp)
