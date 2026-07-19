import fitz  # PyMuPDF
from PIL import Image

def pdf_to_tif(pdf_path, tif_path):
    doc = fitz.open(pdf_path)
    # Take first page only (expand later if multi-page)
    page = doc[0]
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img.save(tif_path, "TIFF")
