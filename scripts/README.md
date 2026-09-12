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

### 3. `generate_index.py`
Crawls the `catalog/` tree and generates `index.json`, a machine-readable summary of the entire catalog used by CLIs and third-party tools.

### 4. `batch_create_agents.py` & `batch_create_phase4.py`
Templating scripts used to rapidly scaffold the initial repository structure.

## Development

If you modify these scripts, please ensure you run the unit tests:
```bash
pytest scripts/test_install.py
```
