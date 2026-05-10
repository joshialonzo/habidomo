from abc import ABC, abstractmethod


class AbstractRepository[T](ABC):
    @abstractmethod
    def add(self, item: T) -> None:
        pass

    @abstractmethod
    def get(self, item_id: str) -> T | None:
        pass

    @abstractmethod
    def list(self) -> list[T]:  # noqa: A003
        pass

    @abstractmethod
    def update(self, item: T) -> None:
        pass

    @abstractmethod
    def delete(self, item_id: str) -> bool:
        pass
