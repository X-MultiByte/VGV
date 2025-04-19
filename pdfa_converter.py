import subprocess

def convert_to_pdfa(input_pdf, output_pdfa):
    subprocess.run([
        "gs", "-dPDFA=2", "-dBATCH", "-dNOPAUSE", "-dNOOUTERSAVE",
        "-sProcessColorModel=DeviceRGB", "-sDEVICE=pdfwrite",
        "-sPDFACompatibilityPolicy=1", f"-sOutputFile={output_pdfa}", input_pdf
    ], check=True)
