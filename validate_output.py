import os
from docx import Document

def validate():
    if not os.path.exists("web_pages_report.docx"):
        print("Error: web_pages_report.docx does not exist.")
        return False

    doc = Document("web_pages_report.docx")

    # We expect 25 headings of level 1
    h1_count = 0
    for para in doc.paragraphs:
        if para.style.name == 'Heading 1':
            h1_count += 1

    print(f"Found {h1_count} Heading 1 entries.")

    if h1_count == 25:
        print("Validation successful: All 25 tasks are represented.")
        return True
    else:
        print(f"Validation failed: Expected 25 Heading 1 entries, but found {h1_count}.")
        return False

if __name__ == "__main__":
    if validate():
        exit(0)
    else:
        exit(1)
