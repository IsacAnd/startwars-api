from fastapi import HTTPException
from app.core.validators import validate_sort
from app.schemas.responses import normalize_person

def filter_people(results: list[dict], name: str | None, gender: str | None):
    if name:
        results = [
            p for p in results
            if name.lower() in p["name"].lower()
        ]

    if gender:
        results = [
            p for p in results
            if gender.lower() == p["gender"].lower()
        ]

    return results


def sort_people(results: list[dict], sort: str | None):
    if not sort:
        return results

    validate_sort("people", sort)

    return sorted(
        results,
        key=lambda x: x.get(sort, "")
    )


def normalize_people(results: list[dict]):
    return [normalize_person(p) for p in results]
