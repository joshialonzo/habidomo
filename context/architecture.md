# Architecture Context

## Stack

| Layer      | Technology                          | Role                                                                 |
| ---------- | ----------------------------------- | -------------------------------------------------------------------- |
| Framework  | Flask + HTML/CSS/JavaScript         | Backend-driven web UI with vanilla JS static assets                  |
| API        | Flask routes                        | Request routing, business logic, authentication, and integrations    |
| Database   | PostgreSQL                          | Relational storage for app data                                     |
| Shared     | Python / JavaScript modules         | Shared models and utilities between backend and frontend            |

## System Boundaries

- The Flask backend owns the web UI and API.
- `/docs` contains documentation and system design artifacts.
- `/scripts` contains automation utilities.

## Storage Model

- **Relational Database:** PostgreSQL stores sections, houses, neighbors, payments, expenses, and users.
- **Blob/File Storage:** Receipt images or attachments may be stored on disk or in external blob storage as needed.

## Auth and Access Model

- Authentication is managed through the Flask backend.
- Each user is identified by a phone number and a role.
- Access control is enforced by the Flask backend and database relationships.

## Invariants

1. Business logic should remain in the backend and persist state in PostgreSQL.
2. The Flask application owns request handling and frontend delivery.
3. Shared models live in common modules to avoid duplication across UI and backend.
4. The browser-facing UI does not access the database directly; all data access goes through Flask routes.
