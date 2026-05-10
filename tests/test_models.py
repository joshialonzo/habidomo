import time
from datetime import datetime
from uuid import uuid4

import pytest

from shared.models import Section

# Tolerance for timestamp comparisons (microseconds)
TIMESTAMP_TOLERANCE_SECONDS = 0.001


class TestSection:
    def test_create_section_with_required_fields(self):
        """Test creating a section with minimal required fields."""
        section = Section(name="Test Section")

        assert section.name == "Test Section"
        assert section.description is None
        assert isinstance(section.section_id, str)
        assert isinstance(section.created_at, datetime)
        assert isinstance(section.updated_at, datetime)
        # Timestamps should be very close (within microseconds)
        assert (
            abs((section.created_at - section.updated_at).total_seconds())
            < TIMESTAMP_TOLERANCE_SECONDS
        )

    def test_create_section_with_all_fields(self):
        """Test creating a section with all fields."""
        section_id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()

        section = Section(
            section_id=section_id,
            name="Test Section",
            description="A test section",
            created_at=created_at,
            updated_at=updated_at,
        )

        assert section.section_id == section_id
        assert section.name == "Test Section"
        assert section.description == "A test section"
        assert section.created_at == created_at
        assert section.updated_at == updated_at

    def test_name_validation_empty_string(self):
        """Test that empty name raises ValueError."""
        with pytest.raises(ValueError, match="Section name cannot be empty"):
            Section(name="")

    def test_name_validation_whitespace_only(self):
        """Test that whitespace-only name raises ValueError."""
        with pytest.raises(ValueError, match="Section name cannot be empty"):
            Section(name="   ")

    def test_name_validation_strips_whitespace(self):
        """Test that name is stripped of whitespace."""
        section = Section(name="  Test Section  ")
        assert section.name == "Test Section"

    def test_update_timestamp(self):
        """Test updating the timestamp."""
        section = Section(name="Test Section")
        original_updated_at = section.updated_at

        # Simulate some time passing
        time.sleep(0.001)

        section.update_timestamp()

        assert section.updated_at > original_updated_at
