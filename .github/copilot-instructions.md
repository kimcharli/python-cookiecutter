# GitHub Copilot Instructions

This file provides context and rules for GitHub Copilot to ensure it follows the development patterns of the **Python Cookiecutter Template**.

## Project Context
- This is a **Cookiecutter** template repository.
- It is used to generate Python CLI and Web Dashboard projects.
- The template source is located in `{{cookiecutter.project_slug}}/`.

## Development Rules
- **Tooling**: Use `uv` for all dependency management tasks.
- **Commit Style**: Use **Conventional Commits** (`feat:`, `fix:`, `docs:`, etc.).
- **Jinja2 Templating**: When editing files inside `{{cookiecutter.project_slug}}/`, remember that these are templates. Use `{{ cookiecutter.variable }}` syntax correctly.
- **Code Quality**: Follow the rules defined in `.pre-commit-config.yaml` (Ruff, mdformat).

## Directory Structure
- `{{cookiecutter.project_slug}}/`: The project boilerplate source.
- `cookiecutter.json`: The configuration variables for the template.
- `docs/`: Documentation for the template itself.
