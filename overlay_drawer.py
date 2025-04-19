from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfReader

def draw_overlay(src_pdf, replacements, out_pdf):
    reader = PdfReader(src_pdf)
    pagesize = reader.pages[0].mediabox
    width = float(pagesize.width)
    height = float(pagesize.height)

    from reportlab.pdfgen.canvas import Canvas

    c = Canvas(out_pdf, pagesize=(width, height))
    for item in replacements:
        if item["page"] != 0:
            continue  # single page for now
        x0, y0, x1, y1 = item["bbox"]
        c.setFillColorRGB(1, 1, 1)
        c.rect(x0, height - y1, x1 - x0, y1 - y0, stroke=0, fill=1)
        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica", item["font_size"])
        c.drawString(x0, height - y1 + 2, item["new_text"])
    c.save()