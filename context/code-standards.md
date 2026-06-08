# Code Standards

## General

- Keep modules small and single-purpose; separate UI concerns from backend logic
- Fix root causes, do not layer workarounds; especially important in data persistence and API design
- Do not mix unrelated concerns in one module (UI layer, business logic, data access)
- All persistent data access must go through the Serverpod backend in `habidomo_server/`

## Dart and Flutter

- Use strong typing and null-safety throughout the codebase
- Validate input at system boundaries (UI input and API request payloads) before processing
- Use descriptive variable and function names; avoid abbreviations except standard conventions
- Keep functions and widgets focused on a single responsibility
- Use standard Dart and Flutter APIs for platform-aware operations

## Frontend Application (`habidomo_flutter/`)

- Keep UI widgets thin and delegate business logic to backend services
- Use `habidomo_client` for typed Serverpod API calls
- Perform input validation and formatting in the UI layer before sending requests
- Return clear, user-friendly messages and handle errors gracefully
- Commands and screens should follow the feature workflows defined in `context/features/`

## Backend Application (`habidomo_server/`)

- Contains business logic, data models, Serverpod endpoints, and auth rules
- No direct database access from frontend; all persistence goes through backend endpoints
- Implement validation and business rules in backend modules
- Keep endpoint handlers concise and delegate domain logic to service classes
- Include unit and integration tests for all critical backend behavior

## Data and Storage

- The Serverpod-managed database is the primary source of truth
- Use `habidomo_server/` data models and migrations to evolve schema safely
- Treat `local/` as sample or legacy CSV data, not production storage
- Do not expose raw database access to the frontend
- Implement transactional behavior through Serverpod when needed

## File Organization

- **`habidomo_flutter/`** — Flutter frontend application and platform-specific runners
- **`habidomo_server/`** — Serverpod backend server, endpoints, and configuration
- **`habidomo_client/`** — Generated Serverpod client package for typed API access
- **`local/`** — Sample CSV fixture data and legacy import files
- **`context/`** — Documentation, feature specs, and architecture guidance

## Testing

- Write unit tests for frontend state and backend logic
- Use `flutter test` for UI tests and `dart test` for backend tests
- Use descriptive test names that explain the scenario and expected outcome
- Keep tests isolated from external services when possible
