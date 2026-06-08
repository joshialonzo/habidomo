# Style Guide

This file defines the coding style conventions for both human and AI contributors to the Habidomo Serverpod and Flutter application.

## General Guidelines
- Keep functions, methods, and widgets small and single-purpose
- Write clear, descriptive names for functions, classes, and variables
- Include documentation comments for public APIs explaining purpose, parameters, and return values
- Use strong typing and null-safety consistently
- Write unit tests for business logic and UI behavior

## Dart & Flutter Formatting
- **Formatter:** `dart format`
- **Linter:** Use `dart analyze` and follow the Dart style guide
- **Imports:** Organize as: Dart SDK → third-party packages → local package imports
- **Naming:**
  - Functions, methods, and variables: `lowerCamelCase`
  - Classes and enums: `UpperCamelCase`
  - Constants: `lowerCamelCase` for fields, `ALL_CAPS_WITH_UNDERSCORES` for top-level constants
  - Private identifiers: prefix with `_`
- **Types:** Use explicit types where helpful and avoid `dynamic` unless necessary

## Flutter UI
- Keep widgets composable and reusable
- Avoid large build methods; split complex screens into small widgets
- Use state management patterns that fit the app size and complexity
- Present clear, accessible labels and error messages
- Keep UI logic separate from backend and domain logic

## Serverpod Backend
- Keep endpoint handlers focused on request validation and orchestration
- Delegate domain logic to service classes or helper modules
- Validate payloads and enforce authorization at the backend boundary
- Use typed request and response models and keep API contracts stable

## Sample Data and Migration
- `local/` may contain sample CSV fixture data for import or migration support
- Do not treat CSV files in `local/` as production storage
- Keep backend data models authoritative for the app schema

## Agent Instructions
*AI Agents must output code adhering strictly to these guidelines. Refactor seamlessly to match this style.*
