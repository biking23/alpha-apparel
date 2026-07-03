#Responsible for everything related to ticker endpoints
from fastapi import APIRouter, Depends

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.ticker import Ticker
from app.schemas.ticker import TickerResponse

router = APIRouter(
    prefix="/tickers",
    tags=["Tickers"]
)

@router.get(
        "",
        response_model=list[TickerResponse]
        )
def get_tickers(db: Session = Depends(get_db)):
    all_tickers = db.scalars(select(Ticker)).all()
    return all_tickers