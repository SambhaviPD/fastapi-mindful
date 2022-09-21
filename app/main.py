from fastapi import FastAPI

app = FastAPI(title="Mindful API", openapi_url="/openapi.json")

@app.get("/")
async def root():
    return {"message":"Welcome to Mindful API"}