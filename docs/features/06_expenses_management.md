# Feature 06: Expenses Management (CRUD)

## Status
- **Current State**: Planned
- **Priority**: 🔴 Critical (Core Financial)
- **Frontend Target**: React / Next.js (`/apps/web`) + React Native (`/apps/mobile`)
- **Backend Target**: AWS CDK / Lambda / DynamoDB (`/infra`)

## Overview
An **Expense** records money spent by the condominium administration. Expenses are tagged to a specific **month/year** period and categorized for reporting clarity.

## User Stories
1. As an administrator, I want to register an expense with the amount, category, date, and the month it belongs to.
2. As an administrator, I want to view all expenses for a given month, grouped by category with subtotals.
3. As an administrator, I want to edit an expense if details were entered incorrectly.
4. As an administrator, I want to delete an erroneous expense (with confirmation).
5. As an administrator, I want to attach a photo of a receipt or invoice to an expense for audit purposes.

## Expense Categories (Suggested Defaults)
- Gardening / Landscaping
- Security Staff Wages
- Electricity (Common Areas)
- Water (Common Areas)
- Maintenance & Repairs
- Cleaning
- Administrative / Legal
- Insurance
- Miscellaneous

## Data Model
```json
{
  "expense_id": "string (auto-generated)",
  "category": "string (from predefined list)",
  "description": "string (e.g., 'Monthly gardener payment')",
  "amount": "number (in MXN)",
  "period_month": "number (1-12)",
  "period_year": "number (e.g., 2026)",
  "expense_date": "timestamp (when the money was spent)",
  "vendor": "string (optional, who was paid)",
  "receipt_url": "string (optional, link to uploaded receipt photo)",
  "notes": "string (optional)",
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "created_by": "string (admin UID who recorded it)"
}
```

## UI Screens (Administrator)
1. **Expenses List**: Filterable by month/year and category. Shows total spent at the top, with category breakdown.
2. **Register Expense**: Form with category dropdown, description, amount, date, vendor, period picker, and optional receipt upload.
3. **Edit Expense**: Same form, pre-populated.

## Validation Rules
- Amount must be greater than 0.
- Category must be from the predefined list.
- Period (month/year) is required.

## Access Control
| Role | Create | Read | Update | Delete |
|---|---|---|---|---|
| `admin` | ✅ | ✅ | ✅ | ✅ |
| `oversight_committee` | ❌ | ✅ | ❌ | ❌ |
| All others | ❌ | ❌ | ❌ | ❌ |
