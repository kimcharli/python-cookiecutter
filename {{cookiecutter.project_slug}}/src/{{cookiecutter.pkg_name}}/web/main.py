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
UI_TEXT_PATH = Path(os.getcwd()) / "config" / "ui_text.yaml"


def load_ui_text():
    if UI_TEXT_PATH.exists():
        with open(UI_TEXT_PATH, "r") as f:
            return yaml.safe_load(f)
    return {}


ui_content = load_ui_text()
templates.env.globals["ui"] = ui_content


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "layout.html",
        {"request": request, "title": "Dashboard"},
    )
{%- else -%}
# Web dashboard is disabled. This file is a placeholder.
{%- endif %}
