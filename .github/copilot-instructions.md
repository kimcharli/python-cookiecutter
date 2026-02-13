# GitHub Copilot Instructions

This file provides context and rules for GitHub Copilot to ensure it follows the development patterns of the **Python Cookiecutter Template**.

## Project Context

- This is a **Cookiecutter** template repository.
- It is used to generate Python CLI and Web Dashboard projects.
- The template source is located in `{{cookiecutter.project_slug}}/`.

## Development Rules

- **Tooling**: Use `uv` for all dependency management tasks.
- **Commit Style**: Use **Conventional Commits** (`feat:`, `fix:`, `docs:`, etc.).
- **Linting & Quality**: Ensure all code and Markdown follow the rules in `.pre-commit-config.yaml`. Specifically, use `ruff` standards for Python and `mdformat` for Markdown. Do not generate code that would require manual fixing to pass pre-commit hooks.
- **Jinja2 Templating**: When editing files inside `{{cookiecutter.project_slug}}/`, remember that these are templates. Use `{{ cookiecutter.variable }}` syntax correctly.

## Directory Structure

- `{{cookiecutter.project_slug}}/`: The project boilerplate source.
- `cookiecutter.json`: The configuration variables for the template.
- `docs/`: Documentation for the template itself.
