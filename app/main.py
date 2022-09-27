from fastapi import FastAPI, HTTPException

from data import BOOKS
from schemas import Book, BookCreate, BookUpdate

from typing import Optional

app = FastAPI(title="Mindful API", openapi_url="/openapi.json")

@app.get("/", status_code=200)
async def root() -> dict:
    return {"message":"Welcome to Mindful API"}

@app.get("/books", status_code=200)
async def get_books() -> dict:
    result = [book for book in BOOKS]
    return {"books" : result}

@app.get("/book/{book_id}", status_code=200)
async def get_book_by_id(book_id:int) -> dict:
    result = [ book for book in BOOKS if book["id"] == book_id]
    return {"book" : result}

@app.get("/books/search/", status_code=200)
async def search_by_author_or_genre(keyword: Optional[str] = None, \
    max_results: Optional[int] = 5) -> dict:

    if not keyword:
        return BOOKS[:max_results]

    result = [book for book in BOOKS if any(keyword.lower() in authors.lower() \
                for authors in book["authors"])] \
            or [book for book in BOOKS if any(keyword.lower() in genre.lower() \
                for genre in book["genre"])]

    if len(result) == 0:
        raise HTTPException(status_code=404, \
            detail=f"Sorry, no books match your search criteria of {keyword}!")

    return {"books" : result}

@app.post("/book/", status_code=201, response_model=Book)
async def create_book(book: BookCreate) -> dict:
    id = len(BOOKS) + 1
    book = Book(
        id = id,
        title = book.title,
        authors = book.authors,
        rating = book.rating,
        genre = book.genre,
        numberofpages = book.numberofpages
    )
    BOOKS.append(book.dict())

    return book

@app.put("/book/{book_id}", status_code=200, response_model=Book)
async def update_book(book_id:int, updated_book: BookUpdate) -> dict:
    book = list(filter(lambda item: item['id'] == book_id, BOOKS))

    if len(book) == 0:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found!")
    else:
        book[0]["title"] = updated_book.title
        book[0]["genre"] = updated_book.genre
        return book[0]

@app.delete("/book/{book_id}", status_code=204)
async def delete_book(book_id: int):
    book = list(filter(lambda item: item['id'] == book_id, BOOKS))

    BOOKS.remove(book[0])