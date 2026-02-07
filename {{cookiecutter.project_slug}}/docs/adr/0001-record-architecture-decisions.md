# ADR 1: Record Architecture Decisions

**Date**: {% now 'utc', '%Y-%m-%d' %}
**Status**: Accepted

## Context

We need a way to track significant architectural decisions made during the development of {{ cookiecutter.project_name }}. These decisions should be documented to provide historical context and explain the "why" behind tool choices and structure.

## Decision

We will use Architecture Decision Records (ADRs) to track these choices. ADRs will be stored as Markdown files in the `docs/adr/` directory, following a numbered sequence.

## Consequences

- **Positive**: Future maintainers will understand why specific tools (like `uv`, `ruff`, `pre-commit`) were chosen.
- **Positive**: Prevents repetitive debates on previously settled architectural topics.
- **Negative**: Requires a small amount of overhead to document decisions as they happen.
