from flask import Blueprint
bp = Blueprint('product', __name__)

@bp.route("/artist/<artist>/<product_type>/<release>")
def show_product(artist, product_type, release):
    return "Product / Event"

@bp.route("/all/<product_type>")
def show_products(product_type):
    pass

@bp.route("/add/<product_type>/to/<artist>")
def add_product_to_artist(artist, product_type):
    return "Add product/event to artist"
