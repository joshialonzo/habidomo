# Architecture Context

## Stack

| Layer      | Technology                          | Role                                                                 |
| ---------- | ----------------------------------- | -------------------------------------------------------------------- |
| Framework  | React / Next.js + React Native      | User interface for web and mobile                                    |
| Infra      | AWS CDK (TypeScript)                | Define and deploy infrastructure, API Gateway, Lambda, and database  |
| API        | API Gateway + Lambda                | Request routing, business logic, authentication, and integrations    |
| Database   | DynamoDB                            | Persistent serverless NoSQL storage for app data                   |
| Shared     | TypeScript packages                 | Cross-platform models, API client, and reusable UI/helpers          |

## System Boundaries

- `/apps/web` — Web client UI owned by the React / Next.js application.
- `/apps/mobile` — Mobile client UI owned by the React Native application.
- `/infra` — CDK stacks, Lambda handlers, and infrastructure provisioning.
- `/packages` — Shared cross-platform types, API client code, and UI utilities.

## Storage Model

- **NoSQL Database:** DynamoDB stores sections, houses, neighbors, payments, expenses, and users.
- **Blob/File Storage:** Receipt images or attachments may be stored in S3 and referenced from the DynamoDB model.

## Auth and Access Model

- Authentication is managed through the API layer. The stack can use JWT tokens, Cognito, or a similar AWS-compatible auth flow.
- Each user is identified by a phone number and a role.
- Access control is enforced by the Lambda API layer and database relationships.

## Invariants

1. Request handlers should remain stateless and offload persistence to the database.
2. Infrastructure definitions are owned by `/infra` and must be deployable via CDK.
3. Shared business models live in `/packages` to avoid duplication across web and mobile.
4. Frontend applications do not directly access the database; all data access goes through the API layer.
