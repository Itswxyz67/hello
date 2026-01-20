import os
from docx import Document

def validate():
    if not os.path.exists("cpp_practicals_report.docx"):
        print("Error: cpp_practicals_report.docx does not exist.")
        return False

    doc = Document("cpp_practicals_report.docx")
    h1_count = 0
    for para in doc.paragraphs:
        if para.style.name == 'Heading 1':
            h1_count += 1

    print(f"Found {h1_count} Heading 1 entries.")
    if h1_count == 14:
        print("Validation successful: All 14 practicals are represented.")
        return True
    else:
        print(f"Validation failed: Expected 14 Heading 1 entries, but found {h1_count}.")
        return False

if __name__ == "__main__":
    if validate():
        exit(0)
    else:
        exit(1)
