from flask import Blueprint, request, redirect, flash, render_template
from mu.model.domain.product import ProductDomain

from mu.model.repository.product import ProductRepository
from mu.model.repository.event import EventRepository
from mu.model.repository.agent import AgentRepository
from mu.model.repository.content_owner import ContentOwnerRepository

bp = Blueprint('product', __name__)
product_domain = ProductDomain(ProductRepository(), EventRepository(), \
        ContentAuthorRepository(), ContentOwnerRepository())

# NOTE: A product may be an event!

@bp.route("/artist/<agent>/<product_type>/<product>")
def show_product(agent, product_type, product):
    return "Product / Event"

@bp.route("/all/<product_type>")
def show_products(product_type):
    # 1. Reject if not in certain product_types... Mabes.
    # 2. Depending on the product_type we should fetch different products out.
    products = product_domain.get_products(product_type)

    return render_template('product/show_products.html', products=products)

@bp.route("/add/<product_type>", methods=['GET', 'POST'])
@bp.route("/add/<product_type>/to/<agent>", methods=['GET', 'POST'])
def add_product_to_content_author(product_type, agent=None):
    product_types = product_domain.product_repository.fetch_product_types()
    product_statuses = product_domain.product_repository.fetch_product_statuses()
    product_mediums = product_domain.product_repository.fetch_product_mediums()

    from mu.form.add_product import AddProductForm
    add_product_form = AddProductForm(request.form)
    add_product_form.product_type.choices = product_types
    add_product_form.product_status.choices = product_statuses
    add_product_form.product_medium.choices = product_mediums

    if request.method == "POST" and add_product_form.validate():
        agent_name = request.form.get('artist')
        content_owner_name = request.form.get('label')
        event_release_date = request.form.get('date')
        product_title = request.form.get('title')
        product_type_id = request.form.get('type')
        product_status_id = request.form.get('status')
        product_medium_id = request.form.get('medium')

        product_domain.add_product(agent_name, event_release_date, \
            product_title, product_type_id, product_status_id, \
            product_medium_id, content_owner_name)

    return render_template('product/add_product.html',
            product_type=product_type, agent=agent, form=add_product_form)
