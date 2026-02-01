from fastapi import FastAPI
from app.routes import people, films

app = FastAPI(
    title="Star Wars API",
    description="API intermediária consumindo a SWAPI",
    version="1.0.0"
)

app.include_router(people.router)
app.include_router(films.router)

@app.get("/")

def root():
    return {"message": "Star Wars API is running"}