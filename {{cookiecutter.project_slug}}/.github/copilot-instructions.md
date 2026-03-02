# GitHub Copilot Instructions

This file provides context and rules for GitHub Copilot to ensure it follows the architectural and coding patterns of **{{ cookiecutter.project_name }}**.

## Project Stack

- **Manager**: `uv` for dependency management and scripts.
- **Build System**: `hatchling` (PEP 621) with `src/` layout.
- **CLI**: `typer` for command-line interfaces.
- **Web**: FastAPI + HTMX + Tailwind CSS (if enabled).
- **QA**: `ruff` for linting/formatting, `pytest` for testing.

## Coding Standards

- **Python**: Target version {{ cookiecutter.python_version }}+.
- **Linting & Quality**: Adhere strictly to the rules in `.pre-commit-config.yaml`. Always format Python code according to `ruff` and Markdown according to `mdformat`. Do not generate code that would fail pre-commit checks.
- **Typing**: Use strict type hints for all function signatures.
- **Paths**: Use `pathlib.Path` exclusively; do not use `os.path`.
- **Formatting**: Prefer f-strings for string interpolation.
- **Configuration**: Use the centralised `Settings` dataclass in `src/{{ cookiecutter.pkg_name }}/core/config.py`.
  Load with `Settings.load()` — resolution order: CLI arg > env var > `config.yaml` > compiled-in default.
  Never define `_WORKSPACE_ROOT` or hardcode paths outside `config.py`.

## Patterns

- **CLI Commands**: Add new commands to `src/{{ cookiecutter.pkg_name }}/cli.py` or separate modules in `commands/`.
- **Logging**: Use the built-in `logging` module, configured via `settings.setup_logging()`.
- **UI Text**: Store user-facing strings in `config/ui_text.yaml` rather than hardcoding.
- **SDD**: Update `specs/config.md` before changing any setting. See `docs/sdd/` for all adopted practices.

## Workspace Layout

- Source: `src/{{ cookiecutter.pkg_name }}/`
- Documentation: `docs/` (includes ADRs and CONVENTIONS.md)
- Tests: `tests/`
- Config: `config/`
