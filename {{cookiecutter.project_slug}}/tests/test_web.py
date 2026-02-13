{% if cookiecutter.include_web_dashboard == "yes" -%}
from fastapi.testclient import TestClient
from {{ cookiecutter.pkg_name }}.web.main import app

client = TestClient(app)

def test_read_main():
    """Test the main entry point of the web dashboard."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Dashboard" in response.text
{%- endif %}
