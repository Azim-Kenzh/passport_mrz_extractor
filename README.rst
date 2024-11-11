passport_mrz_extractor
======================

`passport_mrz_extractor` is a Python library for extracting and validating Machine Readable Zone (MRZ) data from passport images.
It uses Tesseract OCR to read MRZ text and validates it using the `mrz` library.

Features
--------

- Extract MRZ data from passport images.
- Validate MRZ data fields, including document type, name, nationality, date of birth, and expiry date.
- Automatic image processing for better OCR accuracy.

Installation
------------

You can install `passport_mrz_extractor` using `pip`:

.. code-block:: bash

    pip install passport_mrz_extractor

Requirements
------------

- **Python** >= 3.10
- **Tesseract OCR** installed on your system

To install Tesseract:

- **Ubuntu**: `sudo apt install tesseract-ocr`
- **MacOS (using Homebrew)**: `brew install tesseract`
- **Windows**: Download the installer from https://github.com/UB-Mannheim/tesseract/wiki

Dependencies
------------

This library requires the following Python packages:

- `pytesseract` - For performing OCR on images.
- `opencv-python` - For image processing.
- `mrz` - For MRZ data validation.
- `Pillow` - For handling image files in Python.

Usage
-----

Here’s how to use `passport_mrz_extractor` to extract MRZ data from a passport image.

### Basic Example

This example demonstrates extracting all available MRZ fields from an image and handling potential errors.

.. code-block:: python

    import mrz_reader

    # Path to the passport image
    image_path = 'path/to/passport_image.jpg'

    try:
        mrz_data = mrz_reader.read_mrz(image_path)
        print("Extracted MRZ Data:")
        for key, value in mrz_data.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(f"Error reading MRZ: {e}")

### Example of Using Specific MRZ Fields

In this example, we extract specific fields such as the country, document number, and birth date, and print them in a formatted output.

.. code-block:: python

    import mrz_reader

    # Path to the passport image
    image_path = 'path/to/passport_image.jpg'

    try:
        # Extract MRZ data
        mrz_data = mrz_reader.read_mrz(image_path)

        # Display specific fields
        print("Country of Issue:", mrz_data.get("country"))
        print("Document Number:", mrz_data.get("document_number"))
        print("Name:", mrz_data.get("name"))
        print("Surname:", mrz_data.get("surname"))
        print("Date of Birth:", mrz_data.get("birth_date"))
        print("Expiry Date:", mrz_data.get("expiry_date"))
        print("Nationality:", mrz_data.get("nationality"))
        print("Sex:", mrz_data.get("sex"))

    except ValueError as e:
        print(f"Error reading MRZ: {e}")

Contributing
------------

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

Issues
------

If you encounter any issues, please report them on the GitHub repository:

https://github.com/Azim-Kenzh/passport_mrz_extractor/issues

License
-------

`passport_mrz_extractor` is licensed under the MIT License.
