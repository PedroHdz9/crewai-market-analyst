from datetime import datetime

from app.database.db import get_connection


def save_report(
    topic,
    markdown_path,
    pdf_path,
    market_opportunity,
    competitive_threat,
    technology_maturity,
    regulatory_risk,
    investment_attractiveness
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO reports (

        topic,
        created_at,

        market_opportunity,
        competitive_threat,
        technology_maturity,
        regulatory_risk,
        investment_attractiveness,

        markdown_path,
        pdf_path

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        topic,
        datetime.now().isoformat(),

        market_opportunity,
        competitive_threat,
        technology_maturity,
        regulatory_risk,
        investment_attractiveness,

        markdown_path,
        pdf_path
    ))

    conn.commit()
    conn.close()