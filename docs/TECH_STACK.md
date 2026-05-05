# Tech Stack

This document strictly defines the libraries, frameworks, and versions to be used in this project. **AI Agents: Do not deviate from this stack, use alternative libraries, or introduce new major dependencies without asking the user for confirmation.**

## Frontend (`/frontend`)
- **Language:** TypeScript
- **Framework:** React / Next.js
- **UI / Styling:** [e.g., Tailwind CSS, Material UI, or CSS Modules - Please specify]
- **State Management:** [e.g., React Context, Zustand, Redux, React Query - Please specify]
- **Data Fetching:** `fetch`, `axios`, or `swr`
- **Routing:** Next.js built-in routing

## Backend (`/backend`)
- **Language:** Python 3.11+
- **Framework:** Flask
- **Database:** PostgreSQL
- **ORM / Migrations:** SQLAlchemy + Alembic (or preferred PostgreSQL toolkit)
- **Authentication:** JWT or session cookies managed by Flask
- **Package Manager:** `pip` / `poetry`

## Agent Instructions
*Before importing a package to the frontend (via package.json) or backend (via requirements.txt / pyproject.toml), verify if there is an existing library listed here that solves the problem. If not, add your new dependency to this file as well.*
