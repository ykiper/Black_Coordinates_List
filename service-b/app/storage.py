import redis
from schemas import CoordinatesResponse
import os

REDIS_URL = os.getenv("REDIS_URL")

redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

def save_coordinates(coordinates: CoordinatesResponse, ip: str) -> None:
    redis_client.set(ip, coordinates.model_dump_json())

def get_all_coordinates() -> list[dict]:
    keys = redis_client.keys("*")
    result = []
    for key in keys:
        data = redis_client.get(key)
        if data:
            coord = CoordinatesResponse.model_validate_json(data)
            result.append({"ip": key, "lat": coord.lat, "lon": coord.lon})
    return result
