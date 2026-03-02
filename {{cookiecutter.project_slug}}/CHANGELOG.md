# Changelog

All notable changes to **{{ cookiecutter.project_name }}** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - {% now 'utc', '%Y-%m-%d' %}

### Added

- Initial project generation via `python-cookiecutter`.
- Basic CLI structure using `Typer`.
  {%- if cookiecutter.include_web_dashboard == "yes" %}
- FastAPI web server with HTMX and Tailwind CSS.
  {%- endif %}
- Centralised `Settings` configuration (`config.py`) with YAML / env var / CLI resolution order.
- `config.yaml` at repository root (fully commented) and `specs/config.md` spec.
- `--config` and `--show-config` flags on the CLI entry point.
- Development environment setup with `uv` and `pre-commit`.
