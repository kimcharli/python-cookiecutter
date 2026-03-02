# Working Todo List

This document tracks immediate next steps and technical debt for the {{ cookiecutter.project_name }} project.

## 📋 Immediate Next Steps

- [x] Define core domain models in `src/{{ cookiecutter.pkg_name }}/core/models.py`. (Initial stub provided)
- [x] Implement initial CLI commands. (Baseline provided)
- [x] Add first unit tests. (Added test_cli.py and test_web.py)

## � SDD Checklist (Config Consolidation)

- [x] `specs/config.md` drafted (settings table, env vars, resolution order, `--show-config` format)
- [x] `src/{{ cookiecutter.pkg_name }}/core/config.py` — `Settings` dataclass with `Settings.load()`
- [x] `config.yaml` at repository root, fully commented
- [x] `--config` and `--show-config` on CLI entry point
- [ ] No `_WORKSPACE_ROOT` defined outside `config.py` (verify as project grows)
- [ ] Downstream helpers accept paths as parameters, not computing their own

## �🚀 Out of Scope (Current Phase)

- **Dockerization**: Postponed until CLI/Web stability is reached.
