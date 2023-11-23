#!/usr/bin/python3
""" handles the loading and saving of the product database, which is
essentially a simulated persistent storage for the app's product information"""
import json

# Define the path to the JSON file
DATABASE_FILE = "product_database.json"

def load_database():
    try:
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_database(database):
    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file, indent=2)

# Load the initial database
PRODUCT_DATABASE = load_database()
