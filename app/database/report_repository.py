from datetime import datetime

from app.database.db import get_connection

import os

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

def get_unique_topics():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT DISTINCT topic
    FROM reports
    ORDER BY topic
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_dashboard_stats():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM reports
    """)

    total_reports = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(DISTINCT topic)
    FROM reports
    """)

    total_topics = cursor.fetchone()[0]

    conn.close()

    return {
        "total_reports": total_reports,
        "total_topics": total_topics
    }

def delete_report(report_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT markdown_path, pdf_path
        FROM reports
        WHERE id = ?
    """, (report_id,))

    row = cursor.fetchone()

    if row:

        markdown_path = row[0]
        pdf_path = row[1]

        if markdown_path and os.path.exists(markdown_path):
            os.remove(markdown_path)

        if pdf_path and os.path.exists(pdf_path):
            os.remove(pdf_path)

    cursor.execute("""
        DELETE FROM reports
        WHERE id = ?
    """, (report_id,))

    conn.commit()

    conn.close()

def get_analytics_data():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            AVG(market_opportunity),
            AVG(competitive_threat),
            AVG(technology_maturity),
            AVG(regulatory_risk),
            AVG(investment_attractiveness)
        FROM reports
    """)

    averages = cursor.fetchone()

    conn.close()

    return {
        "opportunity": round(averages[0] or 0, 1),
        "threat": round(averages[1] or 0, 1),
        "technology": round(averages[2] or 0, 1),
        "risk": round(averages[3] or 0, 1),
        "investment": round(averages[4] or 0, 1),
    }

def get_top_opportunities(limit=10):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            topic,
            market_opportunity
        FROM reports
        ORDER BY market_opportunity DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_dashboard_stats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM reports"
    )

    total_reports = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(DISTINCT topic) FROM reports"
    )

    total_topics = cursor.fetchone()[0]

    conn.close()

    return {
        "total_reports": total_reports,
        "total_topics": total_topics
    }