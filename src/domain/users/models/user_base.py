from humps import camelize
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    age: int

    class Config:
        frozen = True
        alias_generator = camelize
        allow_population_by_field_name = True
