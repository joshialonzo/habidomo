# Architecture Context

## Stack

| Layer      | Technology                          | Role                                                                 |
| ---------- | ----------------------------------- | -------------------------------------------------------------------- |
| Frontend   | CLI Application (Python)            | Command-line interface for user interaction                          |
| Backend    | Python modules in `shared/`         | Business logic, data models, and core functionality                 |
| Database   | Local file-based storage in `local/`| CSV files and local data persistence                                |
| Shared     | Python modules                      | Shared models and utilities between CLI and backend                 |

## Directory Structure

- **`cli/`** — CLI frontend application; user-facing command-line interface
- **`shared/`** — Backend logic, business rules, data models, and utilities
- **`local/`** — Database storage; CSV files and local data persistence
- **`context/`** — Documentation and system design artifacts
- **`scripts/`** — Automation utilities

## System Boundaries

- The CLI application (`cli/`) owns user interaction and request dispatch.
- The `shared/` backend module owns all business logic and data operations.
- The `local/` folder manages all data persistence (CSV files).
- No data access happens directly in the CLI; all operations go through the `shared/` backend.

## Storage Model

- **Local Database:** CSV files in `local/` store sections, houses, neighbors, payments, expenses, and users.
- **File Format:** Structured CSV with headers matching the data model.
- **Data Access:** All database operations are performed through the `shared/` backend module.

## Auth and Access Model

- Authentication is managed through the `shared/` backend.
- Each user is identified by a phone number and a role.
- Access control is enforced by the `shared/` backend logic and CSV relationships.

## Invariants

1. Business logic must remain in the `shared/` backend; the CLI is only an interface.
2. The CLI application does not directly access or modify data; all operations go through `shared/` modules.
3. Shared data models live in `shared/` to avoid duplication between CLI and backend logic.
4. The `local/` folder contains the single source of truth for all persisted data.
5. CSV files must maintain referential integrity through careful application logic in `shared/`.
