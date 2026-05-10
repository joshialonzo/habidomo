from shared.models import Section
from shared.repositories.abstract_repository import AbstractRepository


class SectionsService:
    def __init__(self, repository: AbstractRepository[Section]) -> None:
        self.repository = repository

    def create_section(self, name: str, description: str | None = None) -> Section:
        # Check uniqueness
        existing_sections = self.repository.list()
        if any(s.name == name for s in existing_sections):
            msg = f"Section with name '{name}' already exists"
            raise ValueError(msg)

        section = Section(name=name, description=description)
        self.repository.add(section)
        return section

    def get_sections(self) -> list[Section]:
        return self.repository.list()

    def get_section_by_id(self, section_id: str) -> Section | None:
        return self.repository.get(section_id)

    def update_section(
        self, section_id: str, name: str | None = None, description: str | None = None
    ) -> Section | None:
        section = self.repository.get(section_id)
        if not section:
            return None

        changed = False

        if name is not None and name != section.name:
            existing_sections = self.repository.list()
            if any(s.name == name for s in existing_sections):
                msg = f"Section with name '{name}' already exists"
                raise ValueError(msg)
            section.name = name
            changed = True

        if description is not None and description != section.description:
            section.description = description
            changed = True

        if changed:
            section.update_timestamp()

        self.repository.update(section)
        return section

    def delete_section(self, section_id: str) -> bool:
        return self.repository.delete(section_id)
