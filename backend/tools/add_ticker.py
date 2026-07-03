"""
Purpose
-------
Insert a sample ticker into the database.

Responsibilities
----------------
- Create a database session.
- Insert one Ticker.
- Commit the transaction.

Depends On
----------
- SQLAlchemy
- Ticker model

Used By
-------
- Developers
"""

from app.database.database import SessionLocal
from app.models.ticker import Ticker

session = SessionLocal()


mu = Ticker(
    ticker="MU",
    company_name="Micron Technology",
    sector="Technology",
    industry="Semiconductors",
    country="USA",
    is_active=True,
)



session.add(mu)
session.commit()
session.close() 