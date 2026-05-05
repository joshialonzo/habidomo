# System Architecture

## Overview
This application uses a federated architecture separating the client app from the backend and database layers.

### 1. Frontend (`/frontend`)
- **Framework**: React / Next.js
- **Platforms**: Web (responsive desktop and mobile)
- **Role**: Presentation, user interaction, client-side state management.

### 2. Backend (`/backend`)
- **Technology**: Python / Flask
- **Database**: PostgreSQL
- **Role**: Core data storage, business logic, REST API, authentication, reporting, and integrations.

### 3. Data Layer
- **Data Store**: PostgreSQL
- **Role**: Persist relational data for sections, houses, neighbors, payments, expenses, and users.

## Data Flow
* [Example: "The frontend calls Flask REST endpoints. The backend reads and writes PostgreSQL tables. For heavy reports, the backend queries payments and expenses and returns a computed summary."]*

## Agent Instructions
*When suggesting architectural changes, please review this document to ensure consistency with the master plan. If a change modifies this flow, update this document.*
