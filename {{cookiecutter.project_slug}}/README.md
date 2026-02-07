# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Quick Start

```bash
# Install dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install

{% if cookiecutter.include_cli == "yes" -%}
# Run the CLI
uv run {{ cookiecutter.project_slug }} --help
{%- endif %}

{% if cookiecutter.include_web_dashboard == "yes" -%}
# Start the web dashboard
uv run {{ cookiecutter.project_slug }} serve
{%- endif %}

# Run tests
uv run pytest
```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── config/          # YAML configuration files
├── data/            # Input/output data (gitignored)
├── docs/            # Project documentation, ADRs, conventions
├── src/             # Application source code
│   └── {{ cookiecutter.pkg_name }}/
└── tests/           # Unit and integration tests
```

## Documentation

See [docs/README.md](docs/README.md) for the full documentation index.
