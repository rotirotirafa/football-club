from sqlalchemy import text

from src.infra.adapters.database.base import engine

conn = engine.connect()
with conn:
    result = conn.execute(text("SELECT * FROM roles"))

    for row in result.mappings():
        print("Opa:", row["name"])
