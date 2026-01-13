from fastapi import APIRouter, HTTPException

from schemas import CoordinatesResponse, IP
from services import add_ip_location


router = APIRouter()


@router.post("/coordinates", response_model=CoordinatesResponse)
def add_ip(ip: IP):
    try:
        return add_ip_location(str(ip.ip_address))
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc



