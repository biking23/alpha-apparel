#responsible for Root landing point
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "application": "Alpha Apparel",
        "status": "online"
    }