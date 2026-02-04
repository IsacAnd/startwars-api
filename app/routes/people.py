from fastapi import APIRouter, Query, Depends
from app.core.auth import get_current_user
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
    sort: str = Query(None),
    user=Depends(get_current_user)
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

@router.get("/{id}")
def get_person_detail(id: int, user=Depends(get_current_user)):
    person = get_person(id)

    if "detail" in person:
        raise HTTPException(status_code=404, detail="Person not found")

    return normalize_people([person])[0]

@router.get("/{id}/full-profile")
def get_full_profile(id: int, user=Depends(get_current_user)):
    person = get_person(id)
    films = [get_resource_by_url(f) for f in person["films"]]
    homeworld = get_resource_by_url(person["homeworld"])

    return {
        "person": normalize_people([person])[0],
        "homeworld": homeworld,
        "films": films
    }
    
@router.get("/top-characters")
def top_characters(user=Depends(get_current_user)):
    films = [get_film(i) for i in range(1, 7)]
    counter = {}

    for film in films:
        for url in film["characters"]:
            counter[url] = counter.get(url, 0) + 1

    ranking = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    top = ranking[:10]

    result = []
    for url, count in top:
        char = get_resource_by_url(url)
        result.append({
            "name": char["name"],
            "films": count
        })

    return result
