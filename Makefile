.PHONY: setup test-template test-all

setup:
	uv run pre-commit install --hook-type commit-msg --hook-type pre-commit

test-template:
	@echo "Verifying template generation..."
	@mkdir -p .test-output
	@uv run cookiecutter . -o .test-output --no-input --overwrite-if-exists
	@echo "Running tests in generated project..."
	@cd .test-output/my-project && uv run pytest
	@echo "Verifying configurations..."
	@grep "tool.commitizen" .test-output/my-project/pyproject.toml > /dev/null || (echo "CZ config missing in template!" && exit 1)
	@grep "cz-changelog" .test-output/my-project/.pre-commit-config.yaml > /dev/null || (echo "CZ hook missing in template!" && exit 1)
	@rm -rf .test-output
	@echo "Template verification successful."

test-all: test-template
	uv run pytest
