import os

from PIL import Image
import pytesseract
import re
from mrz.checker.td1 import TD1CodeChecker, get_country


def extract_mrz_text(image_path):
    """
    Extracts MRZ text directly from an image using Tesseract.
    Filters for lines with MRZ characteristics and formats them as required.
    """
    # Load the image
    image = Image.open(image_path)

    # Perform OCR to extract text
    text = pytesseract.image_to_string(image, lang='eng')
    mrz_lines = re.findall(r'[A-Z0-9<]{30,44}', text.upper())  # Find potential MRZ lines

    # Ensure we have at least two lines that match MRZ formatting
    if len(mrz_lines) >= 2:
        mrz_text = ''.join(mrz_lines)  # Combine the first two MRZ lines
        mrz_text = mrz_text.ljust(90, '<')  # Pad to 90 characters if needed
        formatted_mrz_text = '\n'.join([mrz_text[i:i + 30] for i in range(0, len(mrz_text), 30)])
        return formatted_mrz_text
    else:
        raise ValueError("Failed to locate two MRZ lines in the image")


def read_mrz(image_path):
    """
    Main function to read MRZ from an image by directly extracting and formatting MRZ text.
    Parses the MRZ and returns it as a dictionary with relevant fields.
    """
    # Check if the file exists
    if not os.path.exists(image_path):
        raise ValueError(f"Image path does not exist: {image_path}")

    # Rest of the function remains the same
    mrz_text = extract_mrz_text(image_path)   # Directly extract MRZ text from the image

    # Parse MRZ text using TD1CodeChecker
    try:
        td1_check = TD1CodeChecker(mrz_text)
        fields = td1_check.fields()

        # Build the dictionary with only available fields
        result = {
            "country": get_country(fields.country),
            "name": fields.name,
            "surname": fields.surname,
            "document_type": fields.document_type,
            "document_number": fields.document_number,
            "nationality": fields.nationality,
            "birth_date": fields.birth_date,
            "sex": fields.sex,
            "expiry_date": fields.expiry_date,
            "optional_data": fields.optional_data,
            "optional_data_2": fields.optional_data_2
        }

        # Conditionally add check digit fields if they are present
        if hasattr(fields, 'check_digit_document_number'):
            result["check_digit_document_number"] = fields.check_digit_document_number
        if hasattr(fields, 'check_digit_birth_date'):
            result["check_digit_birth_date"] = fields.check_digit_birth_date
        if hasattr(fields, 'check_digit_expiry_date'):
            result["check_digit_expiry_date"] = fields.check_digit_expiry_date
        if hasattr(fields, 'check_digit_composite'):
            result["check_digit_composite"] = fields.check_digit_composite
        if hasattr(fields, 'valid_check_digits'):
            result["valid_check_digits"] = fields.valid_check_digits

        return result

    except Exception as e:
        raise ValueError(f"MRZ validation failed: {e}")
