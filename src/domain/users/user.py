from uuid import UUID, uuid4

from humps import camelize
from pydantic import BaseModel, Field


class User(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    username: str
    password: str

    class Config:
        frozen = True
        alias_generator = camelize
        allow_population_by_field_name = True
