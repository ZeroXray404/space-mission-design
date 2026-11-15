# Space Mission Design

A terminal-based space mission design game developed in Python for the [NASA Space Apps Challenge 2026](https://www.spaceappschallenge.org/2026/challenges/space-mission-design-game/).

The goal is to explore the trade-offs involved in planning a space mission through interactive decisions. The gameplay, mission mechanics, and scientific models are being designed during the hackathon.

> **Status:** Early development — the current entry point is a starter application, not yet a playable game.

## Requirements

- Git
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python package and project manager)
- A terminal (Linux, macOS, or Windows PowerShell)

The project targets **Python 3.12**. `uv` can download a compatible interpreter if you do not already have one.

## Development environment setup

### 1. Install uv

Follow the [official installation instructions](https://docs.astral.sh/uv/getting-started/installation/) for your operating system.

For Linux/macOS, one supported installation method is:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify the installation:

```bash
uv --version
```

### 2. Clone the repository

```bash
git clone https://github.com/ZeroXray404/space-mission-design.git
cd space-mission-design
```

### 3. Install Python and project dependencies

```bash
uv sync
```

This creates a project-local virtual environment (`.venv/`) and installs the dependencies recorded in `uv.lock`. The virtual environment is not committed to Git.

### 4. Run the application

```bash
uv run space-mission-design
```

The application currently runs a startup function and prints startup messages. The messages will evolve as gameplay is implemented.

### 5. Run Python directly (optional)

```bash
uv run python --version
```

You do not need to manually activate `.venv`: `uv run` uses the project environment automatically.

## Development checks

Run lint, formatting, and tests before opening a pull request:

```bash
uv run ruff check
uv run ruff format --check
uv run pytest -qs
```

if ruff finds errors, fix with `uv run ruff format`

The current smoke test calls `main()` and checks that it completes without exceptions. Terminal messages can change freely during development.

GitHub Actions runs these checks on pull requests and pushes to `main`.

## Working with dependencies

Add a runtime dependency:

```bash
uv add package-name
```

After pulling changes from GitHub, synchronize your environment:

```bash
git pull
uv sync
```

Commit changes to `pyproject.toml` and `uv.lock` together. Never commit the `.venv/` directory.

## Project structure

```text
space-mission-design/
├── .github/
│   ├── workflows/
│   │   └── ci.yml            # Automated lint, formatting, and test checks
│   └── pull_request_template.md # Pull request template
├── src/
│   └── space_mission_design/
│       ├── __init__.py        # Application entry point and main menu loop
│       ├── assessment.py      # Mission status and debriefing placeholders
│       ├── game.py            # Mission startup and player role selection
│       ├── interface.py       # Terminal menus and screen helpers
│       ├── mission.py         # Mission class and file-loading placeholders
│       ├── player.py          # Player class with a name and role
│       └── score.py           # Score-tracking placeholders
├── tests/
│   └── test_smoke.py          # Startup smoke test
├── .gitignore
├── .python-version           # Python 3.12
├── CONTRIBUTING.md           # Collaboration workflow and conventions
├── pyproject.toml            # Project metadata and dependencies
├── README.md
└── uv.lock                   # Locked dependencies
```

The structure will evolve as gameplay and additional tests are added.

## Collaboration

We use short-lived feature branches and pull requests targeting `main`. See [CONTRIBUTING.md](CONTRIBUTING.md) for the collaboration workflow, commit conventions, and PR guidelines.

## Challenge

[NASA Space Apps Challenge 2026 — Space Mission Design Game](https://www.spaceappschallenge.org/2026/challenges/space-mission-design-game/)

This is an independent hackathon project and is not an official NASA product.
