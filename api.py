#!/usr/bin/python3
""" an interface between the main application and the product database.
It initializes the database when the module is imported and provides a
function to retrieve product information based on barcodes."""
from database import PRODUCT_DATABASE, save_database
from file_storage import load_product_data


def initialize_database():
    # Load product data from the file and update the database
    product_data = load_product_data()
    PRODUCT_DATABASE.update(product_data)
    save_database(PRODUCT_DATABASE)

# Initialize the database when the API module is imported
initialize_database()

def get_product_info(barcode):
    """
    Retrieve product information based on the barcode.

    Args:
        barcode (str): The barcode of the product.

    Returns:
        dict: Product information (price, expiry_date, promotion).
              Returns None if the product is not found.
    """
    return PRODUCT_DATABASE.get(barcode)
