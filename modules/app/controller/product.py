from flask import Blueprint, request, redirect, flash, render_template
from mu.model.domain.product import ProductDomain

bp = Blueprint('product', __name__)
product_domain = ProductDomain()

# NOTE: A product may be an event!

@bp.route("/artist/<content_author>/<product_type>/<product>")
def show_product(content_author, product_type, product):
    return "Product / Event"

@bp.route("/all/<product_type>")
def show_products(product_type):
    # 1. Depending on the product_type we should fetch different products out.
    from mu.model.repository.product import ProductRepository
    product_repository = ProductRepository()
    product_domain.product_repository = product_repository

    products = product_domain.get_products(product_type)

    return render_template('product/show_products.html', products=products)

@bp.route("/add/<product_type>/to/<content_author>")
def add_product_to_artist(content_author, product_type):
    return "Add product/event to artist"
