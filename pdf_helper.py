from pydoc import doc
import pymupdf
import os

def is_pdf(file_path):
    """
    Check if the given file is a valid PDF by attempting to open it with PyMuPDF.
    
    Args:
        file_path (str): The path to the file to be checked.
        
    Returns:
        bool: True if the file is a valid PDF, False otherwise.
    """
    try:
        with pymupdf.open(file_path) as doc:
            return doc.is_pdf
    except Exception:
        return False

def is_pure_pdf(file_path):
    """
    Check if the given PDF file is a pure PDF.
    
    Args:
        file_path (str): The path to the PDF file to be checked.
        
    Returns:
        bool: True if the PDF is pure, False otherwise.
    """
    try:
        doc = pymupdf.open(file_path)
        for page in doc:
            if page.get_text().strip():
                return True # If any page contains text, we consider it a pure PDF
        return False # If no pages contain text, it's not a pure PDF
    except Exception:
        return False

def has_images(file_path):
    """
    Check if the given PDF file contains images.
    
    Args:
        file_path (str): The path to the PDF file to be checked.
        
    Returns:
        bool: True if the PDF contains images, False otherwise.
    """
    try:
        doc = pymupdf.open(file_path)
        for page in doc:
            if page.get_images():
                return True # If any page contains images
        return False # If no pages contain images
    except Exception:
        return False
    


def extract_images_from_pdf(pdf_path):
    """
    Extract images from a PDF file using PyMuPDF.
    
    Args:
        pdf_path (str): The path to the PDF file.
    """
    doc = pymupdf.open(pdf_path) # open a document

    os.makedirs(doc.name + "_images", exist_ok=True) # create a directory to save images

    for page_index in range(len(doc)): # iterate over pdf pages
        page = doc[page_index] # get the page
        image_list = page.get_images()

        # print the number of images found on the page
        if image_list:
            print(f"Found {len(image_list)} images on page {page_index}")
        else:
            print("No images found on page", page_index)

        for image_index, img in enumerate(image_list, start=1): # enumerate the image list
            xref = img[0] # get the XREF of the image
            pix = pymupdf.Pixmap(doc, xref) # create a Pixmap

            if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

            pix.save(os.path.join(doc.name + "_images", "page_%s-image_%s.png" % (page_index, image_index))) # save the image as png
            print(f"Saved image {image_index} from page {page_index}")
            pix = None