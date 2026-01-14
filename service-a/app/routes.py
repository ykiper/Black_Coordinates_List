from fastapi import APIRouter, HTTPException

from schemas import CoordinatesResponse, IP
from services import add_ip_location


router = APIRouter()


@router.post("/add_ip")
def add_ip(ip_address: IP):
    return add_ip_location(ip_address)



