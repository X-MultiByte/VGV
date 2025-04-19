from PyPDF2 import PdfReader, PdfWriter

def merge_pdf_with_overlay(base_pdf_path, overlay_pdf_path, output_pdf_path):
    base = PdfReader(base_pdf_path)
    overlay = PdfReader(overlay_pdf_path)
    writer = PdfWriter()

    for base_page, overlay_page in zip(base.pages, overlay.pages):
        base_page.merge_page(overlay_page)
        writer.add_page(base_page)

    with open(output_pdf_path, "wb") as f:
        writer.write(f)
