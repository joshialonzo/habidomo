# Feature 02: Sections Management (CRUD)

## Status
- **Current State**: Planned
- **Priority**: 🔴 Critical (Data Foundation)
- **Frontend Target**: Vanilla JS and Flask-rendered templates
- **Backend Target**: Flask backend with PostgreSQL

## Overview
A **Section** is a logical grouping of houses — typically a street or a cluster of streets within the condominium. Sections are the top-level organizational unit.

## User Stories
1. As an administrator, I want to create a new section (e.g., "Calle 10") so I can organize houses by area.
2. As an administrator, I want to view a list of all sections with the count of houses in each.
3. As an administrator, I want to edit a section's name or description.
4. As an administrator, I want to delete a section only if it has no houses assigned to it.

## Data Model
```json
{
  "section_id": "string (auto-generated)",
  "name": "string (e.g., 'Calle 10 - Poniente')",
  "description": "string (optional)",
  "house_count": "number (computed/denormalized)",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

## UI Screens (Administrator)
1. **Section List**: Scrollable list/cards showing all sections with house counts.
2. **Create/Edit Section**: Simple form with name and optional description fields.
3. **Section Detail**: Tapping a section shows its associated houses (links to Feature 03).

## Validation Rules
- Section name must be unique.
- Cannot delete a section that still contains houses (show error message).

## Access Control
| Role | Create | Read | Update | Delete |
|---|---|---|---|---|
| `admin` | ✅ | ✅ | ✅ | ✅ |
| `oversight_committee` | ❌ | ✅ | ❌ | ❌ |
| All others | ❌ | ❌ | ❌ | ❌ |
