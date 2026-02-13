{% if cookiecutter.include_cli == "yes" -%}
from typer.testing import CliRunner
from {{ cookiecutter.pkg_name }}.cli import app

runner = CliRunner()

def test_cli_help():
    """Test that the CLI help command works."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "{{ cookiecutter.description }}" in result.stdout

def test_cli_version():
    """Test that the CLI version check works (placeholder for real logic)."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
{%- endif %}
