import fitz

def extract_text_boxes(pdf_path, replacements):
    doc = fitz.open(pdf_path)
    replacements_boxes = []

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" not in b: continue
            for l in b["lines"]:
                for s in l["spans"]:
                    for old, new in replacements.items():
                        if old in s["text"]:
                            bbox = s["bbox"]
                            replacements_boxes.append({
                                "page": page_num,
                                "bbox": bbox,
                                "new_text": s["text"].replace(old, new),
                                "font_size": s["size"]
                            })
    doc.close()
    return replacements_boxes
