from app.clients.swapi_client import get_resource_by_url
from typing import List, Dict

def get_film_characters(film_data: dict) -> list[dict]:
    if "characters" not in film_data:
        return []

    characters = []
    for url in film_data["characters"]:
        character = get_resource_by_url(url)
        characters.append(character)

    return characters

