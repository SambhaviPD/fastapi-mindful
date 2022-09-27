from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    authors: list[str]
    rating: float
    genre: list[str]
    numberofpages: int

class BookCreate(BaseModel):
    title: str
    authors: list[str]
    rating: float
    genre: list[str]
    numberofpages: int

class BookUpdate(BaseModel):
    title: str
    genre: list[str]