#Responsible for everything related to ticker endpoints
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.ticker import TickerResponse
from app.schemas.ticker import TickerCreate
from app.services import ticker_service

router = APIRouter(
    prefix="/tickers",
    tags=["Tickers"]
)

@router.get(
        "",
        response_model=list[TickerResponse],
)
def get_tickers(
    db: Session = Depends(get_db),
    ):
    return ticker_service.get_active_tickers(db)

@router.post(
    "",
    response_model=TickerResponse,
)
def create_ticker(
    ticker_data: TickerCreate,
    db: Session = Depends(get_db)
):
    return ticker_service.create_ticker(db, ticker_data)