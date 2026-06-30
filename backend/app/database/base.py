"""
Purpose
-------
Defines the SQLAlchemy Declarative Base.

Responsibilities
----------------
- Create the application's Base class.
- Provide the parent class for all database models.

Depends On
----------
- SQLAlchemy ORM

Used By
-------
- Every model in app/models
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""
    pass