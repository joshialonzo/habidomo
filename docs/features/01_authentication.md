# Feature 01: Authentication (Phone-Based)

## Status
- **Current State**: Planned
- **Priority**: 🔴 Critical (Foundation)
- **Frontend Target**: React / Next.js (`/frontend`)
- **Backend Target**: Flask / PostgreSQL (`/backend`)

## Overview
All users authenticate using their **phone number** as their primary identity. This is intentional — most condominium communication already happens on WhatsApp, so the phone number serves as a natural, universal identifier across the app and messaging channels.

## User Stories
1. As a new user, I want to sign up using my phone number and receive an SMS verification code so I can create my account.
2. As a returning user, I want to log in by verifying my phone number so I can access the app securely.
3. As an administrator, I want to assign roles to verified phone numbers so each user sees the correct dashboard.

## Roles
| Role | Description |
|---|---|
| `admin` | Condominium administrators. Full CRUD access to all entities. |
| `neighbor_active` | Neighbors who are up to date on payments. |
| `neighbor_delinquent` | Neighbors who have outstanding debts. |
| `oversight_committee` | Neighbors with read-only audit access to financials. |
| `security` | Security staff. Access to visitor/gate features only. |
| `employee` | Home employees (maids, contractors). Minimal access. |

## Technical Requirements
- Use the Flask backend to manage phone-based OTP authentication and session or token issuance.
- Store the user's role in the `users` table.
- On first login, the user must be pre-registered by an Administrator (phone number must exist in the system before they can sign up). This prevents unauthorized access.
- Role-based routing: after login, redirect the user to the appropriate dashboard based on their role.

## Out of Scope (Deferred)
- Email/password login.
- Google/Apple social login.
- Self-registration (neighbors must be added by an admin first).
