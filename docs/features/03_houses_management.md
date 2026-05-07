# Feature 03: Houses Management (CRUD)

## Status
- **Current State**: Planned
- **Priority**: 🔴 Critical (Data Foundation)
- **Frontend Target**: React / Next.js (`/apps/web`) + React Native (`/apps/mobile`)
- **Backend Target**: AWS CDK / Lambda / DynamoDB (`/infra`)

## Overview
A **House** represents a physical property (lot) within the condominium. Each house belongs to exactly one Section and can have one or more Neighbors associated with it.

## User Stories
1. As an administrator, I want to create a new house record and assign it to a section so I can track it in the system.
2. As an administrator, I want to view all houses, optionally filtered by section.
3. As an administrator, I want to edit a house's details (e.g., address, lot number).
4. As an administrator, I want to see the payment status of a house at a glance (paid / delinquent).
5. As an administrator, I want to delete a house only if it has no neighbors or payment history.

## Data Model
```json
{
  "house_id": "string (auto-generated)",
  "section_id": "string (FK to sections)",
  "lot_number": "string (e.g., 'Lote 14')",
  "address": "string (e.g., 'Calle 10 #14')",
  "status": "string ('active' | 'vacant' | 'under_construction')",
  "current_balance": "number (computed: total dues - total payments)",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

## UI Screens (Administrator)
1. **House List**: Filterable by section. Each card shows lot number, address, and a color-coded payment status badge (green = paid, red = delinquent).
2. **Create/Edit House**: Form with section dropdown, lot number, and address fields.
3. **House Detail**:  Shows the house info, its associated neighbors (Feature 04), and payment history (Feature 05).

## Validation Rules
- Lot number must be unique within a section.
- Cannot delete a house that has neighbors or payment records associated with it.

## Access Control
| Role | Create | Read | Update | Delete |
|---|---|---|---|---|
| `admin` | ✅ | ✅ | ✅ | ✅ |
| `oversight_committee` | ❌ | ✅ | ❌ | ❌ |
| `neighbor_active` | ❌ | Own house only | ❌ | ❌ |
| `neighbor_delinquent` | ❌ | Own house only | ❌ | ❌ |
