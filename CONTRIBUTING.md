# Contributing to Python Cookiecutter Template

Thank you for your interest in contributing! This document provides guidelines for setting up your local development environment and submitting changes to the template itself.

## 🛠️ Development Setup

We use `uv` for dependency management and `pre-commit` for code quality checks.

### 1. Prerequisites

- Python 3.13+
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

## 📜 Standards & Conventions

- **Branching**: Use descriptive branch names.
- **Commits**: Follow [Conventional Commits](https://www.conventionalcommits.org/) (e.g., `feat:`, `fix:`, `docs:`).
- **Code Style**: We use **Ruff** for formatting and linting.

## 🚀 Submitting Changes

1. Create a new branch.
1. Make your changes to the template files or the boilerplate.
1. Ensure all pre-commit checks are green.
1. Submit a Pull Request.
