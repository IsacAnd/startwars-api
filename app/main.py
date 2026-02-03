from fastapi import FastAPI
from app.routes import people, films
from app.core.security import api_key_middleware
from app.core.rate_limit import rate_limit_middleware

app = FastAPI(
    title="Star Wars API",
    description="API intermediária consumindo a SWAPI",
    version="1.0.0"
)

app.include_router(people.router, prefix="/people", tags=["People"])
app.include_router(films.router, prefix="/films", tags=["Films"])

app.middleware("http")(rate_limit_middleware)
app.middleware("http")(api_key_middleware)

@app.get("/")

def root():
    return {"message": "Star Wars API is running"}