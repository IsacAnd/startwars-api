from fastapi import HTTPException
from typing import Optional

ALLOWED_SORT_FIELDS = {
    "people": ["name", "height", "mass"],
    "films": ["title", "release_date"]
}

def validate_sort(resource: str, field: Optional[str]):
    if field is None:
        return

    if field not in ALLOWED_SORT_FIELDS.get(resource, []):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Allowed: {ALLOWED_SORT_FIELDS[resource]}"
        )