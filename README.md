# Habidomo

Manager for a Condominio.

## Folder Structure

This repository is organized around a Serverpod backend, a Flutter frontend, and a shared Dart client package:

- **`habidomo_flutter/`**: Flutter application for mobile, desktop, and web.
- **`habidomo_server/`**: Serverpod backend, API endpoints, authentication, and deployment configuration.
- **`habidomo_client/`**: Generated Serverpod client package used by the Flutter app.
- **`local/`**: Sample CSV fixture data and legacy import files.
- **`context/`**: Project guidance, architecture, feature specs, and workflow rules.

## Running the Application

See the service-specific documentation for the current setup:

- `habidomo_flutter/README.md` — Flutter app and client runtime
- `habidomo_server/README.md` — Serverpod backend and local development
- `context/` — architecture, tech stack, and feature guidance

## Documentation

Project-level documentation lives in the [`context/`](./context/) directory:

- 📋 [**PRD**](./context/project-overview.md) — What we are building, target audience, roles, and feature index.
- 🏗️ [**Architecture**](./context/architecture.md) — How the frontend, backend, and data layers connect.
- 🧰 [**Tech Stack**](./context/tech-stack.md) — Approved frameworks, libraries, and versions.
- 🎨 [**Style Guide**](./context/style-guide.md) — Coding conventions for Flutter and Serverpod.
- 🔌 [**Data Model**](./context/data-model.md) — Data schemas and integration guidance.

### Feature Specs

Individual feature requirements are in [`context/features/`](./context/features/):

- 🔐 [Authentication](./context/features/01_authentication.md)
- 🏘️ [Sections Management](./context/features/02_sections_management.md)
- 🏠 [Houses Management](./context/features/03_houses_management.md)
- 👤 [Neighbors Management](./context/features/04_neighbors_management.md)
- 💰 [Payments Management](./context/features/05_payments_management.md)
- 💸 [Expenses Management](./context/features/06_expenses_management.md)
- 📊 [Financial Reports](./context/features/07_reports.md)
