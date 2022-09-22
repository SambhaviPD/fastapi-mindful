from fastapi import FastAPI

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

]

app = FastAPI(title="Mindful API", openapi_url="/openapi.json")

@app.get("/", status_code=200)
async def root() -> dict:
    return {"message":"Welcome to Mindful API"}

@app.get("/books", status_code=200)
async def get_books() -> dict:
    result = [book for book in BOOKS]
    return {"books" : result}