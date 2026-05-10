from shared.models import Section
from shared.repositories.sections_repository import InMemorySectionsRepository


class TestInMemorySectionsRepository:
    def test_add_section(self):
        """Test adding a section to the repository."""
        repo = InMemorySectionsRepository()
        section = Section(name="Test Section")

        repo.add(section)

        assert len(repo.list()) == 1
        assert repo.list()[0] == section

    def test_get_existing_section(self):
        """Test getting an existing section."""
        repo = InMemorySectionsRepository()
        section = Section(name="Test Section")
        repo.add(section)

        result = repo.get(section.section_id)

        assert result == section

    def test_get_non_existing_section(self):
        """Test getting a non-existing section returns None."""
        repo = InMemorySectionsRepository()

        result = repo.get("non-existing-id")

        assert result is None

    def test_list_sections_empty(self):
        """Test listing sections when repository is empty."""
        repo = InMemorySectionsRepository()

        result = repo.list()

        assert result == []

    def test_list_sections_with_data(self):
        """Test listing sections with data."""
        repo = InMemorySectionsRepository()
        section1 = Section(name="Section 1")
        section2 = Section(name="Section 2")
        repo.add(section1)
        repo.add(section2)

        result = repo.list()

        expected_count = 2
        assert len(result) == expected_count
        assert section1 in result
        assert section2 in result
        # Ensure it's a copy, not the original list
        result[0] = Section(name="Modified")
        assert repo.list()[0].name == "Section 1"  # Original unchanged

    def test_update_existing_section(self):
        """Test updating an existing section."""
        repo = InMemorySectionsRepository()
        section = Section(name="Original Name")
        repo.add(section)

        updated_section = Section(
            section_id=section.section_id,
            name="Updated Name",
            description="Updated description",
        )
        repo.update(updated_section)

        stored = repo.get(section.section_id)
        assert stored == updated_section
        assert stored.name == "Updated Name"
        assert stored.description == "Updated description"

    def test_update_non_existing_section(self):
        """Test updating a non-existing section does nothing."""
        repo = InMemorySectionsRepository()
        section = Section(name="Test Section")

        repo.update(section)

        # Should not add the section
        assert len(repo.list()) == 0

    def test_delete_existing_section(self):
        """Test deleting an existing section."""
        repo = InMemorySectionsRepository()
        section = Section(name="Test Section")
        repo.add(section)

        result = repo.delete(section.section_id)

        assert result is True
        assert len(repo.list()) == 0

    def test_delete_non_existing_section(self):
        """Test deleting a non-existing section."""
        repo = InMemorySectionsRepository()

        result = repo.delete("non-existing-id")

        assert result is False
