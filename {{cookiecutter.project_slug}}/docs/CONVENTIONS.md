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
