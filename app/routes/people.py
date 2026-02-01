from fastapi import APIRouter
from app.services.swapi_service import get_people

router = APIRouter()

@router.get("/people")
def list_people():
    data = get_people()
    return {
        "count": data["count"],
        "results": data["results"]
    }
