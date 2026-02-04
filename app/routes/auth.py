from fastapi import APIRouter, HTTPException
from app.core.auth import create_access_token

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    if username != "admin" or password != "123":
        raise HTTPException(401, "Invalid credentials")
    
    token = create_access_token({"sub": username})
    return {"access_token": token}
