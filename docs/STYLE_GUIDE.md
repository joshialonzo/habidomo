# Style Guide

This file defines the coding style conventions for both human and AI contributors.

## General Guidelines
- Keep functions small and single-purpose.
- All code must be strongly typed and explicit in TypeScript.
- Write brief documentation for complex functions.

## Frontend / React / TypeScript
- **Formatting**: Run `prettier --write .` and `npm run lint` before finalizing code.
- **Components**: Keep React components small and reusable. Prefer hooks and composable UI primitives.
- **Typing**: Use strict TypeScript types. Avoid `any` unless there is a strong reason.
- **File Naming**: Use `PascalCase` for React component files, `kebab-case` for route/page files, and `camelCase` for utility modules.

## JSON / NoSQL Data 
- Database document keys should be `camelCase`.

## Agent Instructions
*AI Agents must output code that adheres strictly to these guidelines. Refactor code seamlessly to match this style.*
- Database document keys should be `camelCase`.

## Agent Instructions
*AI Agents must output code that adheres strictly to these guidelines. Refactor code seamlessly to match this style.*
