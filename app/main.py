from fastapi import FastAPI

from typing import Optional

BOOKS = [
    {
        "id" : 1,
        "title" : "Nudge: Improving Decisions About Health, Wealth, and Happiness",
        "authors" : ["Richard H.Taler", "Cass R.Sunstein"],
        "rating" : 3.83,
        "genre" : ["Nonfiction", "Psychology", "Economics", "Self Help"],
        "numberofpages" : 260,
    },
    {
        "id" : 2,
        "title" : "Traffic: Why We Drive the Way We Do and What It Says About Us",
        "authors" : ["Tom Vanderbilt"],
        "rating" : 3.72,
        "genre" : ["Nonfiction", "Psychology", "Sociology", "Urban Planning"],
        "numberofpages" : 260,
    },
    {
        "id" : 3,
        "title" : "Patriot Games",
        "authors" : ["Tom Clancy"],
        "rating" : 4.15,
        "genre" : ["Fiction", "Thriller", "Mystery", "Suspense"],
        "numberofpages" : 260,
    },

]

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

@app.get("/books/search", status_code=200)
async def search_by_author_or_genre(keyword: Optional[str] = None, \
    max_results: Optional[int] = 5) -> dict:

    if not keyword:
        return BOOKS[:max_results]

    result = [book for book in BOOKS if any(keyword.lower() in authors.lower() for authors in book["authors"])] \
            or [book for book in BOOKS if any(keyword.lower() in genre.lower() for genre in book["genre"])]

    return {"books" : result}