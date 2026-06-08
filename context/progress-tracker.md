# Progress Tracker

Update this file after every meaningful implementation change.

## Current Phase

- Phase 1: Serverpod + Flutter architecture alignment

## Current Goal

- Align documentation and repository structure with the current Serverpod backend and Flutter frontend implementation

## Completed

- Updated architecture context to reflect the Serverpod and Flutter application
- Defined folder structure: `habidomo_flutter/` (frontend), `habidomo_server/` (backend), `habidomo_client/` (generated client)
- Migrated documentation content into `context/`: architecture, tech stack, style guide, data model, and feature specs
- Identified `local/` as sample CSV fixture and legacy import data
- Updated contextual references to remove CLI/Python-specific assumptions

## In Progress

- Reviewing remaining context docs for stale folder and runtime references

## Next Up

1. Confirm runtime and deployment instructions for Serverpod and Flutter
2. Update any remaining docs that still reference legacy CLI architecture
3. Ensure feature specs reflect current frontend/backend structure

## Open Questions

- Should `local/` continue to be maintained as sample data only?
- Are there additional Serverpod conventions we should capture in `context/`?

## Architecture Decisions

- **Decision:** Use Flutter frontend with Serverpod backend for cross-platform delivery.
  - **Rationale:** Modern UI, shared client code, and robust backend routing.
- **Decision:** Treat the Serverpod backend as the primary business logic layer.
  - **Rationale:** Centralizes auth, validation, and persistence.
- **Decision:** Keep `local/` as sample/legacy CSV data.
  - **Rationale:** Preserves dataset history without making it the runtime store.
- **Decision:** Consolidate documentation into `context/`.
  - **Rationale:** `context/` is the single source of truth for architecture, workflow, and feature guidance.

## Session Notes

- Repository now centers on Flutter + Serverpod instead of a Python CLI
- Documentation has been updated to reflect the current project shape
- Next session should focus on confirming Serverpod build/run steps and aligning feature docs with the actual app implementation
