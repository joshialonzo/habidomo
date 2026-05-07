# System Architecture

## Overview
This application uses an AWS CDK-driven architecture that separates the user interfaces from infrastructure and business logic.

### 1. Frontend
- **Web App:** React / Next.js (`/apps/web`)
- **Mobile App:** React Native (`/apps/mobile`)
- **Role:** Presentation, user interaction, offline-aware UI, and API integration.

### 2. Infrastructure / Backend (`/infra`)
- **Technology:** AWS CDK (TypeScript)
- **Compute:** AWS Lambda functions
- **API:** API Gateway HTTP/REST endpoints
- **Data Store:** DynamoDB managed by CDK
- **Role:** Business logic, authentication, API surface, data persistence, reporting, and integrations.

### 3. Data Layer
- **Data Store:** DynamoDB
- **Role:** Persist application data for sections, houses, neighbors, payments, expenses, and users.

## Data Flow
- The web and mobile apps call API Gateway endpoints.
- Lambda handlers in `/infra/lambdas/` execute business logic and read/write the relational database.
- CDK manages deployment, infrastructure definitions, and resource permissions.

## Agent Instructions
*When suggesting architectural changes, update this document so the system plan stays aligned with the current CDK-driven stack.*
