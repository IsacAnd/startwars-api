from fastapi import APIRouter, HTTPException, Depends
from app.core.auth import get_current_user
from app.clients.swapi_client import (
    get_films,
    get_film,
    get_resource_by_url
)

router = APIRouter()

@router.get("/")
def list_films(user=Depends(get_current_user)):
    data = get_films()
    results = data["results"]

    return {
        "count": len(results),
        "results": results
    }

@router.get("/{id}")
def get_film_detail(id: int, user=Depends(get_current_user)):
    film = get_film(id)

    if "detail" in film:
        raise HTTPException(status_code=404, detail="Film not found")

    return film

@router.get("/{id}/characters")
def get_film_characters(id: int, user=Depends(get_current_user)):
    film = get_film(id)

    if "detail" in film:
        raise HTTPException(status_code=404, detail="Film not found")

    MAX_CHARACTERS = 20

    characters_urls = film["characters"][:MAX_CHARACTERS]
    characters = [get_resource_by_url(url) for url in characters_urls]

    return {
        "film": film["title"],
        "count": len(characters),
        "characters": characters
    }
