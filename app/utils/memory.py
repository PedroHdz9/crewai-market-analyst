from pathlib import Path


def get_previous_reports(topic, max_reports=3):

    reports_dir = Path("reports")

    if not reports_dir.exists():
        return []

    topic_words = topic.lower().split()

    matching_reports = []

    for file in reports_dir.rglob("*.md"):

        filename = file.stem.lower()

        if any(word in filename for word in topic_words):

            matching_reports.append(file)

    matching_reports.sort(
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )

    return matching_reports[:max_reports]

def load_previous_context(topic):

    reports = get_previous_reports(topic)

    if not reports:
        return "No hay informes previos."

    context = []

    for report in reports:

        try:

            with open(
                report,
                "r",
                encoding="utf-8"
            ) as f:

                content = f.read()

            context.append(
                f"""
INFORME ANTERIOR:
{report.name}

{content[:3000]}
"""
            )

        except Exception:
            pass

    return "\n\n".join(context)