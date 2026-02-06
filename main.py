def main():
    print("Hello from extract-pdf!")

    file_path = "pdf/Foto.pdf"

    from pdf_helper import is_pdf, is_pure_pdf, extract_images_from_pdf
    print(f'{file_path} is a pdf: ', is_pdf(file_path))
    print(f'{file_path} is a pure pdf: ', is_pure_pdf(file_path))

    extract_images_from_pdf(file_path)


if __name__ == "__main__":
    main()
