# SDD Practice: Centralised Global Settings

**Status:** Adopted

---

## Problem

Python CLI packages that grow beyond a single file accumulate module-level
constants for paths, ports, and other runtime knobs.
These constants scatter across multiple modules, each independently computing
`_WORKSPACE_ROOT = Path(__file__).parent.parent.parent` and hardcoding
subdirectory names.  The result:

- No single place to see what can be changed
- Overriding a path requires editing source or passing many CLI args
- New contributors cannot discover what is configurable without reading every file
- Relative paths resolve inconsistently depending on `Path()` vs `CWD`

---

## Solution

Centralise all global settings in `src/{{ cookiecutter.pkg_name }}/core/config.py`
and expose them through three surfaces:

1. **A user-editable `config.yaml`** at the project root
2. **Environment variables** using the `{{ cookiecutter.pkg_name | upper }}_` prefix
3. **A `--show-config` flag** on every CLI entry point that prints a
   formatted table of the effective values and their sources

### Resolution order (highest priority wins)

```
CLI arg  >  env var  >  config.yaml  >  compiled-in default
```

---

## Spec First

Before writing any code, draft `specs/config.md` to define:

- **Settings table** — every field, its default, its env var name, and what it controls
- **Derived paths** — paths computed from settings but not independently settable;
  trace each to its parent setting
- **Config file format** — exact YAML key names; ship the file pre-populated with
  every key commented out at its default value
- **Resolution order** — written explicitly so it becomes a contract
- **`--show-config` output format** — column headers, value format (always absolute
  paths), and the exact `Source` strings (`default`, `config <path>`,
  `env <VAR>`, `arg --<flag>`)

---

## Implementation

### `src/{{ cookiecutter.pkg_name }}/core/config.py`

```python
"""Global settings for {{ cookiecutter.pkg_name }}.

Resolution order (highest wins):
    CLI arg  >  env var  >  config.yaml  >  compiled-in default
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Any

import yaml

_WORKSPACE_ROOT = Path(__file__).parent.parent.parent


def _abs(p: Path | str) -> Path:
    p = Path(p)
    return p if p.is_absolute() else _WORKSPACE_ROOT / p


@dataclass
class Settings:
    input_dir:  Path = field(default_factory=lambda: _abs("data/input"))
    output_dir: Path = field(default_factory=lambda: _abs("data/output"))
    logs_dir:   Path = field(default_factory=lambda: _abs("data/logs"))
    web_port:   int  = 8000

    _config_file_path: Path | None = field(default=None, repr=False, compare=False)
    _sources: dict[str, str]       = field(default_factory=dict, repr=False, compare=False)

    @classmethod
    def load(cls, config_path: Path | str | None = None) -> "Settings":
        instance = cls()
        sources = {f.name: "default" for f in fields(cls) if not f.name.startswith("_")}

        cfg = _resolve_config_path(config_path)
        if cfg and cfg.exists():
            data = yaml.safe_load(cfg.read_text()) or {}
            for key, raw in data.items():
                if hasattr(instance, key) and not key.startswith("_"):
                    _set_field(instance, key, raw)
                    sources[key] = f"config {cfg}"
            instance._config_file_path = cfg

        ENV_PREFIX = "{{ cookiecutter.pkg_name | upper }}_"
        for f in fields(cls):
            if f.name.startswith("_"):
                continue
            val = os.environ.get(ENV_PREFIX + f.name.upper())
            if val is not None:
                _set_field(instance, f.name, val)
                sources[f.name] = f"env {ENV_PREFIX + f.name.upper()}"

        instance._sources = sources
        return instance

    def show(self) -> None:
        col_w = (20, 50, 30)
        header = f"{'Setting':<{col_w[0]}}  {'Effective value':<{col_w[1]}}  {'Source':<{col_w[2]}}"
        print(header)
        print("-" * sum(col_w))
        for f in fields(self):
            if f.name.startswith("_"):
                continue
            print(f"{f.name:<{col_w[0]}}  {str(getattr(self, f.name)):<{col_w[1]}}  {self._sources.get(f.name, 'default'):<{col_w[2]}}")
        print(f"{'config_file':<{col_w[0]}}  {str(self._config_file_path or '(none)'):<{col_w[1]}}  {'—':<{col_w[2]}}")


def _resolve_config_path(explicit: Path | str | None) -> Path | None:
    if explicit:
        return Path(explicit)
    env = os.environ.get("{{ cookiecutter.pkg_name | upper }}_CONFIG")
    if env:
        return Path(env)
    candidate = _WORKSPACE_ROOT / "config.yaml"
    return candidate if candidate.exists() else None


def _set_field(obj: Any, name: str, raw: Any) -> None:
    f_type = type(getattr(obj, name))
    if f_type is Path:
        setattr(obj, name, _abs(raw))
    elif f_type is int:
        setattr(obj, name, int(raw))
    else:
        setattr(obj, name, raw)
```

