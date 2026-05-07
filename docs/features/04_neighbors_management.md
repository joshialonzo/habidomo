# Feature 04: Neighbors Management (CRUD)

## Status
- **Current State**: Planned
- **Priority**: 🔴 Critical (Data Foundation)
- **Frontend Target**: React / Next.js (`/apps/web`) + React Native (`/apps/mobile`)
- **Backend Target**: AWS CDK / Lambda / DynamoDB (`/infra`)

## Overview
A **Neighbor** is a person associated with a house. Neighbors are identified by their **phone number** (which doubles as their login identity). A house can have multiple neighbors (e.g., spouses), and a neighbor could theoretically own multiple houses.

## User Stories
1. As an administrator, I want to register a new neighbor by entering their name and phone number and linking them to a house.
2. As an administrator, I want to view a list of all neighbors, filterable by section or house.
3. As an administrator, I want to edit a neighbor's details (name, phone, associated house).
4. As an administrator, I want to see at a glance whether a neighbor is up to date on payments.
5. As an administrator, I want to deactivate (soft-delete) a neighbor who has moved out, preserving their payment history.

## Data Model
```json
{
  "neighbor_id": "string (auto-generated)",
  "user_id": "string (linked after phone verification, nullable)",
  "phone_number": "string (E.164 format, e.g., '+529991234567')",
  "full_name": "string",
  "house_ids": ["string (FK to houses)"],
  "role": "string ('neighbor_active' | 'neighbor_delinquent' | 'admin' | 'oversight_committee')",
  "is_active": "boolean",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

## UI Screens (Administrator)
1. **Neighbor List**: Searchable by name or phone. Filterable by section. Each row shows name, phone, house, and a status badge (active/delinquent).
2. **Create/Edit Neighbor**: Form with name, phone number (with country code picker), and a house selector dropdown.
3. **Neighbor Detail**: Shows personal info, linked house(s), and a chronological payment history.

## Validation Rules
- Phone number must be unique across all neighbors.
- Phone number must be in valid E.164 format.
- At least one house must be associated.
- Cannot hard-delete a neighbor with payment history (use soft-delete via `is_active = false`).

## Access Control
| Role | Create | Read | Update | Delete |
|---|---|---|---|---|
| `admin` | ✅ | ✅ | ✅ | ✅ (soft) |
| `oversight_committee` | ❌ | ✅ | ❌ | ❌ |
| `neighbor_*` | ❌ | Own profile only | ❌ | ❌ |
