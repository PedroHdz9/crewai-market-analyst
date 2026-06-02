from pathlib import Path
from app.crew import run_crew
from datetime import datetime
import re

from app.utils.pdf_generator import generate_pdf

def sanitize_filename(text):
    text = text.lower()

    text = re.sub(r'[^\w\s-]', '', text)

    text = re.sub(r'\s+', '_', text)

    return text[:50]

topic = input("Tema: ")

result = run_crew(topic)

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
    f.write(str(result))

pdf_path = report_path.with_suffix(".pdf")

generate_pdf(
    str(result),
    str(pdf_path),
    topic
)

print(
    f"\nMarkdown: {report_path}"
)

print(
    f"PDF: {pdf_path}"
)