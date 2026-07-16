from fastapi import FastAPI

from app.api import root, health, tickers
from app.database.base import Base
from app.database.database import engine

# Import models so SQLAlchemy registers them
from app.models.design import Design
from app.models.ticker import Ticker

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(root.router)
app.include_router(health.router)
app.include_router(tickers.router)
