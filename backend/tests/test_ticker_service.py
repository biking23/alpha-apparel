"""
Purpose
-------
Unit tests for ticker business logic.

Responsibilities
----------------
- Verify ticker service behavior.
- Protect business rules.

Used By
-------
- pytest
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.base import Base
from app.models.ticker import Ticker
from app.services.ticker_service import get_active_tickers

def test_get_active_tickers_returns_only_active_tickers():

    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(bind=engine)

    session = SessionLocal()

    session.add_all(
        [
            Ticker(
                ticker="MU",
                company_name="Micron",
                sector="Technology",
                industry="Semiconductors",
                country="USA",
                is_active=True,
            ),
            Ticker(
                ticker="OLD",
                company_name="Old Company",
                sector="Technology",
                industry="Semiconductors",
                country="USA",
                is_active=False,
            ),
        ]
    )

    session.commit()

    active = get_active_tickers(session)
    try:
        assert len(active) == 1
        assert active[0].ticker == "MU"
    finally:
        session.close()