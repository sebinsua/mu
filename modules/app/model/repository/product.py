from helper.database import db
from mu.model.entity.product import Product, ProductMedium, ProductType, ProductStatus

def add_product(product):
    db.session.add(product)
    db.session.flush()
    return product.product_id

def fetch_products(product_type=None):
    if product_type:
        query = db.session.query(Product) \
                          .join(ProductType, Product.product_type_id == ProductType.product_type_id) \
                          .filter(ProductType.name==product_type) \
                          .order_by(Product.created.desc())
    else:
        query = db.session.query(Product) \
                          .order_by(Product.created.desc())

    products = query.all()
    return products
