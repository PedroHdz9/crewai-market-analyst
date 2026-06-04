from app.database.db import get_connection


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        topic TEXT NOT NULL,

        created_at TEXT NOT NULL,

        market_opportunity INTEGER,

        competitive_threat INTEGER,

        technology_maturity INTEGER,

        regulatory_risk INTEGER,

        investment_attractiveness INTEGER,

        markdown_path TEXT,

        pdf_path TEXT,

        md_path TEXT
    )
    """)

    conn.commit()
    conn.close()