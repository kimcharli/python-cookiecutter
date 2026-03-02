# Coding Conventions

This document outlines the coding standards for the **{{ cookiecutter.project_name }}** project.

## 1. Modern Python Standards

- **Python Version**: Target Python {{ cookiecutter.python_version }}+.
- **Type Hinting**: All new functions must have type hints for parameters and return values.
- **Path Handling**: Use `pathlib.Path` exclusively instead of `os.path`.
- **String Formatting**: Prefer f-strings for all string interpolations.

## 2. Error Handling

- Do not use bare `except:` blocks.
- Use the standard `logging` library.

## 3. Tooling

- **Formatting**: Automated via `ruff format` (triggered by pre-commit).
- **Linting**: Automated via `ruff check` (triggered by pre-commit).
- **Markdown**: Automated via `mdformat`.

## 4. Git Workflow

- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/).
  - `feat:` for new features.
  - `fix:` for bug fixes.
  - `docs:` for documentation changes.
  - `refactor:` for code restructuring.
  - `test:` for adding or modifying tests.

## 5. Spec-Driven Development (SDD)

This project follows SDD: write the spec before the code.

- **Config changes**: update `specs/config.md` before touching `config.py`.
- **New configurable surface**: add a row to the settings table in `specs/config.md` first.
- See [docs/sdd/README.md](sdd/README.md) for all adopted SDD practices.

### Configuration Consolidation

- All runtime settings live in `src/{{ cookiecutter.pkg_name }}/core/config.py` as the `Settings` dataclass.
- Resolution order: `CLI arg > env var > config.yaml > compiled-in default`.
- No `_WORKSPACE_ROOT` or hardcoded paths outside `config.py`.
- Every CLI entry point exposes `--config` and `--show-config`.
- See [docs/sdd/config-consolidation.md](sdd/config-consolidation.md) for the full practice.
