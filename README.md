# Python Cookiecutter Template

A standardized project template for Python CLI + Web Dashboard applications.

## Features

- **`uv`** for fast dependency management and packaging
- **`hatchling`** build backend with `src/` layout
- **`typer`** CLI framework with centralized `AppConfig`
- **`FastAPI` + `HTMX` + `Tailwind CSS`** web dashboard (optional)
- **`ruff`** for linting and formatting
- **`mdformat`** for Markdown consistency
- **`pre-commit`** hooks for automated code quality
- **`pytest`** with `src/` layout support
- **Architecture Decision Records (ADRs)** for documenting technical choices
- **YAML-based UI text configuration** for dashboards
- **Coding Conventions** document

## Usage

```bash
# Install cookiecutter via uv
uv tool install cookiecutter

# Generate a new project
cookiecutter gh:kimcharli/python-cookiecutter

# Or from a local clone
cookiecutter /path/to/python-cookiecutter
```

You will be prompted for:

| Variable | Default | Description |
| :--- | :--- | :--- |
| `project_name` | `My Project` | Human-readable project name |
| `project_slug` | (auto) | Directory and repo name (e.g., `my-project`) |
| `pkg_name` | (auto) | Python package name (e.g., `my_project`) |
| `description` | — | Short project description |
| `author` | — | Author name |
| `python_version` | `3.13` | Minimum Python version |
| `include_web_dashboard` | `yes` | Include FastAPI + HTMX dashboard |
| `include_cli` | `yes` | Include Typer CLI scaffolding |

## After Generation

```bash
cd my-project
git init
uv sync
uv run pre-commit install
uv run pytest
```

## Project Structure (Generated)

```
my-project/
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── pyproject.toml
├── README.md
├── config/
│   └── ui_text.yaml
├── docs/
│   ├── CONVENTIONS.md
│   ├── README.md
│   ├── TODO.md
│   └── adr/
│       └── 0001-record-architecture-decisions.md
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── config.py
│       │   └── models.py
│       ├── commands/
│       │   └── __init__.py
│       ├── utils/
│       │   └── __init__.py
│       └── web/
│           ├── main.py
│           └── templates/
│               └── layout.html
└── tests/
    └── __init__.py
```

