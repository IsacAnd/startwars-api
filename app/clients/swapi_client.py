import requests
from fastapi import HTTPException
from app.core.cache import get_cache, set_cache

BASE_URL = "https://swapi.dev/api"


def fetch(url: str):
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=502,
            detail="External service unavailable"
        )

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail="Error fetching external resource"
        )

    return response.json()


def get_with_cache(key: str, url: str):
    cached = get_cache(key)
    if cached:
        return cached

    data = fetch(url)
    set_cache(key, data)
    return data


def get_people(page: int = 1):
    return get_with_cache(
        f"people:page:{page}",
        f"{BASE_URL}/people?page={page}"
    )


def get_person(person_id: int):
    return get_with_cache(
        f"person:{person_id}",
        f"{BASE_URL}/people/{person_id}"
    )


def get_film(film_id: int):
    return get_with_cache(
        f"film:{film_id}",
        f"{BASE_URL}/films/{film_id}"
    )


def get_resource_by_url(url: str):
    return get_with_cache(url, url)