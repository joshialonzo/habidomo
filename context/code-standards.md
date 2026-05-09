# Code Standards

## General

- Keep modules small and single-purpose; separate CLI concerns from backend logic
- Fix root causes, do not layer workarounds; especially important in CSV-based data operations
- Do not mix unrelated concerns in one module (CLI layer, business logic, data access)
- All data access must go through the `shared/` backend; the CLI does not directly touch files

## Python

- Use type hints throughout the project for clarity and IDE support
- Validate input at system boundaries (CLI input and file reading) before processing
- Use descriptive variable and function names; avoid abbreviations except standard conventions
- Keep functions focused on a single responsibility
- Use pathlib for file operations instead of os.path

## CLI Application (`cli/`)

- Use Click or similar framework for command structure and argument parsing
- Each command should be a thin wrapper that calls `shared/` backend functions
- Perform input validation and formatting in CLI layer
- Return clear, user-friendly output messages
- Handle errors gracefully with helpful error messages
- Commands map 1:1 to feature workflows defined in `context/features/`

## Shared Backend (`shared/`)

- Contains all business logic, data models, and utilities
- No direct file I/O; use data access layer for persistence
- Implement validation and business rules in backend modules
- Keep functions pure when possible (no side effects)
- Provide clear interfaces that CLI can easily consume
- Include unit tests for all critical business logic

## Data and Storage (`local/`)

- CSV files are the single source of truth for persisted data
- Each entity type (sections, houses, neighbors, etc.) gets its own CSV file
- CSV headers must match the data model defined in `shared/`
- Maintain referential integrity through careful application logic
- Do not expose file paths to the CLI layer; all access goes through `shared/`
- Implement atomic operations and transaction-like behavior where needed

## File Organization

- **`cli/`** — CLI commands, organized by feature/entity
- **`shared/`** — Data models, business logic, data access layer
- **`shared/models/`** — Data classes and model definitions
- **`shared/services/`** — Business logic and operations
- **`shared/database/`** — Data access layer for CSV operations
- **`local/`** — CSV database files (do not edit directly)
- **`context/`** — Feature specifications and API contracts
- **`scripts/`** — Automation and development utilities

## Testing

- Write unit tests for business logic in `shared/`
- Test data access layer independently of CLI
- Mock file I/O in tests when appropriate
- Use descriptive test names that explain the scenario and expected outcome
