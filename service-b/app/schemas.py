from pydantic import BaseModel

class CoordinatesResponse(BaseModel):
    ip: str
    lat: float
    lon: float