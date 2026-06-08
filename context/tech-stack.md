# Tech Stack

This document defines the libraries, frameworks, and versions for the current Habidomo Serverpod/Flutter application. **AI Agents: Do not deviate from this stack, use alternative libraries, or introduce new major dependencies without asking the user for confirmation.**

## Runtime
- **Language:** Dart 3.0+
- **Framework:** Flutter for the frontend
- **Backend:** Serverpod 3.4.x
- **Package Manager:** `dart pub` / `flutter pub`

## Frontend
- **Primary:** Flutter for mobile, desktop, and web UI
- **Client Integration:** `habidomo_client` generated Serverpod client package
- **Purpose:** Build responsive user interfaces and consume typed API endpoints

## Backend
- **Primary:** Serverpod for API routing, authentication, and business logic
- **Database:** PostgreSQL via Serverpod
- **Purpose:** Host endpoints, implement authorization rules, and persist domain data

## Generated Client
- **Package:** `habidomo_client`
- **Purpose:** Provide a shared typed Dart interface used by the Flutter app to call Serverpod endpoints

## Testing
- **Frontend tests:** `flutter test`
- **Backend tests:** `dart test`
- **Serverpod utilities:** `serverpod_test`

## Data Persistence
- **Primary datastore:** PostgreSQL managed by Serverpod
- **Sample data:** `local/` contains CSV fixture data and import samples
- **Runtime access:** Always through Serverpod backend endpoints

## Build & Deployment
- Build Flutter app with `flutter build`
- Run backend with Serverpod or `dart run bin/main.dart`
- Keep dependencies pinned in subpackage manifests

## Agent Instructions
*Before adding a dependency, verify it's necessary and confirm with user. Keep dependencies minimal and document all new packages in this file.*
