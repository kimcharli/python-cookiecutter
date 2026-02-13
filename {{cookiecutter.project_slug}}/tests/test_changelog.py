from pathlib import Path
import pytest

def test_changelog_exists():
    """Ensure the CHANGELOG.md file exists in the generated project."""
    assert Path("CHANGELOG.md").exists()

def test_changelog_has_initial_version():
    """Ensure the CHANGELOG.md contains the initial version tracker."""
    content = Path("CHANGELOG.md").read_text()
    assert "## [0.1.0]" in content
    assert "Initial project generation" in content
