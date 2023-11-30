#!/usr/bin/python3
""" route definitions and view functions for Flask application."""
from flask import jsonify
from app import app

@app.route('/')
def index():
    return 'Hello, Barcode Scanner!'

@app.route('/product/<barcode>', methods=['GET'])
def get_product_info(barcode):
    # Replace this with your logic to fetch product information based on the barcode
    return jsonify(product.json)
