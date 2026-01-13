from fastapi import APIRouter
from schemas import IP
from services import add_ip_location


router = APIRouter()


@router.post
def add_ip(ip_address: IP):
    return add_ip_location()



