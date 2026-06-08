# Architecture Context

## Stack

| Layer        | Technology                             | Role                                                                 |
| ------------ | -------------------------------------- | -------------------------------------------------------------------- |
| Frontend     | Flutter app in `habidomo_flutter/`     | Cross-platform mobile, desktop, and web user interface               |
| Backend      | Serverpod server in `habidomo_server/` | API endpoints, authentication, business logic, and persistence       |
| Client       | `habidomo_client/`                     | Generated typed Dart client package used by the Flutter frontend     |
| Data         | PostgreSQL via Serverpod               | Persistent relational storage for application entities              |
| Documentation| `context/`                             | Architecture, feature specs, tech stack, and workflow guidance       |

## Directory Structure

- **`habidomo_flutter/`** — Flutter frontend application and platform-specific runners
- **`habidomo_server/`** — Serverpod backend server, endpoint definitions, and config
- **`habidomo_client/`** — Generated Serverpod client package for typed server access
- **`local/`** — Sample CSV fixture data and legacy import files
- **`context/`** — Documentation and design artifacts

## System Boundaries

- The Flutter application (`habidomo_flutter/`) owns user interaction and sends requests via the typed Serverpod client.
- The Serverpod backend (`habidomo_server/`) owns business logic, authentication, authorization, and data persistence.
- The generated client package (`habidomo_client/`) centralizes the typed interface between frontend and backend.
- The `local/` folder is used for sample or legacy CSV data and is not the primary runtime datastore.

## Storage Model

- **Primary Database:** PostgreSQL managed by Serverpod.
- **Data Access:** All persistent operations are routed through Serverpod endpoints in `habidomo_server/`.
- **Sample Data:** `local/` contains CSV source data for import, analytics, or migration support.

## Auth and Access Model

- Authentication is handled by Serverpod and configured under `habidomo_server/config/`.
- Each user is identified by credentials managed through the backend.
- Access control is enforced by backend logic and Serverpod endpoint policies.

## Invariants

1. Business logic must remain in `habidomo_server/` and not be duplicated in the frontend.
2. The Flutter frontend does not directly access the database; it communicates through Serverpod APIs.
3. The generated client package (`habidomo_client/`) provides a single typed interface for server communication.
4. Legacy CSV data in `local/` is treated as sample or migration material, not production storage.
5. Backend data models are authoritative and drive the API contract for the frontend.
