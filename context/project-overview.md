# Habidomo — Condominium Management CLI

## Overview

Habidomo is a condominium management application that enables administrators to manage sections, houses, neighbors, payments, and expenses — and to generate financial reports that can be shared instantly via WhatsApp or exported to Google Sheets. The application is built as a local CLI tool for ease of deployment and management on local infrastructure.

## Goals

1. Provide administrators with a fast, reliable way to manage all condominium data without cloud dependencies
2. Automate financial reporting and enable instant sharing of reports via WhatsApp
3. Maintain accurate, auditable financial records for oversight committees
4. Support payment collection workflow with clear neighbor payment status tracking

## Core User Flow

1. Administrator starts the CLI application
2. Administrator authenticates with phone number and OTP
3. Administrator performs data management operations (add sections/houses/neighbors, log payments/expenses)
4. Administrator generates monthly financial reports
5. Administrator exports or shares reports via WhatsApp or Google Sheets

## Features

### Phase 1: Data Foundation (Admin-First)

- **Authentication**: Phone-based sign-in with OTP. Roles assigned by admin.
- **Sections Management**: CRUD for streets/clusters of houses.
- **Houses Management**: CRUD for lots/properties. Linked to sections.
- **Neighbors Management**: CRUD for residents. Linked to houses. Phone number as identity.

### Phase 2: Financial Core

- **Payments Management**: CRUD for dues received. Linked to neighbors and houses by month.
- **Expenses Management**: CRUD for condominium expenditures by category and month.
- **Financial Reports**: Monthly payments, expenses, and balance reports. Copy-to-clipboard (WhatsApp), Google Sheets export.

### Phase 3: Community (Future)

- Announcements Board
- QR Visitor Passes
- Digital Voting / Polls

## Scope

### In Scope

- CLI-based interface for administrators
- Local CSV-based data persistence
- Core CRUD operations for sections, houses, neighbors, payments, and expenses
- Monthly financial report generation
- Report export and sharing integration
- Role-based access control (admin and read-only roles)

### Out of Scope

- Mobile app (separate project)
- Real-time notifications
- Security staff gate management (Phase 3+)
- Home employee time tracking (Phase 3+)
- Cloud synchronization (MVP phase uses local storage only)

## Success Criteria

1. Administrators can perform CRUD operations on all core entities via CLI commands
2. Administrators can generate a monthly financial report in under 30 seconds
3. All financial data is auditable and traceable
4. The application can be deployed and run locally without external dependencies
5. Payment collection workflow is clear and efficient (delinquency tracking)
