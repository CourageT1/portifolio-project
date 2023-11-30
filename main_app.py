#!/usr/bin/python3
""" Kivy provides a set of UI components that i
can use to create my app's interface"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from api import initialize_database, get_product_info
import json
from file_storage import save_product_data


class BarcodeScannerApp(App):
    def build(self):
        return Label(text='Hello, Kivy!')
        # Create the main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create widgets
        self.label = Label(text="Scan a barcode:")
        self.barcode_input = TextInput(multiline=False)
        self.result_label = Label(text="")
        self.get_info_button = Button(text="Get Product Info")
        self.get_info_button.bind(on_press=self.get_product_info)

        # Add widgets to the layout
        main_layout.add_widget(self.label)
        main_layout.add_widget(self.barcode_input)
        main_layout.add_widget(self.result_label)
        main_layout.add_widget(self.get_info_button)

        return main_layout

    def get_product_info(self, instance):
        barcode = self.barcode_input.text
        product_info = get_product_info(barcode)

        if product_info:
            # Extract product details
            price = product_info.get("price", "N/A")
            expiry_date = product_info.get("expiry_date", "N/A")
            promotion = product_info.get("promotion", "No promotion available")

            # Format and display product information
            result_text = f"Price: {price}\nExpiry Date: {expiry_date}\nPromotion: {promotion}"
        else:
            result_text = "Product not found."

        # Display the result in a popup
        popup = Popup(title='Product Information', content=Label(text=result_text), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    BarcodeScannerApp().run()
