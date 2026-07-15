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
from app.services.ticker_service import create_ticker

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

def test_create_ticker_creates_active_ticker():
    
    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(bind=engine)

    session = SessionLocal()

    try:
        from app.schemas.ticker import TickerCreate

        ticker_data = TickerCreate(
            ticker="TSM",
            company_name="Taiwan Semiconductor Manufacturing",
            sector="Technology",
            industry="Semiconductors",
            country="Taiwan",
        )

        new_ticker = create_ticker(session, ticker_data)

        assert new_ticker.ticker == "TSM"
        assert new_ticker.is_active is True
    finally:
        session.close()