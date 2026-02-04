import os
import json
import redis
from typing import Any

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

CACHE_CONFIG = {
    "people": 60,
    "films": 300,
    "default": 120
}

def _get_ttl_from_key(key: str) -> int:
    if key.startswith("people"):
        return CACHE_CONFIG["people"]
    if key.startswith("film"):
        return CACHE_CONFIG["films"]
    return CACHE_CONFIG["default"]


def get_cache(key: str):
    if os.getenv("ENV") == "test":
        return None

    data = r.get(key)
    if data:
        return json.loads(data)
    return None


def set_cache(key: str, data: Any):
    if os.getenv("ENV") == "test":
        return

    ttl = _get_ttl_from_key(key)
    r.setex(key, ttl, json.dumps(data))
