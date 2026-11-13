
"""Inventory manages Product objects. It calls their methods; it never does their work."""
import json
from product import Product
from ProductFactory import create_product_from_dict


class Inventory:
    def __init__(self):
        self._products: list[Product] = []

    def add_product(self, product):
        for existing_product in self._products:
            if existing_product.product_id == product.product_id:
                raise ValueError(f"Product ID {product.product_id} already exists.")

        self._products.append(product)

    def get_product(self, product_id):
        for product in self._products:
            if product.product_id == product_id:
                return product
        return None

    def update_stock(self, product_id, new_quantity):
        product = self.get_product(product_id)
        if product is None:
            raise KeyError(product_id)
        product.update_stock(new_quantity)

    def display_all(self):
        for product in self._products:
            product.display_information()

    def load(self, filename):
        with open(filename, "r") as file:
            records = json.load(file)

        products = [create_product_from_dict(r) for r in records]
        self._products = products

    def save(self, filename):
        with open(filename, "w") as file:
            json.dump([p.to_dict() for p in self._products], file, indent=4)
