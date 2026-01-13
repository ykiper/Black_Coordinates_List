from fastapi import APIRouter 
from storage import save_coordinates, get_all_coordinates
from schemas import CoordinatesResponse

router = APIRouter()

@router.post("/store-coordinates")
def store_coordinates(coordinates: CoordinatesResponse, ip: str):
    save_coordinates(coordinates, ip)
    return {"ip": ip, **coordinates.model_dump()}

@router.get("/coordinates")
def list_coordinates():
    return get_all_coordinates()