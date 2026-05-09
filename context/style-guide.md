# Style Guide

This file defines the coding style conventions for both human and AI contributors to the Habidomo CLI application.

## General Guidelines
- Keep functions small and single-purpose
- Write clear, descriptive names for functions, classes, and variables
- Include docstrings for public functions explaining purpose, parameters, and return values
- All code must use type hints for clarity
- Write unit tests for business logic in `shared/`

## Python Formatting & Structure
- **Formatter:** Black (enforced via `black --line-length 100`)
- **Linter:** Follow PEP 8 with pylint or flake8
- **Imports:** Organize as: standard library → third-party → local imports
- **Naming:**
  - Functions and variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`
  - Private methods: prefix with `_`
- **Type Hints:** Use throughout; avoid `Any` unless absolutely necessary

## CLI Commands (`cli/`)
- Command names: short, descriptive, `lowercase`
- Arguments: descriptive names, use `--flag` format
- Output: Clear, concise messages; use prefixes for success/error/warning
- Always include help text via `--help`

## Shared Backend (`shared/`)
- Keep modules focused on a single responsibility
- Move business logic out of CLI commands into service functions
- Write docstrings explaining business rules and edge cases
- Validate data at system boundaries (CLI input and file reading)

## CSV Data Format
- Headers: `snake_case`, no spaces
- Values: UTF-8 encoded, quoted if containing commas
- Column names in CSV files must match corresponding model definitions in `shared/models/`

## Agent Instructions
*AI Agents must output code adhering strictly to these guidelines. Refactor seamlessly to match this style.*
