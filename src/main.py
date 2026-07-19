# src/main.py
import os
from convert import pdf_to_tif
from compare import compare_images

# Paths
DATA_FOLDER = "data"
OUTPUT_FOLDER = "output"

def main():
    base_pdf = os.path.join(DATA_FOLDER, "A_BASE.pdf")
    output_pdf = os.path.join(DATA_FOLDER, "A_OUTPUT.pdf")

    base_tif = os.path.join(OUTPUT_FOLDER, "A_BASE.tif")
    output_tif = os.path.join(OUTPUT_FOLDER, "A_OUTPUT.tif")
    compare_tif = os.path.join(OUTPUT_FOLDER, "A_COMPARE.tif")

    # Step 1: Convert PDFs to TIFFs
    pdf_to_tif(base_pdf, base_tif)
    pdf_to_tif(output_pdf, output_tif)

    # Step 2: Compare TIFFs
    compare_images(base_tif, output_tif, compare_tif)

if __name__ == "__main__":
    main()
