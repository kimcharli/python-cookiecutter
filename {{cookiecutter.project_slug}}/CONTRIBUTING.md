# Contributing to {{ cookiecutter.project_name }}

Thank you for your interest in contributing! This document provides guidelines for setting up your local development environment and submitting changes.

## 🛠️ Development Setup

We use `uv` for dependency management and `pre-commit` for code quality checks.

### 1. Prerequisites

- Python {{ cookiecutter.python_version }}+
- [uv](https://github.com/astral-sh/uv) installed on your system.

### 2. Initial Setup

Clone the repository and sync the dependencies:

```bash
uv sync
```

### 3. Pre-commit Hooks

We use `pre-commit` to ensure code quality (Ruff, mdformat, etc.) is consistent before any code is committed.

**Installation**:

```bash
uv run pre-commit install
```

**Running Manually**:
If you want to check all files without committing:

```bash
uv run pre-commit run --all-files
```

## 🧪 Running Tests

We use `pytest` for testing.

```bash
uv run pytest
```

## 📜 Standards & Conventions

- **Branching**: Use descriptive branch names (e.g., `feature/add-logic`).
- **Commits**: Follow [Conventional Commits](https://www.conventionalcommits.org/) (e.g., `feat:`, `fix:`, `docs:`).
- **Code Style**: We use **Ruff** for formatting and linting.
- **Documentation**: See [docs/CONVENTIONS.md](docs/CONVENTIONS.md) for detailed coding standards.

## 🚀 Submitting Changes

1. Create a new branch.
1. Make your changes.
1. Ensure all tests pass and pre-commit checks are green.
1. Submit a Pull Request.
