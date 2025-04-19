FROM python:3.10-slim

RUN apt-get update &&     apt-get install -y ghostscript python3-dev build-essential &&     pip install pymupdf PyPDF2 reportlab

WORKDIR /app
COPY . /app

ENTRYPOINT ["python", "runner.py"]
