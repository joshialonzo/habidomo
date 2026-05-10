# 0001: Sections Management CRUD

## Description

Implement a complete CRUD (Create, Read, Update, Delete) interface for managing condominium sections in the Habidomo CLI application. Sections represent geographic or logical groupings of houses (e.g., streets or clusters).

### Requirements
- **Data Model**: Section entity with ID, name, description, timestamps
- **Storage**: In-memory storage for initial implementation
- **CLI Interface**: Command-line commands using Click framework
- **Architecture**: Follow Cosmic Python patterns (Repository, Service Layer, Dependency Injection)
- **Code Quality**: Implement ruff (linting/formatting), pyright (type checking), pre-commit hooks
- **Validation**: Pydantic models with business rule validation

### Acceptance Criteria
- [x] Section model with validation (Pydantic)
- [x] Repository pattern with abstract base class
- [x] Service layer for business logic
- [x] CLI commands: create, list-sections, update, delete
- [x] Unique name constraint enforcement
- [x] Code quality tools configured (ruff, pyright, pre-commit)
- [x] Local testing instructions documented
- [x] Unit tests with 100% coverage implemented
- [x] All code passes linting and type checking

### Design Patterns

#### 1. Repository Pattern (Cosmic Python)
Abstracts data persistence behind a common interface, enabling testability and swappability of storage implementations.
- **Abstract Repository**: `shared/repositories/abstract_repository.py` - Generic interface defining CRUD operations
- **Concrete Implementation**: `shared/repositories/sections_repository.py` - In-memory storage using `InMemorySectionsRepository[Section]`
- **Benefits**: Decouples business logic from storage mechanism; easy to swap in CSV, database, or API persistence later

#### 2. Service Layer Pattern (Cosmic Python)
Orchestrates business logic and domain rules, acting as the primary interface for CLI operations.
- **Location**: `shared/service_layer/sections_service.py` - `SectionsService` class
- **Responsibilities**:
  - Business rule enforcement (unique name validation)
  - Timestamp management on updates
  - Repository coordination
- **Benefits**: Centralized business logic; reusable across CLI and future APIs

#### 3. Dependency Injection
Repository is injected into Service rather than hardcoded, enabling loose coupling and testability.
- **Instantiation**: `cli/app.py` lines 13-14 - Repository created and passed to service
- **Service Constructor**: `shared/service_layer/sections_service.py` line 5 - Accepts `AbstractRepository[Section]`
- **Test Fixtures**: `tests/test_service_layer.py` - Fixtures provide fresh repository and service per test
- **Benefits**: Easy to mock in tests; can inject different implementations without code changes

#### 4. Data Validation Pattern (Pydantic)
Models define structure and enforce constraints at the domain layer.
- **Field Validation**: `shared/models.py` line 18 - `@field_validator` ensures non-empty names
- **Model Validation**: `shared/models.py` line 14 - `@model_validator` ensures timestamps are consistent
- **Benefits**: Type safety; validation errors caught early; automatic serialization support

#### 5. Command Pattern (Click)
CLI commands encapsulate requests as objects, enabling structured command dispatch.
- **Command Groups**: `cli/app.py` lines 24-26 - `@click.group()` organizes related commands
- **Subcommands**: `cli/app.py` lines 30-74 - `create`, `list-sections`, `update`, `delete` commands
- **Command Handlers**: Each command is a function that invokes service methods
- **Benefits**: Extensible command structure; consistent error handling; built-in help generation

#### 6. Generic Type Pattern
Generic types preserve type information through abstraction layers for type safety.
- **Abstract Generic**: `shared/repositories/abstract_repository.py` line 7 - `AbstractRepository[T]` with `Generic[T]`
- **Concrete Type**: `shared/repositories/sections_repository.py` line 6 - `AbstractRepository[Section]` specifies Section type
- **Service Type Hint**: `shared/service_layer/sections_service.py` line 5 - `AbstractRepository[Section]` for type checking
- **Benefits**: Full type inference through call chain; pyright validation catches type errors

#### 7. Factory Pattern (implicit)
Service factory creates consistent service instances with proper dependency injection.
- **Location**: `cli/app.py` lines 13-14 - Repository and service instantiated with dependencies
- **Reusability**: Single instance used across all CLI commands
- **Benefits**: Consistent behavior; single point of control for service configuration
- **Models**: `shared/models.py` - Pydantic BaseModel
- **Repository**: `shared/repositories/` - Abstract and in-memory implementations
- **Service**: `shared/service_layer/` - Business logic with dependency injection
- **CLI**: `cli/app.py` - Click commands with service integration
- **Tools**: `pyproject.toml`, `pyrightconfig.json`, `.pre-commit-config.yaml`

## Prompts

### Prompt 1

Consider these files:
* @file:02_sections_management.md
* @file:data-model.md
I want to implement the Sections CRUD operations in the CLI. I want to declare the models in the shared/ folder and store the records in the memory. Create an app entrypoint in the cli/ folder; it could be an app.py file.
Create a markdown file with a number like 0001 and a title with snake case format; let's emulate we are a software company.
Save this prompt in the corresponding ticket.

### Prompt 2

Follow these instructions:
* Implement ruff (flake8, isort, black), pyright, pre-commit, and pydantic in the project.
* Refactor the current feature using the design patterns we have in the "cosmic python" book.
* Write the instructions to test locally in the current MD ticket. Append a new section.

### Prompt 3

Write a ticket description in the @file:0001: Sections Management CRUD.

