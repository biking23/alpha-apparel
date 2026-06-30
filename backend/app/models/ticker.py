"""
Purpose
-------
Defines the Ticker model.

Responsibilities
----------------
- Represents publicly traded companies supported by Alpha Apparel.
- Defines the database schema for the tickers table.

Depends On
----------
- SQLAlchemy ORM
- Base class

Used By
-------
- Design generation
- API endpoints
- Future admin tools
"""
from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base

class Ticker(Base):
    __tablename__ = "tickers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticker: Mapped[str] = mapped_column(
        String(10),
        unique = True,
        nullable = False
    )
    company_name: Mapped[str] = mapped_column(
        String(255), 
        nullable=False
    )
    sector: Mapped[str]
    industry: Mapped[str]
    country: Mapped[str]
    is_active: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<Ticker(symbol='{self.ticker}')>"
