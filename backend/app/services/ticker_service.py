"""
Purpose
-------
Business logic for ticker operations.

Responsibilities
----------------
- Retrieve active tickers ordered alphabetically by ticker symbol.
- Retrieve individual tickers.
- Encapsulate ticker-related business rules.

Depends On
----------
- SQLAlchemy
- Ticker model

Used By
-------
- API endpoints
- Future background jobs
- Admin tools
"""
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.ticker import Ticker
from app.schemas.ticker import TickerCreate
from fastapi import HTTPException


def get_active_tickers(db: Session) -> list[Ticker]:
    """
    Retrieve all active tickers.
    """
    statement = (
        select(Ticker)
        .where(Ticker.is_active)
        .order_by(Ticker.ticker)
    )

    return db.scalars(statement).all()

def create_ticker(db: Session, ticker_data: TickerCreate) -> Ticker:
    #check for existing ticker
    statement = (
        select(Ticker)
        .where(Ticker.ticker == ticker_data.ticker)
    )
    ticker = db.scalar(statement)
    if ticker:
        raise HTTPException(
            status_code=409,
            detail=f"Ticker '{ticker_data.ticker}' already exists.",
            )
    # Create a new Ticker object
    ticker = Ticker(
        ticker=ticker_data.ticker,
        company_name=ticker_data.company_name,
        sector=ticker_data.sector,
        industry=ticker_data.industry,
        country=ticker_data.country,
        is_active=True
    )
    # Add to database
    db.add(ticker)
    # Commit transaction
    db.commit()   
    # Refresh object
    db.refresh(ticker)
    # Return ticker
    return ticker