# API Contracts

This file defines the data contracts and schemas passed between the frontend, DynamoDB database, and AWS Lambda-backed API.

## Database Tables

### `users` table
```json
{
  "id": "integer",
  "email": "string",
  "display_name": "string",
  "phone_number": "string",
  "role": "string",
  "created_at": "timestamp"
}
```

## Backend API Endpoints

### `GET /api/v1/health`
**Response:**
```json
{
  "status": "ok"
}
```

## Agent Instructions
*When adding a new database table or a new endpoint, document the JSON shape and URLs here so the frontend and mobile apps can generate shared models.*
