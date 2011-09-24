from flask import session

class ProductDomain:
    product_repository = None

    def __init__(self, product_repository=None):
        self.product_repository = product_repository

    def get_products(self, product_type=None):
        products = self.product_repository.fetch_products(product_type)
        return products
