from helper.database import db
from mu.model.entity.product import Product, ProductMedium, ProductType, ProductStatus

def add_product(product):
    db.session.add(product)
    db.session.commit()
    return product.product_id

def fetch_products(product_type=None):
    query = db.session.query(Product)
    products = query.all()
    return products
