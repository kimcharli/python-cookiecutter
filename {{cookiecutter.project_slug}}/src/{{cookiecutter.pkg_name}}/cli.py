{% if cookiecutter.include_cli == "yes" -%}
import logging
from pathlib import Path
from typing import Annotated

import typer

from .core.config import AppConfig

app = typer.Typer(
    help="{{ cookiecutter.description }}",
    add_completion=False,
)


@app.callback(invoke_without_command=True)
def main_callback(
    ctx: typer.Context,
    input_dir: Annotated[
        Path,
        typer.Option(
            "--input-dir",
            "-i",
            help="Directory containing input files.",
            exists=True,
            file_okay=False,
            dir_okay=True,
            readable=True,
            resolve_path=True,
        ),
    ] = Path("./data/input"),
    output_dir: Annotated[
        Path,
        typer.Option(
            "--output-dir",
            "-o",
            help="Directory to save output results.",
            file_okay=False,
            dir_okay=True,
            writable=True,
            resolve_path=True,
        ),
    ] = Path("./data/output"),
    log_file: Annotated[
        Path | None,
        typer.Option(
            "--log-file",
            "-l",
            help="Path to the log file.",
            file_okay=True,
            dir_okay=False,
            writable=True,
            resolve_path=True,
        ),
    ] = Path("./data/logs/app.log"),
    log_level: Annotated[
        str,
        typer.Option(
            "--log-level",
            help="Logging level (DEBUG, INFO, WARNING, ERROR).",
        ),
    ] = "INFO",
):
    """{{ cookiecutter.description }}"""
    config = AppConfig(
        input_dir=input_dir,
        output_dir=output_dir,
        log_file=log_file,
        log_level=log_level,
    )
    config.setup_logging()

    ctx.obj = config

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
