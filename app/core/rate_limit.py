from fastapi import Request
from fastapi.responses import JSONResponse
import time

REQUESTS = {}
LIMIT = 10
WINDOW = 10  # segundos

async def rate_limit_middleware(request: Request, call_next):
    ip = request.client.host
    now = time.time()

    history = REQUESTS.get(ip, [])
    history = [t for t in history if now - t < WINDOW]

    if len(history) >= LIMIT:
        return JSONResponse(
            status_code=429,
            content={"detail": "Rate limit exceeded"}
        )

    history.append(now)
    REQUESTS[ip] = history
    return await call_next(request)
