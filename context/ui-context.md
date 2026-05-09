# CLI Output Context

Habidomo is a command-line application. UI theming and styling (colors, typography, components) are not applicable.

## CLI Output Format

**Output Formatting Principles:**
- Clear, human-readable text output
- Use of ANSI color codes for emphasis (success=green, error=red, warning=yellow)
- Organized tables for data display (e.g., monthly reports, neighbor lists)
- Consistent prefixes for message types:
  - `✓` for success
  - `✗` for error
  - `!` for warning
  - `ℹ` for info

**Table Format:**
- Column headers in uppercase
- Data rows aligned and readable
- Optional pagination for large datasets

**Help Text:**
- Every command includes `--help` or `-h` flag
- Clear usage examples
- Concise descriptions of arguments and options
