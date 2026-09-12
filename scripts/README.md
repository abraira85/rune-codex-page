# Scripts (Repo Infrastructure)

This directory contains the automation backbone of the `rune-codex-page` catalog. It ensures that 300+ items remain structurally sound, well-documented, and easy to extract.

## Tools

### 1. `install.py`
Extracts a prompt payload from a Markdown file and installs it into the target tool's native configuration structure (e.g. copying an `antigravity` agent to `.agents/agents/<slug>.md`). It safely strips repo-specific metadata and correctly parses nested code blocks.

**Usage:**
```bash
python3 scripts/install.py catalog/engineering/claude/agents/code-reviewer.md --target ../my-project
```

### 2. `validate.py`
The source of truth for repository health. Every PR is checked against this script. It verifies that every Markdown file has valid YAML front-matter with `name`, `status`, `context`, and `description`.

### 3. `lint_prompts.py`
Semantic and structural prompt quality linter. Validates payload length, detects unfinished placeholders (`TODO`, `FIXME`), verifies JSON formatting in MCP definitions, and checks directive actionability.

**Usage:**
```bash
python3 scripts/lint_prompts.py
python3 scripts/lint_prompts.py --strict
```

### 4. `rune-search.py`
Terminal CLI catalog search utility. Allows instant querying of agents and tools across name, description, area, and type directly from your shell.

**Usage:**
```bash
python3 scripts/rune-search.py "sales"
```

### 5. `generate_index.py`
Crawls the `catalog/` tree and compiles `catalog/index.json` as well as `docs/data/index.json` (for the static GitHub Pages UI) with full metadata and prompt payloads.

### 6. Batch Generators
- `batch_create_phase5.py`: Scaffolds HR, Finance, and Marketing agents & tools.
- `batch_create_phase6.py`: Scaffolds Sales, Customer Success, Product agents, and core MCP servers (GitHub, Slack, Notion).

## Development & Testing

Ensure all quality checks and unit tests pass before submitting changes:
```bash
pytest scripts/test_install.py
python3 scripts/validate.py
python3 scripts/lint_prompts.py --strict
```

