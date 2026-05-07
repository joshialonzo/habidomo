# Project TODO

This file is a living document intended for agentic workflows (vibe-coding). When you assign a task to the AI, reference the items in this list.

## Phase 1: Scaffolding (In Progress)
- [x] Create project subdirectories (`apps/web`, `apps/mobile`, `infra`, `docs`, `scripts`)
- [x] Scaffold React / Next.js web app
- [x] Scaffold React Native mobile app
- [x] Create agent Markdown context files

## Phase 2: AWS Infrastructure
- [ ] Initialize AWS CDK project in `/infra`
- [ ] Define Lambda functions and API Gateway endpoints
- [ ] Provision DynamoDB tables with CDK

## Phase 3: Core App Features
- [ ] Set up shared API client and cross-platform models
- [ ] Implement authentication UI and API integration for web and mobile
- [ ] Build core CRUD workflows for sections, houses, neighbors, payments, and expenses

## Phase 4: Deployment and Integration
- [ ] Deploy CDK stack and verify API connectivity
- [ ] Connect web and mobile apps to the deployed backend
- [ ] Document the end-to-end deployment process
