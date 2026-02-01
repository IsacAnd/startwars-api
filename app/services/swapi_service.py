import requests

BASE_URL = "https://swapi.dev/api"

def get_people():
    response = requests.get(f"{BASE_URL}/people")
    return response.json()

def get_film(film_id: int):
    response = requests.get(f"{BASE_URL}/films/{film_id}")
    return response.json()

def get_resource_by_url(url: str):
    response = requests.get(url)
    return response.json()
