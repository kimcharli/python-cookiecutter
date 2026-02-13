{% if cookiecutter.include_web_dashboard == "yes" -%}
import os
from pathlib import Path

import yaml
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="{{ cookiecutter.project_name }}")

# Setup templates
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Load UI text from YAML config
# Try looking in the root config directory first
UI_TEXT_PATH = Path("config/ui_text.yaml")


def load_ui_text():
    # If not in CWD/config, check relative to the package
    search_path = UI_TEXT_PATH
    if not search_path.exists():
        # Fallback to package relative if it were bundled (less likely for config)
        pkg_root = Path(__file__).resolve().parents[2]
        search_path = pkg_root / "config" / "ui_text.yaml"

    if search_path.exists():
        with open(search_path, "r") as f:
            return yaml.safe_load(f)
    return {}


ui_content = load_ui_text()
templates.env.globals["ui"] = ui_content


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request,
        "layout.html",
        {"title": "Dashboard"},
    )
{%- else -%}
# Web dashboard is disabled. This file is a placeholder.
{%- endif %}
