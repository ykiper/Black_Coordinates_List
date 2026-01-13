import os

import requests

from schemas import CoordinatesResponse


IP_API_BASE_URL = "http://ip-api.com/json"
SERVICE_B_URL = os.getenv("SERVICE_B_URL", "http://service-b:8001/api/v1")


def get_ip_location(ip_address: str) -> CoordinatesResponse:
    response = requests.get(f"{IP_API_BASE_URL}/{ip_address}", timeout=10)
    response.raise_for_status()
    data = response.json()
    return CoordinatesResponse(lat=data["lat"], lon=data["lon"])


def add_ip_location(ip_address: str) -> CoordinatesResponse:
    coordinates = get_ip_location(ip_address)

    response = requests.post(
        f"{SERVICE_B_URL}/store-coordinates",
        params={"ip": ip_address},
        json=coordinates.model_dump(),
        timeout=10,
    )
    response.raise_for_status()

    return coordinates
