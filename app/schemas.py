from pydantic import BaseModel

class Author(BaseModel):
    id: int
    name: str
    genre: list[str]

class AuthorCreate(BaseModel):
    name: str
    genre: list[str]

class AuthorUpdate(BaseModel):
    genre: list[str]

class Book(BaseModel):
    id: int
    title: str
    authors: list[Author]
    rating: float
    genre: list[str]
    numberofpages: int

class BookCreate(BaseModel):
    title: str
    authors: list[Author]
    rating: float
    genre: list[str]
    numberofpages: int

class BookUpdate(BaseModel):
    title: str
    genre: list[str]