from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import (
    TA_CENTER
)


def add_page_number(canvas, doc):
    page_num = canvas.getPageNumber()

    canvas.drawRightString(
        550,
        20,
        f"Página {page_num}"
    )


def generate_pdf(
    content: str,
    output_path: str,
    topic: str
):

    doc = SimpleDocTemplate(
        output_path,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Title"],
        alignment=TA_CENTER
    )

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"]
    )

    body_style = styles["BodyText"]

    story = []

    # PORTADA

    story.append(
        Spacer(1, 100)
    )

    story.append(
        Paragraph(
            "Market Intelligence Report",
            title_style
        )
    )

    story.append(
        Spacer(1, 30)
    )

    story.append(
        Paragraph(
            topic,
            styles["Heading1"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            datetime.now().strftime(
                "%d/%m/%Y %H:%M"
            ),
            styles["Italic"]
        )
    )

    story.append(
        PageBreak()
    )

    # CONTENIDO

    for line in content.split("\n"):

        line = line.strip()

        if not line:
            story.append(
                Spacer(1, 8)
            )
            continue

        if line.startswith("# "):

            story.append(
                Paragraph(
                    line[2:],
                    styles["Heading1"]
                )
            )

            continue

        if line.startswith("## "):

            story.append(
                Paragraph(
                    line[3:],
                    heading_style
                )
            )

            continue

        if line.startswith("### "):

            story.append(
                Paragraph(
                    line[4:],
                    styles["Heading3"]
                )
            )

            continue

        story.append(
            Paragraph(
                line,
                body_style
            )
        )

    doc.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )