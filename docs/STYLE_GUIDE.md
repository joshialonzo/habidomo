# Style Guide

This file defines the coding style conventions for both human and AI contributors.

## General Guidelines
- Keep functions small and single-purpose.
- All code must be strongly typed and explicit in TypeScript.
- Write brief documentation for complex functions.

## Frontend / JavaScript
- **Formatting**: Keep HTML, CSS, and JS readable and consistent. Use a formatter such as Prettier for frontend assets when available.
- **Structure**: Keep vanilla JS modules small and reusable. Prefer descriptive function names and clear DOM update patterns.
- **Typing**: Use explicit validation for user input in JavaScript and rely on backend validation for business rules.
- **File Naming**: Use `kebab-case` for static asset filenames and `camelCase` for JavaScript modules.

## Python / Flask
- **Formatting**: Follow PEP 8 and use a formatter such as `black` for Python code.
- **Structure**: Keep Flask route handlers focused and move business logic into reusable service modules.
- **Typing**: Use type hints where it improves clarity. Avoid `Any` unless necessary.

## JSON / Relational Data
- Database column names should be `snake_case` in PostgreSQL.

## Agent Instructions
*AI Agents must output code that adheres strictly to these guidelines. Refactor code seamlessly to match this style.*
- Database document keys should be `camelCase`.

## Agent Instructions
*AI Agents must output code that adheres strictly to these guidelines. Refactor code seamlessly to match this style.*