### Prompt 4

Implement the latest pytest version and provide 100% coverage for all the code in shared/.

### Prompt 5

Create a virtual environment using python 3.13 and reinstall all.

### Prompt 6

Append the usage to the current ticket.

### Prompt 7

I have this issue:

Import "click" could not be resolved

### Prompt 8

Write the design patterns used in this ticket and detail the instances of these in the "### Design Patterns" section of the markdown.

### Prompt 9

Fix this:

(venv) ➜  habidomo git:(0001_sections_management_crud) ✗ ruff check . --fix
UP046 Generic class `AbstractRepository` uses `Generic` subclass instead of type parameters
 --> shared/repositories/abstract_repository.py:7:31
  |
7 | class AbstractRepository(ABC, Generic[T]):
  |                               ^^^^^^^^^^
8 |     @abstractmethod
9 |     def add(self, item: T) -> None:
  |
help: Use type parameters

### Prompt 10

Fix this:

PLR2004 Magic value used in comparison, consider replacing `0.001` with a constant variable
  --> tests/test_models.py:21:81
   |
19 |         assert isinstance(section.updated_at, datetime)
20 |         # Timestamps should be very close (within microseconds)
21 |         assert abs((section.created_at - section.updated_at).total_seconds()) < 0.001
   |                                                                                 ^^^^^
22 |
23 |     def test_create_section_with_all_fields(self):

### Prompt 11

Fix this:

PLR2004 Magic value used in comparison, consider replacing `2` with a constant variable
  --> tests/test_repositories.py:52:31
   |
50 |         result = repo.list()
51 |
52 |         assert len(result) == 2
   |                               ^
53 |         assert section1 in result
54 |         assert section2 in result

## Local Testing Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install pre-commit
   pre-commit install
   ```

2. **Run code quality checks:**
   ```bash
   ruff check . --fix
   ruff format .
   pyright
   ```

3. **Test the CLI:**
   - View help: `python cli/app.py --help`
   - View sections help: `python cli/app.py sections --help`
   - Create a section: `python cli/app.py sections create --name "Calle 10" --description "Main street"`
   - List sections: `python cli/app.py sections list-sections`
   - Update a section: `python cli/app.py sections update <section_id> --name "New Name"`
   - Delete a section: `python cli/app.py sections delete <section_id>`

Note: Since data is stored in memory, sections are not persisted between separate CLI invocations (`python cli/app.py ...`). End-to-end CRUD verification requires a single long-running process/test harness or a persistent storage backend.

4. **Run unit tests:**
   ```bash
   pytest
   ```

   This will run all tests with 100% coverage reporting for the `shared/` directory. Coverage report is also generated in HTML format in the `htmlcov/` directory.

## Usage

### Environment Setup

1. **Create virtual environment (Python 3.13):**
   ```bash
   python3.13 -m venv venv
   source venv/bin/activate  # macOS/Linux
   ```

2. **Install all dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install pre-commit ruff pyright
   pre-commit install
   ```

### Command Reference

#### Help Commands
```bash
# Show main CLI help
python cli/app.py --help

# Show sections command help
python cli/app.py sections --help

# Show specific command help
python cli/app.py sections create --help
```

#### Create a Section
```bash
# Create section with name and description
python cli/app.py sections create --name "Calle 10" --description "Main street area"

# Expected output:
# ✓ Section created: Calle 10 (ID: 84540997-7b6a-43cc-ace7-80997e695b28)
```

#### List All Sections
```bash
python cli/app.py sections list-sections

# Example output:
# SECTIONS:
# ────────────────────────────────────────────────────────────────────────────
# ID: 84540997-7b6a-43cc-ace7-80997e695b28
# Name: Calle 10
# Description: Main street area
# Created: 2026-05-09 20:53:19.773751
# ────────────────────────────────────────────────────────────────────────────
```

#### Update a Section
```bash
# Update name
python cli/app.py sections update 84540997-7b6a-43cc-ace7-80997e695b28 --name "Calle 10 - Poniente"

# Update description
python cli/app.py sections update 84540997-7b6a-43cc-ace7-80997e695b28 --description "Updated description"

# Update both
python cli/app.py sections update 84540997-7b6a-43cc-ace7-80997e695b28 --name "New Name" --description "New description"

# Expected output:
# ✓ Section updated: Calle 10 - Poniente
```

#### Delete a Section
```bash
python cli/app.py sections delete 84540997-7b6a-43cc-ace7-80997e695b28

# Expected output:
# ✓ Section deleted
```

### Workflow Example

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Create three sections
python cli/app.py sections create --name "Calle 10" --description "Main avenue"
python cli/app.py sections create --name "Calle 11" --description "Secondary avenue"
python cli/app.py sections create --name "Calle 12" --description "Residential area"

# 3. List all sections
python cli/app.py sections list-sections

# 4. Update a section (copy ID from list output)
python cli/app.py sections update <SECTION_ID> --name "Calle 10 Norte"

# 5. Delete a section
python cli/app.py sections delete <SECTION_ID>

# 6. Verify deletion
python cli/app.py sections list-sections
```

### Quality Assurance

Run these commands to ensure code quality:

```bash
# Lint and fix issues
ruff check . --fix

# Format code
ruff format .

# Type checking
pyright

# Run tests (30 tests, 100% coverage)
pytest

# Run tests with verbose output
pytest -v

# Generate coverage HTML report
pytest --cov=shared --cov-report=html
```
