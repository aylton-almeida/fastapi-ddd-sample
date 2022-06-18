from .user import User
from .user_base import UserBase


class UserCreate(UserBase):
    password: str

    def to_user(self):
        return User(**self.dict())
