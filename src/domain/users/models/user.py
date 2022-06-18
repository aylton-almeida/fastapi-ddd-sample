from uuid import UUID

from .user_base import UserBase


class User(UserBase):
    user_id: UUID

    class Config:
        orm_mode = True
