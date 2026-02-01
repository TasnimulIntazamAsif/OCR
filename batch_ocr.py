from pathlib import Path
from ocr_images import ocr_image
from ocr_pdfs import ocr_pdf

INPUT_IMAGES = Path("C:/Users/user/Downloads/images")
INPUT_PDFS = Path("C:/Users/user/Downloads/National_ID_Card")

OUTPUT_TEXT = Path("output/text")
OUTPUT_PDF = Path("output/pdf")

OUTPUT_TEXT.mkdir(parents=True, exist_ok=True)
OUTPUT_PDF.mkdir(parents=True, exist_ok=True)

# Process images
for image_file in INPUT_IMAGES.glob("*"):
    if image_file.suffix.lower() in [".png", ".jpg", ".jpeg", ".tiff"]:
        output_txt = OUTPUT_TEXT / f"{image_file.stem}.txt"
        ocr_image(image_file, output_txt)

# Process PDFs
for pdf_file in INPUT_PDFS.glob("*.pdf"):
    output_pdf = OUTPUT_PDF / pdf_file.name
    ocr_pdf(str(pdf_file), str(output_pdf))

print("Batch OCR completed.")
