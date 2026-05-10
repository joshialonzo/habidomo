# pyright: reportUnknownVariableType=false
from datetime import datetime
from typing import Any
from uuid import uuid4

from pydantic import (  # pyright: ignore[reportUnknownVariableType]
    BaseModel,
    Field,
    field_validator,
    model_validator,
)


class Section(BaseModel):
    section_id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    description: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @model_validator(mode="before")
    @classmethod
    def set_timestamps(cls, data: Any) -> Any:  # pyright: ignore[reportUnknownParameterType]
        if (
            isinstance(data, dict)
            and data.get("created_at") is None  # pyright: ignore[reportUnknownMemberType]
            and data.get("updated_at") is None  # pyright: ignore[reportUnknownMemberType]
        ):
            now = datetime.now()
            data["created_at"] = now
            data["updated_at"] = now
        return data

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            msg = "Section name cannot be empty"
            raise ValueError(msg)
        return v.strip()

    def update_timestamp(self) -> None:
        self.updated_at = datetime.now()
