{% if cookiecutter.include_cli == "yes" -%}
from pathlib import Path
from typing import Annotated, Optional

import typer

from .core.config import Settings

app = typer.Typer(
    help="{{ cookiecutter.description }}",
    add_completion=False,
)


@app.callback(invoke_without_command=True)
def main_callback(
    ctx: typer.Context,
    config: Annotated[
        Optional[Path],
        typer.Option(
            "--config",
            help="Path to config.yaml (default: <project_root>/config.yaml).",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
        ),
    ] = None,
    show_config: Annotated[
        bool,
        typer.Option(
            "--show-config",
            help="Print effective settings (with sources) and exit.",
        ),
    ] = False,
    input_dir: Annotated[
        Optional[Path],
        typer.Option("--input-dir", "-i", help="Override input_dir setting."),
    ] = None,
    output_dir: Annotated[
        Optional[Path],
        typer.Option("--output-dir", "-o", help="Override output_dir setting."),
    ] = None,
    log_level: Annotated[
        Optional[str],
        typer.Option("--log-level", help="Override log_level setting (DEBUG/INFO/WARNING/ERROR)."),
    ] = None,
):
    """{{ cookiecutter.description }}"""
    # 1. Load settings: defaults → config.yaml → env vars
    settings = Settings.load(config_path=config)

    # 2. Apply CLI overrides
    if input_dir is not None:
        settings.input_dir = input_dir.resolve()
        settings._sources["input_dir"] = "arg --input-dir"
    if output_dir is not None:
        settings.output_dir = output_dir.resolve()
        settings._sources["output_dir"] = "arg --output-dir"
    if log_level is not None:
        settings.log_level = log_level
        settings._sources["log_level"] = "arg --log-level"

    # 3. --show-config exits immediately
    if show_config:
        settings.show()
        raise typer.Exit(0)

    settings.setup_logging()
    ctx.obj = settings

    if ctx.invoked_subcommand is None:
        typer.echo("Run --help to see available commands.")

{% if cookiecutter.include_web_dashboard == "yes" %}

@app.command()
def serve(
    host: str = "127.0.0.1",
    port: int = 8000,
):
    """Starts the web dashboard (FastAPI + HTMX)."""
    import uvicorn

    from .web.main import app as web_app

    typer.echo(
        f"🚀 Starting web dashboard at http://{host}:{port}"
    )
    uvicorn.run(web_app, host=host, port=port)


{% endif %}

def main():
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
{%- else -%}
# CLI is disabled. This file is a placeholder.
def main():
    print("{{ cookiecutter.project_name }} is running.")


if __name__ == "__main__":
    main()
{%- endif %}
