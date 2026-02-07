"""Allow running as `python -m {{ cookiecutter.pkg_name }}`."""

{% if cookiecutter.include_cli == "yes" -%}
from {{ cookiecutter.pkg_name }}.cli import main

main()
{%- else -%}
print("{{ cookiecutter.project_name }} is running.")
{%- endif %}
