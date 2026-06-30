from fastapi import FastAPI
from app.database.base import Base
from app.database.database import engine
from app.models.ticker import Ticker

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