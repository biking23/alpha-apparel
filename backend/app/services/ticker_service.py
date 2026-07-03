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