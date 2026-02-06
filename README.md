# PDF Image Text Extractor

A Python-based tool designed to extract text content from images embedded within PDF files. This is particularly useful for scanned documents or PDFs where text is not selectable.

## Purpose

The goal of this project is to provide a seamless way to:
1. Identify if a PDF is "pure" (contains selectable text) or image-based.
2. Extract images from PDF pages.
3. Perform OCR (Optical Character Recognition) on extracted images to retrieve text content.

## 🛠 Features (In Progress)

- [x] **PDF Validation**: Check if a file is a valid PDF.
- [x] **PDF Analysis**: Determine if a PDF contains selectable text or only images.
- [x] **Image Extraction**: Efficiently extract images from each page of a PDF using `PyMuPDF`.
- [ ] **OCR Integration**: (Coming soon) Extract text from the saved images.

## Installation

This project uses `uv` for dependency management.

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd extract_pdf
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

Currently, you can run the tool to analyze a PDF and extract its images:

1. Place your PDF file in the `pdf/` directory.
2. Update the `file_path` in `main.py` if necessary.
3. Run the application:
   ```bash
   uv run main.py
   ```

The extracted images will be saved in a directory named `<pdf_filename>_images`.

## Project Structure

- `main.py`: Entry point of the application.
- `pdf_helper.py`: Contains logic for PDF processing and image extraction.
- `pdf/`: Directory for input PDF files.
- `pyproject.toml`: Project configuration and dependencies.

## Dependencies

- [PyMuPDF (fitz)](https://github.com/pymupdf/PyMuPDF): For PDF manipulation and image extraction.
- [Pillow](https://python-pillow.org/): For image processing.
- [pdf2image](https://github.com/Belval/pdf2image): For converting PDF pages to images.

---
*This project is currently under development.*
