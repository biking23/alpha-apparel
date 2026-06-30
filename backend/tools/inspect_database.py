import os
import sys
from sqlalchemy import inspect
from sqlalchemy import select
from app.database.database import SessionLocal
from app.database.database import engine
from app.models.ticker import Ticker

print("cwd:", os.getcwd())
print("sys.path[0]:", sys.path[0])

session = SessionLocal()

inspector = inspect(engine)

print(inspector.get_table_names())

for column in inspector.get_columns("tickers"):
    print(column["name"], column["type"])

tickers = session.scalars(select(Ticker)).all()

print("\nTickers")
print("--------")
for ticker in tickers:
    print(ticker)