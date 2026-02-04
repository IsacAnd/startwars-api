from fastapi import APIRouter
from app.services.analytics_service import (
    gender_distribution,
    average_height
)

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/gender-distribution")
def get_gender_distribution():
    return gender_distribution()

@router.get("/average-height")
def get_average_height():
    return average_height()
