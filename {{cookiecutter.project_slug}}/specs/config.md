# Settings Spec — {{ cookiecutter.project_name }}

**Status:** Draft
**Owner:** {{ cookiecutter.author }}

> This spec must be written (or updated) *before* any implementation change
> that adds, renames, or removes a setting.
> See [docs/sdd/config-consolidation.md](../docs/sdd/config-consolidation.md).

---

## Settings Table

| Setting | Default | Env var | What it controls |
|---|---|---|---|
| `input_dir` | `data/input` | `{{ cookiecutter.pkg_name | upper }}_INPUT_DIR` | Root directory for input files |
| `output_dir` | `data/output` | `{{ cookiecutter.pkg_name | upper }}_OUTPUT_DIR` | Root directory for output files |
| `logs_dir` | `data/logs` | `{{ cookiecutter.pkg_name | upper }}_LOGS_DIR` | Directory for log files |
| `log_level` | `INFO` | `{{ cookiecutter.pkg_name | upper }}_LOG_LEVEL` | Python logging level |
| `web_port` | `8000` | `{{ cookiecutter.pkg_name | upper }}_WEB_PORT` | Port for the web dashboard |

---

## Derived Paths

| Derived value | Expression | Parent setting |
|---|---|---|
| App log file | `logs_dir / "app.log"` | `logs_dir` |

---

## Config File Format

File: `config.yaml` at the repository root.

All paths are relative to the repository root unless absolute.

```yaml
# input_dir:  data/input
# output_dir: data/output
# logs_dir:   data/logs
# log_level:  INFO
# web_port:   8000
```

---

## Resolution Order

```
CLI arg  >  env var  >  config.yaml  >  compiled-in default
```

---

## `--show-config` Output Format

Columns: `Setting` (20), `Effective value` (52), `Source` (30).

`Source` values:
- `default` — compiled-in default
- `config <absolute_path>` — loaded from config.yaml
- `env {{ cookiecutter.pkg_name | upper }}_<NAME>` — overridden via environment variable
- `arg --<flag>` — overridden via CLI argument

All path values are printed as absolute paths.
