# Product Requirements Document (PRD)

## App Overview
**Name**: Real de Dzityá  
**Platforms**: Web (responsive across desktop and mobile)  
**Description**: A condominium management app for the Real de Dzityá residential community. It enables administrators to manage sections, houses, neighbors, payments, and expenses — and to generate financial reports that can be shared instantly via WhatsApp or exported to Google Sheets.

## Target Audience
- **Condominium Administrators**: Primary users. Manage all data and operations.
- **Neighbors (Active & Delinquent)**: View their own house/payment info.
- **Oversight Committee**: Audit financials with read-only access.
- **Security Staff**: (Future) Gate/visitor management.
- **Home Employees**: (Future) Minimal access for clock-in/out.

## User Roles
| Role | Code | Description |
|---|---|---|
| Administrator | `admin` | Full CRUD access to all entities and reports. |
| Active Neighbor | `neighbor_active` | Up to date on payments. Can view own data. |
| Delinquent Neighbor | `neighbor_delinquent` | Has outstanding debts. Restricted access. |
| Oversight Committee | `oversight_committee` | Read-only audit access to all financial data. |
| Security Staff | `security` | (Future) Gate and visitor features only. |
| Home Employee | `employee` | (Future) Minimal access. |

## Core Features

Detailed requirements for each feature are maintained in the [`docs/features/`](./features/) directory. Features are listed below in priority order (build sequence).

### Phase 1: Data Foundation (Admin-First)
- 🔐 [**01 — Authentication**](./features/01_authentication.md): Phone-based sign-in (SMS OTP). Roles assigned by admin.
- 🏘️ [**02 — Sections Management**](./features/02_sections_management.md): CRUD for streets/clusters of houses.
- 🏠 [**03 — Houses Management**](./features/03_houses_management.md): CRUD for lots/properties. Linked to sections.
- 👤 [**04 — Neighbors Management**](./features/04_neighbors_management.md): CRUD for residents. Linked to houses. Phone number as identity.

### Phase 2: Financial Core
- 💰 [**05 — Payments Management**](./features/05_payments_management.md): CRUD for dues received. Linked to neighbors and houses by month.
- 💸 [**06 — Expenses Management**](./features/06_expenses_management.md): CRUD for condominium expenditures by category and month.
- 📊 [**07 — Financial Reports**](./features/07_reports.md): Monthly payments, expenses, and balance reports. Copy-to-clipboard (WhatsApp), Google Sheets export, and future WhatsApp bot delivery.

### Phase 3: Community (Future)
- 🔔 Announcements Board
- 🎫 QR Visitor Passes
- 🗳️ Digital Voting / Polls
- 🚨 SOS / Panic Button

## Success Metrics
- 90%+ of monthly payment records entered within the first week of each month.
- Administrators can generate and share a monthly report in under 30 seconds.
- All financial data auditable by the oversight committee in real-time.
- Neighbor payment collection rate improvement (tracked month-over-month).

## Agent Instructions
*When adding features to this app, first read the relevant feature file in `docs/features/` for full context. Update this PRD if a new feature is added. Refuse to build features that contradict the core purpose defined here unless expressly asked by the user. Always prioritize the Administrator experience first.*
