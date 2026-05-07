# Feature 05: Payments Management (CRUD)

## Status
- **Current State**: Planned
- **Priority**: 🔴 Critical (Core Financial)
- **Frontend Target**: React / Next.js (`/apps/web`) + React Native (`/apps/mobile`)
- **Backend Target**: AWS CDK / Lambda / DynamoDB (`/infra`)

## Overview
A **Payment** records money received from a neighbor for their condominium dues. Payments are associated with both a **neighbor** and a **house**, and are tagged to a specific **month/year** period.

## User Stories
1. As an administrator, I want to register a payment from a neighbor, specifying the amount, date, and the month it covers.
2. As an administrator, I want to view all payments for a given month, with totals.
3. As an administrator, I want to edit a payment record if I made a data entry mistake.
4. As an administrator, I want to delete an erroneous payment (with confirmation).
5. As an administrator, I want to quickly see which houses have NOT paid for a given month.

## Data Model
```json
{
  "payment_id": "string (auto-generated)",
  "house_id": "string (FK to houses)",
  "neighbor_id": "string (FK to neighbors — who made the payment)",
  "amount": "number (in MXN)",
  "period_month": "number (1-12)",
  "period_year": "number (e.g., 2026)",
  "payment_date": "timestamp (when the money was received)",
  "payment_method": "string ('cash' | 'transfer' | 'deposit' | 'other')",
  "receipt_url": "string (optional, link to uploaded photo of receipt)",
  "notes": "string (optional)",
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "created_by": "string (admin UID who recorded it)"
}
```

## UI Screens (Administrator)
1. **Payments List**: Filterable by month/year, section, and house. Sortable by date. Shows total collected at the top.
2. **Register Payment**: Form with neighbor/house selector, amount, method dropdown, period picker, and optional receipt photo upload.
3. **Edit Payment**: Same form, pre-populated.
4. **Unpaid Houses View**: For a selected month, shows a list of houses that do NOT have a payment record. This is crucial for follow-up.

## Validation Rules
- Amount must be greater than 0.
- Period (month/year) is required.
- A house should not have duplicate payments for the same period (warn but allow — some might pay extra).

## Access Control
| Role | Create | Read | Update | Delete |
|---|---|---|---|---|
| `admin` | ✅ | ✅ | ✅ | ✅ |
| `oversight_committee` | ❌ | ✅ | ❌ | ❌ |
| `neighbor_*` | ❌ | Own payments only | ❌ | ❌ |
