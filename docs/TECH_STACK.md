# Tech Stack

This document strictly defines the libraries, frameworks, and versions to be used in this project. **AI Agents: Do not deviate from this stack, use alternative libraries, or introduce new major dependencies without asking the user for confirmation.**

## Frontend
- **Language:** TypeScript
- **Web Framework:** React / Next.js (`/apps/web`)
- **Mobile Framework:** React Native (`/apps/mobile`)
- **UI / Styling:** [Tailwind CSS, Material UI, or CSS Modules - Please specify]
- **State Management:** [React Context, Zustand, Redux, React Query - Please specify]
- **Data Fetching:** `fetch`, `axios`, or `swr`
- **Routing:** Next.js built-in routing for web; React Navigation for mobile

## Infrastructure (`/infra`)
- **Language:** TypeScript
- **Framework:** AWS CDK
- **Compute:** AWS Lambda
- **API:** API Gateway
- **Database:** DynamoDB (serverless NoSQL) managed by CDK
- **Authentication:** JWT, Cognito, or OIDC as defined in CDK
- **Package Manager:** `pnpm`, `npm`, or `yarn`

## Agent Instructions
*Before importing a package to the frontend or infra workspace, verify if there is an existing library listed here that solves the problem. If not, add your new dependency to this file as well.*
