import requests

BASE_URL = "https://swapi.dev/api"

def get_people():
    response = requests.get(f"{BASE_URL}/people")
    return response.json()