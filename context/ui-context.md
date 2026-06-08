# UI Context

Habidomo uses a Flutter frontend for cross-platform UI. This document captures visual and UX guidance for the app.

## Flutter UI Format

**UI Principles:**
- Clean, accessible layouts for mobile, desktop, and web
- Clear hierarchy with typography, spacing, and component grouping
- Use consistent color, iconography, and affordances across screens
- Provide immediate feedback for success, errors, and warnings

**Navigation:**
- Use standard Flutter navigation patterns for nested flows
- Keep key tasks reachable from the main dashboard
- Provide clear back and cancel actions where appropriate

**Data Display:**
- Use cards, tables, or lists for entities such as sections, houses, neighbors, payments, and expenses
- Present totals and summaries clearly in report views
- Use responsive layout behavior for web and tablet form factors

**Accessibility:**
- Use readable font sizes and contrast
- Include semantic labels for interactive controls
- Support screen readers where possible

**Error Handling:**
- Show friendly error messages when API calls fail
- Provide retry or corrective actions where appropriate
- Avoid exposing raw backend errors to end users