### `config.yaml` (shipped at repository root)

```yaml
# {{ cookiecutter.project_name }} global configuration
# All paths are relative to the repository root unless absolute.
# Set {{ cookiecutter.pkg_name | upper }}_CONFIG=/path/to/config.yaml to load a custom file.
# Uncomment and edit any line to override the compiled-in default.

# input_dir:  data/input
# output_dir: data/output
# logs_dir:   data/logs
# web_port:   8000
```

### Wiring into CLI entry points

```python
settings = Settings.load(config_path=args.config)

if args.output_dir:
    settings.output_dir = _abs(args.output_dir)
    settings._sources["output_dir"] = "arg --output-dir"

if args.show_config:
    settings.show()
    raise SystemExit(0)
```

**Key rule:** after `Settings.load()`, pass the instance down to all helpers.
No helper module computes `Path(__file__).parent...` or reads env vars directly.

---

## Updating downstream modules

```python
# Before
_WORKSPACE_ROOT = Path(__file__).parent.parent.parent
def get_output(name: str) -> Path:
    return _WORKSPACE_ROOT / "data" / "output" / name

# After
def get_output(name: str, output_dir: Path) -> Path:
    return output_dir / name
```

Callers pass `settings.output_dir`.  This also makes functions trivially
testable with any temporary directory.

---

## Checklist

- [ ] `specs/config.md` drafted before any implementation
- [ ] `src/{{ cookiecutter.pkg_name }}/core/config.py` with `Settings` dataclass and `Settings.load()`
- [ ] `config.yaml` at repository root, fully commented
- [ ] `--config` and `--show-config` on every CLI entry point
- [ ] No `_WORKSPACE_ROOT` defined outside `config.py`
- [ ] Downstream helpers accept paths as parameters
- [ ] `{{ cookiecutter.pkg_name | upper }}_` env prefix documented in `config.yaml` comments

---

## Anti-patterns to Avoid

| Anti-pattern | Preferred alternative |
|---|---|
| `DEFAULT_X = Path(__file__).parent…` in multiple files | `Settings.x` in `config.py` only |
| Bare `Path("data/output")` (CWD-relative) | `_abs("data/output")` anchored to workspace root |
| One env var per constant with no shared prefix | `{{ cookiecutter.pkg_name | upper }}_SETTING_NAME` prefix |
| Silently ignoring unknown keys in `config.yaml` | Log a warning for unrecognised keys |
| Printing relative paths in `--show-config` | Always resolve to absolute |

---

## Prior Art & Terminology

This practice combines several well-known concepts:

| Term | What it maps to here |
|---|---|
| **[12-Factor App — Factor III (Config)](https://12factor.net/config)** | Store config in the environment; never hardcode in source. The `env var > default` layer is straight from this. |
| **Layered / Cascading Configuration** | The full `CLI arg > env var > config.yaml > default` resolution order. |
| **Settings Object pattern** | One typed object (`Settings`) holds all settings and is passed down to all callers — no module reads env vars or computes paths independently. |
| **Project-relative paths / workspace-root anchoring** | All relative paths are resolved from a fixed project root, not `CWD`. Used by `pytest` (`rootdir`), `cargo`, `go`, etc. |
| **Effective configuration display** | A `--show-config` flag that prints resolved values *with their source*. Equivalent to `git config --list --show-origin` or Ansible's variable precedence output. |

**Standard library**: [`pydantic-settings`](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
is the canonical Python implementation of this pattern.
The hand-rolled `Settings` class here is intentionally minimal and
dependency-light; migrate to `pydantic-settings` if validation,
nested models, or secret management become requirements.
