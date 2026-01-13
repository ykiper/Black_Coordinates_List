from pydantic import BaseModel

class CoordinatesResponse(BaseModel):
    lat: float
    lon: float 



