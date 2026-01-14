import requests
from schemas import CoordinatesResponse

def get_ip_location(ip: IP):
    response = requests.get(f"http://ip-api.com/json/{ip.ip_address}")
    loc_tuple = response.json()["lat"], response.json()["lon"]
    return loc_tuple


def add_ip_location(ip: IP):
    lat, lon = get_ip_location(ip)
    coord = CoordinatesResponse(lat=lat, lon=lon)
    requests.post("http://service-b:8001/api/v1/store-coordinates", json=coord.model_dump(), params={"ip": str(ip.ip_address)})



