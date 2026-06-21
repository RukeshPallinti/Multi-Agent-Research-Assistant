import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from config import REPORTS_DIR


def generate_pdf_report(
    topic: str,
    report_content: str
):

    os.makedirs(
        REPORTS_DIR,
        exist_ok=True
    )

    safe_name = topic.replace(
        " ",
        "_"
    ).lower()

    file_path = os.path.join(
        REPORTS_DIR,
        f"{safe_name}_report.pdf"
    )

    doc = SimpleDocTemplate(
        file_path
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            topic,
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    sections = report_content.split("\n")

    for line in sections:

        line = line.strip()

        if not line:
            continue

        content.append(
            Paragraph(
                line,
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 6)
        )

    doc.build(content)

    return file_path