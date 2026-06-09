from pathlib import Path
from app.crew import run_crew
from datetime import datetime
import re

from app.utils.pdf_generator import generate_pdf
from app.database.models import create_tables
from app.utils.score_parser import extract_score
from app.database.report_repository import save_report


def sanitize_filename(text):
    text = text.lower()

    text = re.sub(r'[^\w\s-]', '', text)

    text = re.sub(r'\s+', '_', text)

    return text[:50]

create_tables()

topic = input("Tema: ").strip()

result = run_crew(topic)

report_text = str(result)

market_opportunity = extract_score(
    report_text,
    "Market Opportunity Score"
)

competitive_threat = extract_score(
    report_text,
    "Competitive Threat Score"
)

technology_maturity = extract_score(
    report_text,
    "Technology Maturity Score"
)

regulatory_risk = extract_score(
    report_text,
    "Regulatory Risk Score"
)

investment_attractiveness = extract_score(
    report_text,
    "Investment Attractiveness Score"
)

Path("reports").mkdir(exist_ok=True)

safe_topic = sanitize_filename(topic)

today = datetime.now().strftime(
    "%Y-%m-%d"
)

timestamp = datetime.now().strftime(
    "%H%M%S"
)

daily_folder = Path("reports") / today

daily_folder.mkdir(
    parents=True,
    exist_ok=True
)

filename = (
    f"{safe_topic}_{timestamp}.md"
)

report_path = daily_folder / filename

with open(
    report_path,
    "w",
    encoding="utf-8"
) as f:
    f.write(report_text)

pdf_path = report_path.with_suffix(".pdf")

generate_pdf(
    report_text,
    str(pdf_path),
    topic
)

if None in [
    market_opportunity,
    competitive_threat,
    technology_maturity,
    regulatory_risk,
    investment_attractiveness
]:
    print(
        "\n Algunos scores no pudieron extraerse."
    )

save_report(
    topic,
    str(report_path),
    str(pdf_path),

    market_opportunity,
    competitive_threat,
    technology_maturity,
    regulatory_risk,
    investment_attractiveness
)

print(
    f"\nMarkdown: {report_path}"
)

print(
    f"PDF: {pdf_path}"
)