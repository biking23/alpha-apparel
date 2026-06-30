import os
import sys
from sqlalchemy import inspect

print("cwd:", os.getcwd())
print("sys.path[0]:", sys.path[0])

from app.database.database import engine



inspector = inspect(engine)

print(inspector.get_table_names())

for column in inspector.get_columns("tickers"):
    print(column["name"], column["type"])