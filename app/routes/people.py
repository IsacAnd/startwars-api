# app/routes/people.py
from fastapi import APIRouter, Query
from app.clients.swapi_client import get_people, get_person, get_resource_by_url
from app.services.people_service import (
    filter_people,
    sort_people,
    normalize_people
)

router = APIRouter()


@router.get("/")
def list_people(
    name: str = None,
    gender: str = None,
    sort: str = Query(None)
):
    data = get_people()
    results = data["results"]

    results = filter_people(results, name, gender)
    results = sort_people(results, sort)
    results = normalize_people(results)

    return {
        "count": len(results),
        "results": results
    }


@router.get("/{id}/full-profile")
def get_full_profile(id: int):
    person = get_person(id)
    films = [get_resource_by_url(f) for f in person["films"]]
    homeworld = get_resource_by_url(person["homeworld"])

    return {
        "person": normalize_people([person])[0],
        "homeworld": homeworld,
        "films": films
    }
