import pytest

from shared.repositories.sections_repository import InMemorySectionsRepository
from shared.service_layer.sections_service import SectionsService


@pytest.fixture()
def repository():
    """Fixture to provide a fresh repository for each test."""
    return InMemorySectionsRepository()


@pytest.fixture()
def service(repository):
    """Fixture to provide a service with repository."""
    return SectionsService(repository)


class TestSectionsService:
    def test_create_section_success(self, service, repository):
        """Test successfully creating a section."""
        section = service.create_section("Test Section", "A test description")

        assert section.name == "Test Section"
        assert section.description == "A test description"
        assert len(repository.list()) == 1

    def test_create_section_duplicate_name(self, service):
        """Test creating a section with duplicate name raises error."""
        service.create_section("Test Section")

        with pytest.raises(
            ValueError, match="Section with name 'Test Section' already exists"
        ):
            service.create_section("Test Section")

    def test_create_section_empty_name(self, service):
        """Test creating a section with empty name raises error."""
        with pytest.raises(ValueError, match="Section name cannot be empty"):
            service.create_section("")

    def test_get_sections_empty(self, service):
        """Test getting sections when none exist."""
        result = service.get_sections()

        assert result == []

    def test_get_sections_with_data(self, service):
        """Test getting sections with data."""
        section1 = service.create_section("Section 1")
        section2 = service.create_section("Section 2")

        result = service.get_sections()

        expected_count = 2
        assert len(result) == expected_count
        assert section1 in result
        assert section2 in result

    def test_get_section_by_id_existing(self, service):
        """Test getting an existing section by ID."""
        section = service.create_section("Test Section")

        result = service.get_section_by_id(section.section_id)

        assert result == section

    def test_get_section_by_id_non_existing(self, service):
        """Test getting a non-existing section by ID."""
        result = service.get_section_by_id("non-existing-id")

        assert result is None

    def test_update_section_success(self, service):
        """Test successfully updating a section."""
        section = service.create_section("Original Name", "Original description")
        original_updated_at = section.updated_at

        updated = service.update_section(
            section.section_id, name="Updated Name", description="Updated description"
        )

        assert updated is not None
        assert updated.name == "Updated Name"
        assert updated.description == "Updated description"
        assert updated.updated_at > original_updated_at

    def test_update_section_partial_update(self, service):
        """Test updating only some fields."""
        section = service.create_section("Original Name", "Original description")

        updated = service.update_section(section.section_id, name="Updated Name")

        assert updated.name == "Updated Name"
        assert updated.description == "Original description"

    def test_update_section_duplicate_name(self, service):
        """Test updating to a duplicate name raises error."""
        service.create_section("Section 1")
        section2 = service.create_section("Section 2")

        with pytest.raises(
            ValueError, match="Section with name 'Section 1' already exists"
        ):
            service.update_section(section2.section_id, name="Section 1")

    def test_update_section_allow_same_name(self, service):
        """Test updating with the same name is allowed."""
        section = service.create_section("Test Section")

        updated = service.update_section(
            section.section_id, description="New description"
        )

        assert updated.description == "New description"
        assert updated.name == "Test Section"

    def test_update_section_non_existing(self, service):
        """Test updating a non-existing section."""
        result = service.update_section("non-existing-id", name="New Name")

        assert result is None

    def test_update_section_no_changes(self, service):
        """Test updating with no changes."""
        section = service.create_section("Test Section")
        original_updated_at = section.updated_at

        updated = service.update_section(section.section_id)

        assert updated == section
        assert updated.updated_at == original_updated_at

    def test_delete_section_existing(self, service, repository):
        """Test deleting an existing section."""
        section = service.create_section("Test Section")

        result = service.delete_section(section.section_id)

        assert result is True
        assert len(repository.list()) == 0

    def test_delete_section_non_existing(self, service):
        """Test deleting a non-existing section."""
        result = service.delete_section("non-existing-id")

        assert result is False
