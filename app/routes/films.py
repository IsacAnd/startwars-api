from fastapi import APIRouter, HTTPException
from app.clients.swapi_client import get_film, get_resource_by_url

router = APIRouter()

@router.get("/{film_id}/characters")
def get_film_characters(film_id: int):
    film = get_film(film_id)

    if "detail" in film:
        raise HTTPException(status_code=404, detail="Film not found")
    
    MAX_CHARACTERS = 20

    characters_urls = film["characters"][:MAX_CHARACTERS]
    characters = []

    for url in characters_urls:
        character = get_resource_by_url(url)
        characters.append(character)

    return {
        "film": film["title"],
        "count": len(characters),
        "characters": characters
    }
