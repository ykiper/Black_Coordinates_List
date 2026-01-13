from fastapi import APIRouter
from schemas import IP


router = APIRouter()


@router.post
def add_ip(ip_address: IP):
    return ip_address

