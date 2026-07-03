from fastapi import FastAPI

from app.api import root, health, tickers

app = FastAPI()

app.include_router(root.router)
app.include_router(health.router)
app.include_router(tickers.router)
