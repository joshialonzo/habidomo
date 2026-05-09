# Data Model Reference

This file documents the core data structures and CSV schemas for the Habidomo application. All models are defined as Python dataclasses in `shared/models/`.

## Entity Relationships

```
Section 1 ---- N Houses
House 1 ---- N Neighbors
Neighbor 1 ---- N Payments
Expense N (not tied to specific neighbor; shared condominium expenses)
User 1 ---- 1 Role
```

## Core Entities

### User
Represents an authenticated person (admin or resident).
- **Primary Key:** `user_id` (UUID)
- **Identity:** `phone_number` (unique, immutable)
- **Fields:**
  - `phone_number`: Phone identity
  - `role`: `admin`, `neighbor_active`, `neighbor_delinquent`, `oversight_committee`
  - `name`: Display name
  - `created_at`: Account creation timestamp
  - `updated_at`: Last modification timestamp

### Section
A geographic or logical grouping of houses (e.g., street, cluster).
- **Primary Key:** `section_id` (UUID)
- **Fields:**
  - `name`: Section name (required, unique)
  - `description`: Optional details
  - `created_at`: Timestamp

### House
A property or lot linked to a section.
- **Primary Key:** `house_id` (UUID)
- **Foreign Key:** `section_id` → Section
- **Fields:**
  - `house_number`: Lot or property number (required, unique per section)
  - `created_at`: Timestamp

### Neighbor
A resident linked to a house.
- **Primary Key:** `neighbor_id` (UUID)
- **Foreign Key:** `house_id` → House
- **Identity:** `phone_number` (unique, immutable)
- **Fields:**
  - `phone_number`: Phone identity
  - `name`: Neighbor name
  - `email`: Optional contact
  - `status`: `active`, `delinquent`, `inactive` (based on payment history)
  - `created_at`: Timestamp

### Payment
A monthly payment record linked to a neighbor.
- **Primary Key:** `payment_id` (UUID)
- **Foreign Key:** `neighbor_id` → Neighbor
- **Fields:**
  - `amount`: Decimal payment amount
  - `month`: YYYY-MM format (required)
  - `payment_date`: When payment was received (ISO 8601)
  - `notes`: Optional memo or reference

### Expense
A shared condominium expense (e.g., maintenance, utilities).
- **Primary Key:** `expense_id` (UUID)
- **No Foreign Keys:** Expenses are shared; not linked to specific neighbors
- **Fields:**
  - `category`: `maintenance`, `utilities`, `administration`, etc.
  - `amount`: Decimal expense amount
  - `month`: YYYY-MM format
  - `description`: Optional details
  - `created_at`: Timestamp

## CSV File Structure

All CSV files in `local/` follow these conventions:
- **Headers:** First row contains field names in `snake_case`
- **Encoding:** UTF-8
- **Quoting:** Values containing commas must be quoted
- **Dates:** ISO 8601 format (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)
- **Decimals:** Standard decimal notation (e.g., `1500.00`)

## Referential Integrity

The application logic (in `shared/`) is responsible for maintaining referential integrity:
- **Cascading:** When a section is deleted, its houses should be handled gracefully
- **Constraints:** Foreign key relationships must be validated before writes
- **Orphans:** Application should prevent orphaned records (e.g., payment without neighbor)

## Financial Calculations

### Neighbor Balance
```
balance = sum(payments for neighbor in month) - (monthly_dues)
- Positive balance: overpaid or no outstanding debt
- Negative balance: delinquent
```

### Monthly Report
```
total_payments = sum(all payments in month)
total_expenses = sum(all expenses in month)
balance = total_payments - total_expenses
```

## Agent Instructions

*When implementing features, use these data models as the source of truth. All CRUD operations must respect these structures. Add to this file when introducing new entities or modifying existing relationships.*
