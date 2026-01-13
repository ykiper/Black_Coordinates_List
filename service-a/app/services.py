from schemas import IP, CoordinatesResponse
import requests


def get_ip_location(ip_address):
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    loc_tuple = response.json()["lat"], response.json()["lon"]
    return loc_tuple



def add_ip_location(ip_address):
    loc_tuple = get_ip_location(ip_address)
    requests.post("http://127.0.0.1:8001", loc_tuple[0], loc_tuple[1])
