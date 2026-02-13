# ADR 2: Standardize Dependencies and Linting Configuration

**Date**: 2026-02-13
**Status**: Accepted

## Context

The initial template had several issues that prevented it from being "ready-to-use" out of the box:
1.  **Dependency Versions**: The `pyproject.toml` contained future-dated versions (e.g., `ruff>=0.14.0`) that do not exist yet, causing environment sync to fail.
2.  **Linting Interference**: Running `ruff` at the repository root would attempt to parse the Jinja2-templated files in `{{cookiecutter.project_slug}}/`, leading to syntax errors because of the template tags.
3.  **Bootstrap Experience**: The `tests/` directory was empty, and path management in the web dashboard was reliant on the current working directory, which is inconsistent in different execution environments.

## Decision

1.  **Stable Dependencies**: Pin dependencies to existing stable versions (Ruff 0.9.x, Pytest 8.3.x, etc.).
2.  **Explicit Exclusion**: Configure the root `pyproject.toml` to exclude the `{{cookiecutter.project_slug}}/` directory from linting and formatting to avoid Jinja2 parsing errors.
3.  **Template Tests**: Include baseline unit tests for both CLI and Web components within the template to ensure a working test suite immediately after generation.
4.  **Robust Pathing**: Use package-relative path resolution for configuration files in the generated project.

## Consequences

- **Positive**: `uv sync` works immediately after project generation.
- **Positive**: Developers can run linting at the repository root without errors.
- **Positive**: The generated project includes a functional test suite, encouraging best practices from the start.
- **Negative**: Maintainers must manually exclude new template directories if the structure changes significantly.
