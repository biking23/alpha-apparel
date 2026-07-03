from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database.base import Base
from app.database.dependencies import get_db
from app.database.database import engine
from app.models.ticker import Ticker
from app.schemas.ticker import TickerResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {
        "application": "Alpha Apparel",
        "status": "online"
    }

@app.get("/health")
def health():   
    return {
        "status": "healthy"
    }

@app.get("/tickers",response_model=list[TickerResponse])
def get_tickers(db: Session = Depends(get_db)):
    all_tickers = db.scalars(select(Ticker)).all()
    return all_tickers