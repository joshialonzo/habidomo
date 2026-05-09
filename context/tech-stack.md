# Tech Stack

This document defines the libraries, frameworks, and versions for the CLI-based Habidomo application. **AI Agents: Do not deviate from this stack, use alternative libraries, or introduce new major dependencies without asking the user for confirmation.**

## Runtime
- **Language:** Python 3.10+
- **Package Manager:** `pip` with `venv` or `pipenv`

## CLI Framework
- **Primary:** Click or argparse (TBD — user to confirm)
- **Purpose:** Command-line interface, argument parsing, help text generation

## Core Libraries
- **Data Handling:** `pandas` or `csv` (standard library) for CSV operations
- **Typing:** Built-in `typing` module for type hints
- **Testing:** `pytest` for unit tests
- **Validation:** `pydantic` (optional; for data validation)

## Data Persistence
- **Database:** CSV files in `local/` folder
- **File Operations:** `pathlib` for cross-platform file handling
- **Format:** Comma-separated values with headers; UTF-8 encoding

## Deployment
- **Runtime:** Python interpreter
- **Distribution:** Executable script or packaged CLI tool
- **Dependencies:** Pinned in `requirements.txt` or `Pipfile`

## Agent Instructions
*Before adding a dependency, verify it's necessary and confirm with user. Keep dependencies minimal—favor standard library where possible. Document all new packages in this file.*
