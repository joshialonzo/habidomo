# Progress Tracker

Update this file after every meaningful implementation
change.

## Current Phase

- Architecture planning and documentation consolidation

## Current Goal

- Establish the project structure with CLI frontend, shared backend, and local database storage.
- Centralize implementation guidance in `context/`.

## Completed

- Updated architecture context to reflect CLI-based application
- Defined folder structure: `cli/` (frontend), `shared/` (backend), `local/` (database)
- Established data model to use CSV files for persistence
- Migrated documentation content into `context/`: architecture, tech stack, style guide, data model, and feature specs
- Created context/data-model.md to document data structures and CSV schemas
- Updated context/ui-context.md for CLI output formatting (no longer web UI focused)

## In Progress

- None yet.

## Next Up

1. Scaffold the CLI application structure in `cli/`
2. Create shared backend modules in `shared/` with data models and business logic
3. Set up CSV-based database schema in `local/`
4. Implement data access layer connecting CLI to shared backend
5. Create initial CLI commands for core workflows

## Open Questions

- What CLI framework should be used? (click, argparse, etc.)
- How should CSV files be structured for relationships between entities?
- Should there be data validation at the CLI level or only in `shared/`?

## Architecture Decisions

- **Decision:** Use CLI instead of web application for better local development and deployment flexibility.
  - **Rationale:** Simplifies deployment, reduces infrastructure requirements, better suited for local team management.
- **Decision:** Use CSV files instead of PostgreSQL for initial implementation.
  - **Rationale:** Easier to set up locally, files are portable, suitable for MVP phase.
- **Decision:** Separate concerns into `cli/`, `shared/`, and `local/` folders.
  - **Rationale:** Clear boundaries between user interface, business logic, and data storage; makes testing and maintenance easier.
- **Decision:** Consolidate documentation into `context/` only.
  - **Rationale:** `context/` is the single source of truth for AI workflow, implementation guidance, and feature specs.

## Session Notes

- User initiated shift from Flask web UI to CLI application
- New structure: CLI (frontend) → Shared (backend) → Local CSV database
- Migrated documentation: `context/` now reflects CLI architecture and feature guidance
- Created separate data-model.md in context/ for data structure reference
- Next session should start with scaffolding the project structure
