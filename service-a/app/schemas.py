from ipaddress import IPv4Address

from pydantic import BaseModel


class IP(BaseModel):
    ip_address: IPv4Address

class CoordinatesResponse(BaseModel):
    lat: float
    lon: float