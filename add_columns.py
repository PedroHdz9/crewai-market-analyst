import sqlite3

conn = sqlite3.connect("market_intelligence.db")

cursor = conn.cursor()

cursor.execute(
    "ALTER TABLE reports ADD COLUMN md_path TEXT"
)


conn.commit()

conn.close()

print("Columnas añadidas")