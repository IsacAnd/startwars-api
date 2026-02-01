from fastapi import APIRouter, Query, HTTPException
from app.services.swapi_service import get_people

router = APIRouter()

ALLOWED_SORT_FIELDS = ["name", "height", "mass"]

@router.get("/people")
def list_people(
    name: str = None,
    gender: str = None,
    sort: str = Query(None, description="Campo para ordenação")
):
    if sort and sort not in ALLOWED_SORT_FIELDS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Allowed: {ALLOWED_SORT_FIELDS}"
        )

    data = get_people()
    results = data["results"]

    if name:
        results = [p for p in results if name.lower() in p["name"].lower()]

    if gender:
        results = [p for p in results if gender.lower() == p["gender"].lower()]

    if sort:
        results = sorted(results, key=lambda x: x.get(sort, ""))

    return {
        "count": len(results),
        "filters": {
            "name": name,
            "gender": gender,
            "sort": sort
        },
        "results": results
    }
