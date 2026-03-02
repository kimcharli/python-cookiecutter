"""Global settings for {{ cookiecutter.pkg_name }}.

Resolution order (highest wins):
    CLI arg  >  env var  >  config.yaml  >  compiled-in default

See docs/sdd/config-consolidation.md for the full practice description.
See specs/config.md for the settings spec.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)

# Workspace root: the repository root, independent of CWD.
# Defined here only — every other module receives paths via Settings.
_WORKSPACE_ROOT = Path(__file__).parent.parent.parent


def _abs(p: Path | str) -> Path:
    """Resolve a path: absolute as-is, relative → anchored to workspace root."""
    p = Path(p)
    return p if p.is_absolute() else _WORKSPACE_ROOT / p


# Environment variable prefix: {{ cookiecutter.pkg_name | upper }}_
# e.g.  {{ cookiecutter.pkg_name | upper }}_OUTPUT_DIR,  {{ cookiecutter.pkg_name | upper }}_WEB_PORT
# Set {{ cookiecutter.pkg_name | upper }}_CONFIG to point to a custom config.yaml.
_ENV_PREFIX = "{{ cookiecutter.pkg_name | upper }}_"


@dataclass
class Settings:
    """Centralised runtime settings.  Populated by Settings.load()."""

    # ------------------------------------------------------------------ paths
    input_dir: Path = field(default_factory=lambda: _abs("data/input"))
    output_dir: Path = field(default_factory=lambda: _abs("data/output"))
    logs_dir: Path = field(default_factory=lambda: _abs("data/logs"))

    # --------------------------------------------------------- runtime values
    log_level: str = "INFO"
    web_port: int = 8000

    # Internal bookkeeping — not exposed as user-facing settings.
    _config_file_path: Path | None = field(default=None, repr=False, compare=False)
    _sources: dict[str, str] = field(default_factory=dict, repr=False, compare=False)

    # ------------------------------------------------------------------
    # Factory
    # ------------------------------------------------------------------

    @classmethod
    def load(cls, config_path: Path | str | None = None) -> "Settings":
        """Build a fully-resolved Settings instance.

        1. Start from compiled-in defaults.
        2. Merge config.yaml (from *config_path*, the ``{{ cookiecutter.pkg_name | upper }}_CONFIG``
           env var, or ``<workspace_root>/config.yaml``).
        3. Overlay ``{{ cookiecutter.pkg_name | upper }}_*`` environment variables.

        CLI overrides are applied by the caller after this method returns.
        """
        instance = cls()
        sources: dict[str, str] = {
            f.name: "default"
            for f in fields(cls)
            if not f.name.startswith("_")
        }

        # --- step 2: config file ---
        cfg_path = _resolve_config_path(config_path)
        if cfg_path and cfg_path.exists():
            data = yaml.safe_load(cfg_path.read_text()) or {}
            unknown = [k for k in data if not hasattr(instance, k) or k.startswith("_")]
            for key in unknown:
                logger.warning("config.yaml: unrecognised key %r — ignored", key)
            for key, raw in data.items():
                if hasattr(instance, key) and not key.startswith("_"):
                    _set_field(instance, key, raw)
                    sources[key] = f"config {cfg_path}"
            instance._config_file_path = cfg_path

        # --- step 3: env vars ---
        for f in fields(cls):
            if f.name.startswith("_"):
                continue
            env_key = _ENV_PREFIX + f.name.upper()
            val = os.environ.get(env_key)
            if val is not None:
                _set_field(instance, f.name, val)
                sources[f.name] = f"env {env_key}"

        instance._sources = sources
        return instance

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------

    def show(self) -> None:
        """Print effective settings to stdout (for --show-config)."""
        col_w = (20, 52, 30)
        header = (
            f"{'Setting':<{col_w[0]}}  "
            f"{'Effective value':<{col_w[1]}}  "
            f"{'Source':<{col_w[2]}}"
        )
        print(header)
        print("-" * sum(col_w))
        for f in fields(self):
            if f.name.startswith("_"):
                continue
            val = getattr(self, f.name)
            src = self._sources.get(f.name, "default")
            print(f"{f.name:<{col_w[0]}}  {str(val):<{col_w[1]}}  {src:<{col_w[2]}}")
        cfg = self._config_file_path or "(none)"
        print(f"{'config_file':<{col_w[0]}}  {str(cfg):<{col_w[1]}}  {'—':<{col_w[2]}}")

    # ------------------------------------------------------------------
    # Convenience
    # ------------------------------------------------------------------

    def setup_logging(self) -> None:
        """Configure the root logger from settings."""
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        log_file = self.logs_dir / "app.log"

        logging.basicConfig(
            level=getattr(logging, self.log_level.upper(), logging.INFO),
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(log_file),
            ],
        )
        logger.debug("Logging initialised (level=%s, file=%s)", self.log_level, log_file)


# ------------------------------------------------------------------
# Helpers (module-private)
# ------------------------------------------------------------------

def _resolve_config_path(explicit: Path | str | None) -> Path | None:
    if explicit:
        return Path(explicit)
    env = os.environ.get(_ENV_PREFIX + "CONFIG")
    if env:
        return Path(env)
    candidate = _WORKSPACE_ROOT / "config.yaml"
    return candidate if candidate.exists() else None


def _set_field(obj: Any, name: str, raw: Any) -> None:
    """Set a field, preserving the correct Python type."""
    f_type = type(getattr(obj, name))
    if f_type is Path:
        setattr(obj, name, _abs(raw))
    elif f_type is int:
        setattr(obj, name, int(raw))
    else:
        setattr(obj, name, raw)
