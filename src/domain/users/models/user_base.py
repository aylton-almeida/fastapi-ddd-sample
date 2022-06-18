from humps import camelize
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    age: int

    class Config:
        frozen = True
        alias_generator = camelize
        allow_population_by_field_name = True
