from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from src.infrastructure.postgresql.entities.base_entity import BaseEntity

from ..database import Base


class UserEntity(Base, BaseEntity):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
