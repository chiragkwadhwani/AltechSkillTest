from typing import Union
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    description: Union[str, None] = None
    publish_date: str
    author_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        from_attributes = True


class AuthorBase(BaseModel):
    name: str
    bio: str
    birth_date: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True