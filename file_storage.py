#!/usr/bin/python3
""" provides functions to load and save product data to a file
(product_data.json)"""
import json


# Define the path to the JSON file
PRODUCT_DATA_FILE = "product_data.json"

def load_product_data():
    try:
        with open(PRODUCT_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_product_data(product_data):
    with open(PRODUCT_DATA_FILE, "w") as file:
        json.dump(product_data, file, indent=2)
