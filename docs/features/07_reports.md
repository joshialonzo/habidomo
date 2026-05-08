# Feature 07: Financial Reports

## Status
- **Current State**: Planned
- **Priority**: 🟠 High
- **Frontend Target**: React / Next.js (`/apps/web`) + React Native (`/apps/mobile`)
- **Backend Target**: AWS CDK / Lambda / DynamoDB (`/infra`) — Google Sheets export and WhatsApp bot handled by Lambda or managed services.

## Overview
Reports aggregate payment and expense data into summaries that administrators can **view in-app**, **copy as formatted text to paste into WhatsApp**, or **export to Google Sheets**. This is the primary accountability tool for the condominium.

## Report Types

### 7a. Monthly Payments Report
Shows all payments received for a specific month.
- List of houses that paid, with amount and date.
- List of houses that did NOT pay (delinquent).
- Total collected vs. total expected.
- Collection rate percentage.

### 7b. Monthly Expenses Report
Shows all expenses incurred during a specific month.
- Breakdown by category with subtotals.
- Total spent.

### 7c. Monthly Balance Report
The executive summary combining 7a and 7b.
- Total income (payments).
- Total expenses.
- Net balance (income - expenses).
- Running accumulated balance (if tracked).

## User Stories
1. As an administrator, I want to select a month/year and instantly see a payments report.
2. As an administrator, I want to tap a "Copy to Clipboard" button that formats the report as clean WhatsApp-friendly text (with emojis and line breaks) so I can paste it directly into the community group chat.
3. As an administrator, I want to export a report to a Google Sheet so the oversight committee can audit it in spreadsheet format.
4. (Future) As a neighbor, I want to message the WhatsApp bot with "reporte abril 2026" and receive the monthly balance report automatically.

## Clipboard Format Example (WhatsApp)
```
📊 *Habidomo — Reporte Abril 2026*

💰 *Ingresos*
✅ Lote 14 - Juan Pérez: $500 MXN (transferencia)
✅ Lote 22 - María López: $500 MXN (efectivo)
❌ Lote 8 - Carlos Ruiz: *No pagó*
❌ Lote 31 - Ana Torres: *No pagó*

Total cobrado: $1,000 MXN de $2,000 MXN esperados (50%)

💸 *Gastos*
🌿 Jardinería: $300 MXN
🔒 Seguridad: $400 MXN
💡 Electricidad: $150 MXN

Total gastado: $850 MXN

📈 *Balance: +$150 MXN*
```

## Technical Notes
- **Clipboard**: Use the browser clipboard API (`navigator.clipboard.writeText()`) to copy the formatted string.
- **Google Sheets**: Use the Google Sheets API via Lambda functions or managed integration services. The admin provides a sheet ID, and the backend writes the report data as rows.
- **WhatsApp Bot**: Future feature using the WhatsApp Business API or a Twilio integration in Lambda or a serverless workflow.

## Access Control
| Role | View | Copy to Clipboard | Export to Sheets |
|---|---|---|---|
| `admin` | ✅ | ✅ | ✅ |
| `oversight_committee` | ✅ | ✅ | ✅ |
| `neighbor_*` | ❌ | ❌ | ❌ |
