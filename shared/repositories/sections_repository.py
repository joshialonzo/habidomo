from shared.models import Section

from .abstract_repository import AbstractRepository


class InMemorySectionsRepository(AbstractRepository[Section]):
    def __init__(self) -> None:
        self._sections: list[Section] = []

    def add(self, item: Section) -> None:
        self._sections.append(item)

    def get(self, item_id: str) -> Section | None:
        return next((s for s in self._sections if s.section_id == item_id), None)

    def list(self) -> list[Section]:  # noqa: A003
        return self._sections.copy()

    def update(self, item: Section) -> None:
        # Since Section is mutable, just ensure it's in the list
        existing = self.get(item.section_id)
        if existing:
            index = self._sections.index(existing)
            self._sections[index] = item

    def delete(self, item_id: str) -> bool:
        section = self.get(item_id)
        if section:
            self._sections.remove(section)
            return True
        return False
