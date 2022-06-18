from uuid import UUID, uuid4

from pydantic import Field

from .user_base import UserBase


class User(UserBase):
    user_id: UUID = Field(default_factory=uuid4)

    class Config:
        orm_mode = True
