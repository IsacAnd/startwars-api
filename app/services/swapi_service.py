import requests
import time

BASE_URL = "https://swapi.dev/api"
CACHE = {}
CACHE_TTL = 75  # 1.25 min


def get_with_cache(key: str, url: str, ttl: int = CACHE_TTL):
    now = time.time()

    if key in CACHE:
        cached_data, timestamp = CACHE[key]
        if now - timestamp < ttl:
            return cached_data

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        if key in CACHE:
            return CACHE[key][0]  # fallback
        raise

    CACHE[key] = (data, now)
    return data


def get_people():
    return get_with_cache(
        key="people",
        url=f"{BASE_URL}/people"
    )


def get_film(film_id: int):
    return get_with_cache(
        key=f"film_{film_id}",
        url=f"{BASE_URL}/films/{film_id}"
    )


def get_resource_by_url(url: str):
    return get_with_cache(
        key=url,  # a própria URL como chave
        url=url
    )
