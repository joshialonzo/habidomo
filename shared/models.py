# pyright: reportUnknownVariableType=false
from datetime import datetime
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

    @model_validator(mode="after")
    def set_timestamps(self):
        # Ensure created_at and updated_at are the same initially
        if self.created_at == self.updated_at:
            now = datetime.now()
            self.created_at = now
            self.updated_at = now
        return self

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            msg = "Section name cannot be empty"
            raise ValueError(msg)
        return v.strip()

    def update_timestamp(self) -> None:
        self.updated_at = datetime.now()
