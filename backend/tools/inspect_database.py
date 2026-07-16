import os
import sys

from sqlalchemy import inspect
from sqlalchemy import select

from app.database.database import SessionLocal
from app.database.database import engine
from app.models.ticker import Ticker
from app.models.design import Design

print("cwd:", os.getcwd())
print("sys.path[0]:", sys.path[0])

session = SessionLocal()

inspector = inspect(engine)

tables = inspector.get_table_names()

for table in tables:
    print(f"\n{table.capitalize()} Table Columns")
    print("-" * 25)
    for column in inspector.get_columns(table):
        print(column["name"], column["type"])

tickers = session.scalars(select(Ticker)).all()

print("\nTickers")
print("--------")
for ticker in tickers:
    print(ticker)