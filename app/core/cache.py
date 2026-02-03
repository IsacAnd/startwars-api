import time
import os
from typing import Any, Dict

CACHE: Dict[str, tuple[Any, float]] = {}

CACHE_CONFIG = {
    "people": 60,
    "films": 300,
    "default": 120
}

def get_cache(key: str):
    if os.getenv("ENV") == "test":
        return None

    if key in CACHE:
        data, timestamp = CACHE[key]
        ttl = CACHE_CONFIG.get(key, CACHE_CONFIG["default"])
        if time.time() - timestamp < ttl:
            return data
    return None


def set_cache(key: str, data: Any):
    if os.getenv("ENV") == "test":
        return

    CACHE[key] = (data, time.time())
