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

def get_all_reports():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        topic,
        created_at,
        market_opportunity,
        competitive_threat
    FROM reports
    ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_reports_by_topic(topic):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM reports
    WHERE topic = ?
    ORDER BY created_at DESC
    """, (topic,))

    rows = cursor.fetchall()

    conn.close()

    return rows

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

def get_all_reports():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        topic,
        created_at,
        market_opportunity,
        competitive_threat
    FROM reports
    ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_reports_by_topic(topic):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM reports
    WHERE topic = ?
    ORDER BY created_at DESC
    """, (topic,))

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_report_by_id(report_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM reports
    WHERE id = ?
    """, (report_id,))

    row = cursor.fetchone()

    conn.close()

    return row