# Habidomo

Manager for a Condominio.

## Folder Structure

This repository is organized to support a Flask backend, vanilla JavaScript frontend assets, and documentation:

- **Backend:** Flask application that serves HTML, CSS, and vanilla JS from static assets.
- **/docs/**: Markdown documentation for project parameters, keeping developers and AI coding agents aligned.
- **/scripts/**: Utility scripts for local development and deployment automation.

## Running the Environments

For instructions on how to run, build, and deploy the application, see the documentation in `docs/` and the Flask backend guide once the backend scaffold is available.

## Documentation

Project-level documentation lives in the [`docs/`](./docs/) directory:

- 📋 [**PRD (Product Requirements)**](./docs/PRD.md) — What we are building, target audience, roles, and feature index.
- 🏗️ [**Architecture**](./docs/ARCHITECTURE.md) — How the frontend, backend, and database connect.
- 🧰 [**Tech Stack**](./docs/TECH_STACK.md) — Approved frameworks, libraries, and versions.
- 🎨 [**Style Guide**](./docs/STYLE_GUIDE.md) — Coding conventions for Flask and vanilla JavaScript.
- 🔌 [**API Contracts**](./docs/API_CONTRACTS.md) — Database schemas and backend endpoint definitions.

### Feature Specs

Individual feature requirements are in [`docs/features/`](./docs/features/):

- 🔐 [Authentication](./docs/features/01_authentication.md)
- 🏘️ [Sections Management](./docs/features/02_sections_management.md)
- 🏠 [Houses Management](./docs/features/03_houses_management.md)
- 👤 [Neighbors Management](./docs/features/04_neighbors_management.md)
- 💰 [Payments Management](./docs/features/05_payments_management.md)
- 💸 [Expenses Management](./docs/features/06_expenses_management.md)
- 📊 [Financial Reports](./docs/features/07_reports.md)
