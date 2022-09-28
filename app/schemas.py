from pydantic import BaseModel, Field

class Author(BaseModel):
    id: int
    name: str
    genre: list[str] = Field(min_items=1, max_items=5)

class AuthorCreate(BaseModel):
    name: str
    genre: list[str] = Field(min_items=1, max_items=5)

class AuthorUpdate(BaseModel):
    genre: list[str] = Field(min_items=1, max_items=5)

class Book(BaseModel):
    id: int
    title: str = Field(description="Title of the book", max_length=200)
    authors: list[Author] = Field(min_items=1)
    rating: float = Field(gt=0, description="Rating must be greater than zero")
    genre: list[str] = Field(min_items=1, max_items=5)
    numberofpages: int = Field(gt=0, description="Number of pages must be greater than zero")

class BookCreate(BaseModel):
    title: str = Field(description="Title of the book", max_length=200)
    authors: list[Author]
    rating: float = Field(gt=0, description="Rating must be greater than zero")
    genre: list[str] = Field(min_items=1, max_items=5)
    numberofpages: int = Field(gt=0, description="Number of pages must be greater than zero")

class BookUpdate(BaseModel):
    title: str = Field(description="Title of the book", max_length=200)
    genre: list[str] = Field(min_items=1, max_items=5)