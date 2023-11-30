#!/usr/bin/python3
"""flask for my application"""
import os
from flask import Flask, request
from flask_restful import Resource, Api
from flask import Flask, jsonify, request
from api import initialize_database, get_product_info
import json
from file_storage import save_product_data
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.network.urlrequest import UrlRequest

app = Flask(__name__)
api = Api(app)


class BarcodeScannerApp(App):
    def build(self):
        self.barcode_input = TextInput(hint_text='Enter barcode')
        self.get_info_button = Button(text='Get Product Info')
        self.get_info_button.bind(on_press=self.get_product_info)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.barcode_input)
        layout.add_widget(self.get_info_button)

        return layout

    def get_product_info(self, instance):
        barcode = self.barcode_input.text
        url = 'http://127.0.0.1:5000/product/' + barcode


        def on_success(request, result):
            # Handle the result and display information
            # This is a placeholder; replace it with your logic
            product_info = json.loads(result)
            price = product_info.get('price', 'N/A')
            expiry_date = product_info.get('expiry_date', 'N/A')
            promotion = product_info.get('promotion', 'No promotion available')

            result_text = f"Price: {price}\nExpiry Date: {expiry_date}\nPromotion: {promotion}"
            self.show_result_popup(result_text)

        def on_error(request, error):
            print('Error:', error)

        UrlRequest(url, on_success=on_success, on_error=on_error)

    def show_result_popup(self, result_text):
        popup = Popup(title='Product Information', content=Label(text=result_text), size_hint=(None, None), size=(400, 200))
        popup.open()

    with open('products.json', 'r') as file:
        product_data = json.load(file)

@app.route('/product/<barcode>', methods=['GET'])
def get_product_info(barcode):
    # Check if the barcode exists in the product data
    if barcode in product_data:
        return jsonify(product_data[barcode])
    else:
        return jsonify({'error': 'Product not found'})


if __name__ == '__main__':
    app.run(debug=True)
