import subprocess
from pathlib import Path

def ocr_pdf(input_pdf, output_pdf):
    subprocess.run([
        "ocrmypdf",
        "--force-ocr",
        "--optimize", "3",
        input_pdf,
        output_pdf
    ], check=True)

    print(f"OCR PDF complete: {input_pdf.name}")
