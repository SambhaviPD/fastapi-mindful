"""
Holds Pydantic Models
"""

from pydantic import BaseModel, Field

class AuthorBase(BaseModel):
    name: str
    genre: list[str] = Field(min_items=1, max_items=5)

class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    addedby_id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str = Field(description="Title of the book", max_length=200)
    authors: list[Author] = Field(min_items=1)
    rating: float = Field(gt=0, description="Rating must be greater than zero")
    genre: list[str] = Field(min_items=1, max_items=5)
    numberofpages: int = Field(gt=0, description="Number of pages must be greater than zero")

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str = Field(description="Title of the book", max_length=200)
    genre: list[str] = Field(min_items=1, max_items=5)

class Book(BookBase):
    id: int
    addedby_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str
    is_active: bool

class UserCreate(UserBase):
    password: str

class UserUpdate(UserCreate):
    password: str

class User(UserBase):
    id: int
    authors = list[Author] = []
    books = list[Book] = []

    class Config:
        orm_mode = True

