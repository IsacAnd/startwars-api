from fastapi import Request, HTTPException
from app.core.settings import API_KEY

async def api_key_middleware(request: Request, call_next):
    api_key = request.headers.get("x-api-key")

    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    response = await call_next(request)
    return response
