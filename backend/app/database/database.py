"""
Purpose
-------
Creates the database engine and session factory.

Responsibilities
----------------
- Read database configuration.
- Create the SQLAlchemy engine.
- Create database sessions.

Depends On
----------
- SQLAlchemy
- Environment variables

Used By
-------
- API routes
- Services
- Database models
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./alpha_apparel.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)