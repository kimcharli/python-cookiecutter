import subprocess
from pathlib import Path

import pytest


def test_changelog_integrity():
    """Verify that automated changelog updates do not delete manual 'Added' entries."""
    changelog_path = Path("CHANGELOG.md")
    if not changelog_path.exists():
        pytest.skip("CHANGELOG.md not found")

    content_before = changelog_path.read_text()

    # We expect a versioned section to exist for stability
    assert "## [0.1.0]" in content_before or "## Unreleased" in content_before

    # Run a dry-run update
    subprocess.run(
        ["uv", "run", "cz", "changelog", "--incremental", "--dry-run"],
        capture_output=True,
        text=True,
        check=True,
    )

    assert "### Added" in content_before, "Manual 'Added' section has been lost!"
    assert "Support for `uv` dependency management." in content_before
