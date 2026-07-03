"""
Purpose
-------
Defines API schemas for ticker data.

Responsibilities
----------------
- Validate incoming ticker data.
- Define outgoing ticker responses.
- Separate API contracts from database models.

Depends On
----------
- Pydantic

Used By
-------
- FastAPI endpoints
"""
from datetime import datetime
from pydantic import BaseModel
from pydantic import ConfigDict


class TickerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    ticker: str
    company_name: str
    sector: str
    industry: str
    country: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

