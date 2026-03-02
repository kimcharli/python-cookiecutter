# Spec-Driven Development (SDD)

This project follows **Spec-Driven Development (SDD)**: every non-trivial
implementation decision starts with a written spec that captures intent,
constraints, and the observable contract *before* any code is written.

## Why SDD?

- Keeps intent and implementation in sync
- Makes review easier — reviewers can check code against the spec
- Produces a permanent record of *why* choices were made
- Forces clarity before committing to an approach

## Resolution Order (applies to all configurable surfaces)

```
CLI arg  >  env var  >  config file  >  compiled-in default
```

Write this order down in every spec that defines configurable behavior.

---

## Practices

| Practice | Document | Status |
|---|---|---|
| Centralised global settings | [config-consolidation.md](config-consolidation.md) | Adopted |

---

## How to Add a New Practice

1. Create a Markdown file in `docs/sdd/`.
2. Use the structure: **Problem → Solution → Spec First → Implementation → Checklist → Anti-patterns**.
3. Add a row to the table above.
4. Link from [docs/README.md](../README.md).
