# Real de Dzityá

Manager for the Real de Dzityá Condominio.

## Folder Structure

This repository is organized to support a modern web frontend, scalable backend, and agentic coding workflows ("vibe-coding"):

- **/frontend/**: The React / Next.js application for a responsive web client.
- **/backend/**: The Flask backend with PostgreSQL for API and data storage.
- **/docs/**: Markdown documentation for project parameters, keeping developers and AI coding agents aligned (includes PRD, tech stack, and API agreements).
- **/scripts/**: Utility or bash scripts for launching local servers, migrations, and deployment automation.

## Running the Environments

For instructions on how to run, build, and deploy specific parts of the stack, see the dedicated README inside the backend folder. Frontend setup documentation will be added once the React/Next.js app is scaffolded.

- 🐍 [**Backend / Flask API Instructions**](./backend/README.md)

## Documentation

Project-level documentation lives in the [`docs/`](./docs/) directory:

- 📋 [**PRD (Product Requirements)**](./docs/PRD.md) — What we are building, target audience, roles, and feature index.
- 🏗️ [**Architecture**](./docs/ARCHITECTURE.md) — How the frontend, backend, and database connect.
- 🧰 [**Tech Stack**](./docs/TECH_STACK.md) — Approved frameworks, libraries, and versions.
- 🎨 [**Style Guide**](./docs/STYLE_GUIDE.md) — Coding conventions for TypeScript, React, and Python.
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
