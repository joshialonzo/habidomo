# Tech Stack

This document strictly defines the libraries, frameworks, and versions to be used in this project. **AI Agents: Do not deviate from this stack, use alternative libraries, or introduce new major dependencies without asking the user for confirmation.**

## Frontend
- **Language:** HTML, CSS, JavaScript
- **Framework:** vanilla JavaScript and Flask-rendered templates
- **UI / Styling:** Plain CSS, utility CSS, or lightweight CSS framework if needed
- **State Management:** Browser state and DOM updates via vanilla JavaScript
- **Data Fetching:** `fetch`
- **Routing:** Flask route endpoints with optional client-side navigation for dynamic behavior

## Backend
- **Language:** Python 3.10+
- **Framework:** Flask
- **Database:** PostgreSQL
- **ORM / DB Layer:** SQLAlchemy, `psycopg`, or equivalent
- **Authentication:** Flask session cookies or JWT depending on requirements
- **Package Manager:** `pip`, `venv`, or `pipenv`
- **Deployment:** WSGI-compatible host, Docker optional

## Agent Instructions
*Before importing a package, verify if the required functionality can be achieved with Flask, vanilla JavaScript, or standard PostgreSQL tooling. Document new dependencies here when added.*
