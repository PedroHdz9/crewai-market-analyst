import markdown

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.database.report_repository import (
    get_all_reports,
    get_reports_by_topic,
    get_report_by_id
)

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="app/dashboard/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/dashboard/templates"
)


@app.get("/")
def home(request: Request):

    reports = get_all_reports()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "reports": reports
        }
    )


@app.get("/topic/{topic}")
def topic_page(
    request: Request,
    topic: str
):

    reports = get_reports_by_topic(topic)

    return templates.TemplateResponse(
        request=request,
        name="report.html",
        context={
            "topic": topic,
            "reports": reports
        }
    )

@app.get("/report/{report_id}")
def report_detail(
    request: Request,
    report_id: int
):

    report = get_report_by_id(report_id)

    if not report:
        return {"error": "Report not found"}

    markdown_path = report[8]

    with open(
        markdown_path,
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    html_content = markdown.markdown(
    content,
    extensions=[
        "tables",
        "fenced_code"
    ]
)

    return templates.TemplateResponse(
        request=request,
        name="report_detail.html",
        context={
            "report": report,
            "content": html_content
        }
    )

@app.get("/download/pdf/{report_id}")
def download_pdf(report_id: int):

    report = get_report_by_id(report_id)

    return FileResponse(
        path=report[9],
        filename="report.pdf",
        media_type="application/pdf"
    )

@app.get("/download/md/{report_id}")
def download_markdown(report_id: int):

    report = get_report_by_id(report_id)

    return FileResponse(
        path=report[8],
        filename="report.md",
        media_type="text/markdown"
    )