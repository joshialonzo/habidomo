# System Architecture

## Overview
This application uses a Flask-driven architecture where the backend serves the web interface, business logic, and API endpoints.

### 1. Web UI + Backend
- **Web App:** Static HTML/CSS and vanilla JavaScript served by Flask templates and static assets.
- **Backend:** Flask application that handles request routing, server-side rendering, API endpoints, and business logic.
- **Role:** Presentation, form handling, authentication, and data access.

### 2. Data Layer
- **Database:** PostgreSQL
- **Role:** Persistent relational storage for sections, houses, neighbors, payments, expenses, and users.

### 3. Deployment
- **Runtime:** Python + Flask
- **Hosting:** WSGI-compatible server or local Flask development server
- **Role:** Serve the application and expose the backend API.

## Data Flow
- The browser sends requests to Flask routes.
- Flask handlers render pages or return JSON.
- The backend reads and writes data in PostgreSQL.
- Static assets and client-side behavior are served from Flask's static directory.

## Agent Instructions
*When suggesting architectural changes, update this document so the system plan stays aligned with the current Flask/PostgreSQL stack.*
