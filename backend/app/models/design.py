"""
Purpose
-------
Defines the Design model.

Responsibilities
----------------
- Represents a generated design created by Alpha Apparel.
- Stores the creative inputs and resulting image location.
- Defines the database schema for the designs table.

Depends On
----------
- SQLAlchemy ORM
- Base class
- Ticker model

Used By
-------
- Design generation
- API endpoints
- Future admin tools
- Product generation workflows
"""

from datetime import datetime

from sqlalchemy import DateTime, String, Text
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base

class Design(Base):
    __tablename__ = "designs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticker_id: Mapped[int] = mapped_column(Integer, nullable=False)
    theme_id: Mapped[int] = mapped_column(Integer, nullable=False)
    style_id: Mapped[int] = mapped_column(Integer, nullable=False)
    humor_level_id: Mapped[int] = mapped_column(Integer, nullable=False)
    generation_prompt: Mapped[str] = mapped_column(
        Text, 
        nullable=False
    )
    image_location: Mapped[str] = mapped_column(
        String(512),
        nullable=False
    )
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
        return f"<Design(id={self.id}, ticker_id={self.ticker_id})>"