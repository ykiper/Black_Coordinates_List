from pydantic import BaseModel
from ipaddress import IPv4Address


class IP(BaseModel):
    ip_address: IPv4Address

class CoordinatesResponse(BaseModel):
    lat: float
    lon: float