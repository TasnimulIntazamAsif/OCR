import pytesseract
from PIL import Image
from pathlib import Path
from config import TESSERACT_PATH, LANGUAGE
custom_config = "--oem 3 --psm 6"

if TESSERACT_PATH:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def ocr_image(image_path, output_text_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang=LANGUAGE,config=custom_config)
    LANGUAGE = "eng+deu+fra"
    with open(output_text_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"OCR complete: {image_path.name}")
