# Contributing

This project is built by a small team during the NASA Space Apps Challenge. Keep changes focused, reviewable, and easy to integrate.

## Git workflow

1. Update your local `main`: `git switch main && git pull --ff-only`.
2. Create a short-lived branch, e.g. `git switch -c feat/mission-selection`.
3. Implement and test one focused change.
4. Commit using the convention below.
5. Push the branch and open a pull request against `main`.
6. Have the other contributor review the PR whenever possible. Merge after checking that the game still runs.

Avoid committing directly to `main` during regular development. Communicate before changing shared files such as `pyproject.toml` or the main game loop.

## Commit convention

We follow [qoomon's Conventional Commits cheatsheet](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13):

```text
<type>(<optional-scope>): <imperative description>
```

Use lowercase, imperative, present-tense descriptions without a trailing period. Keep commits small and coherent.

| Type | Use for |
| --- | --- |
| `feat` | Add or change gameplay or user-facing behavior |
| `fix` | Fix a bug |
| `refactor` | Restructure code without changing behavior |
| `perf` | Improve performance |
| `style` | Formatting-only changes |
| `test` | Add or update tests |
| `docs` | Documentation changes |
| `build` | Dependencies, package configuration, or build tooling |
| `ops` | CI, deployment, or operational configuration |
| `chore` | Maintenance tasks not covered above |

Examples:

```text
feat(mission): add destination selection
feat(terminal): show resource overview
fix(physics): correct fuel mass calculation
test(mission): cover invalid mission choices
docs: document uv setup
build: add rich terminal dependency
ops(ci): run tests on pull requests
```

For breaking changes, use `!` before the colon and explain the impact in a `BREAKING CHANGE:` footer. Reference issues in the optional footer, e.g. `Closes #12`.

## Pull requests

Use the same Conventional Commit format for PR titles. This also makes squash-merge commit history consistent.

Before requesting review:
- Explain **what** changed and **why**.
- Document **how it was tested**.
- Note any known limitations and related issues.
- Ensure `uv sync --locked` and `uv run space-mission-design` work.
- Keep unrelated changes out of the PR.

During the hackathon, prefer small pull requests over large, long-lived branches.

## Dependencies and local environment

Use `uv add` to modify dependencies. Commit both `pyproject.toml` and `uv.lock`. Never commit `.venv/`, local secrets, or temporary files.
