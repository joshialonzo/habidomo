# Habidomo — Condominium Management App

## Overview

Habidomo is a condominium management application that enables administrators to manage sections, houses, neighbors, payments, and expenses — and to generate financial reports that can be shared instantly. The current implementation uses a Flutter frontend and a Serverpod backend for a modern cross-platform user experience.

## Goals

1. Provide administrators with a fast, reliable way to manage condominium data.
2. Automate financial reporting and enable shareable output for committees.
3. Maintain accurate, auditable financial records.
4. Support payment collection workflow with clear neighbor payment status tracking.

## Core User Flow

1. Administrator opens the Flutter application.
2. Administrator authenticates through the Serverpod backend.
3. Administrator performs data management operations (add sections/houses/neighbors, log payments/expenses).
4. Administrator generates monthly financial reports.
5. Administrator exports or shares reports through the app.

## Features

### Phase 1: Data Foundation (Admin-First)

- **Authentication**: Backend-managed sign-in with secure credential handling.
- **Sections Management**: CRUD for streets/clusters of houses.
- **Houses Management**: CRUD for lots/properties. Linked to sections.
- **Neighbors Management**: CRUD for residents. Linked to houses.

### Phase 2: Financial Core

- **Payments Management**: CRUD for dues received. Linked to neighbors and houses by month.
- **Expenses Management**: CRUD for condominium expenditures by category and month.
- **Financial Reports**: Monthly payments, expenses, and balance reports. Export options and sharing workflow.

### Phase 3: Community (Future)

- Announcements Board
- Visitor management
- Digital voting / polls

## Scope

### In Scope

- Flutter-based frontend for administrators
- Serverpod backend for API, authentication, and persistence
- Core CRUD operations for sections, houses, neighbors, payments, and expenses
- Monthly financial report generation
- Report export and sharing integration
- Role-based access control

### Out of Scope

- Native mobile apps separate from Flutter
- Real-time notifications
- Security staff gate management (Phase 3+)
- Home employee time tracking (Phase 3+)
- Cloud sync beyond the Serverpod-hosted backend for MVP

## Success Criteria

1. Administrators can perform CRUD operations on all core entities through the Flutter app.
2. Administrators can generate a monthly financial report in under 30 seconds.
3. All financial data is auditable and traceable.
4. The application can be run locally with the Serverpod backend.
5. Payment collection workflow is clear and efficient.
