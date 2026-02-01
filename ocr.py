from pathlib import Path
import pytesseract
from PIL import Image
import subprocess

# ---------- CONFIG ----------
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Languages (ONLY include what you need)
LANG = "eng+urd+ara"

# OCR configuration (important for ID cards / mixed text)
CUSTOM_CONFIG = r"--oem 3 --psm 11"

INPUT_IMAGES = Path(r"C:\Users\user\Downloads\image")
INPUT_PDFS = Path(r"C:\Users\user\Downloads\pdf")

OUTPUT_TEXT = Path("output/text")
OUTPUT_PDF = Path("output/pdf")

OUTPUT_TEXT.mkdir(parents=True, exist_ok=True)
OUTPUT_PDF.mkdir(parents=True, exist_ok=True)

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
# ----------------------------

print("\n🔍 OCR STARTED\n")

# ---------- IMAGE OCR ----------
for img_path in INPUT_IMAGES.iterdir():
    if img_path.suffix.lower() in [".png", ".jpg", ".jpeg", ".tiff", ".bmp"]:
        print(f"📷 Processing image: {img_path.name}")

        # Convert to grayscale for better OCR
        img = Image.open(img_path).convert("L")

        text = pytesseract.image_to_string(
            img,
            lang=LANG,
            config=CUSTOM_CONFIG
        )

        out_txt = OUTPUT_TEXT / f"{img_path.stem}.txt"
        out_txt.write_text(text, encoding="utf-8")

        print(f"✅ Text saved → {out_txt}")

# ---------- PDF OCR ----------
for pdf_path in INPUT_PDFS.glob("*.pdf"):
    print(f"📄 Processing PDF: {pdf_path.name}")

    out_pdf = OUTPUT_PDF / pdf_path.name
    txt_output = OUTPUT_TEXT / f"{pdf_path.stem}.txt"

    subprocess.run([
        "ocrmypdf",
        "--force-ocr",
        "--language", LANG,
        "--sidecar", str(txt_output),
        str(pdf_path),
        str(out_pdf)
    ], check=True)

    print(f"✅ Searchable PDF saved → {out_pdf}")
    print(f"✅ Text extracted → {txt_output}")

print("\n🎉 OCR COMPLETED SUCCESSFULLY\n")
