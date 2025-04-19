from extract import extract_text_boxes
from overlay_drawer import draw_overlay
from pdf_merger import merge_pdf_with_overlay
from pdfa_converter import convert_to_pdfa
import os

def main():
    input_folder = "input"
    output_folder = "output"
    for fname in os.listdir(input_folder):
        if fname.endswith(".pdf"):
            src_pdf = os.path.join(input_folder, fname)
            overlay_pdf = os.path.join(output_folder, f"overlay_{fname}")
            merged_pdf = os.path.join(output_folder, f"replaced_{fname}")
            final_pdfa = os.path.join(output_folder, f"pdfa_{fname}")

            replacements = {
                "WMY FOOD MARKETING SDN BHD": "VG VERSE TRADING",
                "NO 100-02,":"8 JALAN TERATAI 74",
                "JALAN ECO CASCADIA 6/2,":"TAMAN JOHOR JAYA" 
            }

            boxes = extract_text_boxes(src_pdf, replacements)
            draw_overlay(src_pdf, boxes, overlay_pdf)
            merge_pdf_with_overlay(src_pdf, overlay_pdf, merged_pdf)
            convert_to_pdfa(merged_pdf, final_pdfa)

if __name__ == "__main__":
    main()
