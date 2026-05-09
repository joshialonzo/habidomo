# Habidomo

Manager for a Condominio.

## Folder Structure

This repository is organized with a CLI frontend, shared backend logic, and local database storage:

- **`cli/`**: CLI application for user interaction; entry point for all user-facing commands.
- **`shared/`**: Backend business logic, data models, and utilities; implements core functionality.
- **`local/`**: Database storage; CSV files containing application data.
- **`context/`**: Project guidance, architecture, feature specs, and workflow rules.
- **`scripts/`**: Utility scripts for local development and automation.

## Running the Application

For instructions on how to run, build, and deploy the application, see the documentation in `context/` and the CLI setup guide once the application is scaffolded.

## Documentation

Project-level documentation lives in the [`context/`](./context/) directory:

- 📋 [**PRD**](./context/project-overview.md) — What we are building, target audience, roles, and feature index.
- 🏗️ [**Architecture**](./context/architecture.md) — How the frontend, backend, and database connect.
- 🧰 [**Tech Stack**](./context/tech-stack.md) — Approved frameworks, libraries, and versions.
- 🎨 [**Style Guide**](./context/style-guide.md) — Coding conventions for CLI and Python.
- 🔌 [**Data Model**](./context/data-model.md) — CSV schemas and data model definitions.

### Feature Specs

Individual feature requirements are in [`context/features/`](./context/features/):

- 🔐 [Authentication](./context/features/01_authentication.md)
- 🏘️ [Sections Management](./context/features/02_sections_management.md)
- 🏠 [Houses Management](./context/features/03_houses_management.md)
- 👤 [Neighbors Management](./context/features/04_neighbors_management.md)
- 💰 [Payments Management](./context/features/05_payments_management.md)
- 💸 [Expenses Management](./context/features/06_expenses_management.md)
- 📊 [Financial Reports](./context/features/07_reports.md)
