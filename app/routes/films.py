from fastapi import APIRouter, HTTPException
from app.services.swapi_service import get_film, get_resource_by_url

router = APIRouter()

@router.get("/films/{film_id}/characters")
def get_film_characters(film_id: int):
    film = get_film(film_id)

    if "detail" in film:
        raise HTTPException(status_code=404, detail="Film not found")

    characters_urls = film["characters"]
    characters = []

    for url in characters_urls:
        character = get_resource_by_url(url)
        characters.append(character)

    return {
        "film": film["title"],
        "count": len(characters),
        "characters": characters
    }
