from mu.model.repository.event import *
from mu.model.repository.product import *
from mu.model.repository.agent import *
from mu.model.repository.content_owner import *

class ProductDomain:
    @staticmethod
    def add_product(agent_name, agent_type_id, event_release_date,
                    product_title, product_type_id=None, product_status_id=None,
                    product_medium_id=None, content_owner_name=None):
        # Add an Event
        from mu.model.entity.event import Event
        # @todo: Pick the correct release date field depending on the data.
        event = Event(predicted_textual_release_date=event_release_date)
        event_id = add_event(event)

        # Add a Product
        from mu.model.entity.product import Product

        product = Product(product_title, event_id, product_type_id, product_status_id, product_medium_id)
        product_id = add_product(product)

        # Add an Agent
        from mu.model.entity.agent import Agent, AgentType
        # @todo: musicbrainz_mbid, start_date and end_date can be None or fetched from musicbrainz.
        agent = Agent(agent_name, agent_type_id)
        agent_id = add_agent(agent)
        link_product_to_agent(agent_id, product_id, agent_type_id)

        # Optionally add a ContentOwner
        if content_owner_name:
            from mu.model.entity.content_owner import ContentOwner

            content_owner = ContentOwner(content_owner_name)
            # @todo: start_date, end_date can be none or fetched from musicbrainz.
            content_owner_id = add_content_owner(content_owner)
            link_product_to_content_owner(content_owner_id, product_id)

        from helper.database import db

        db.session.commit()

        return product_id

    @staticmethod
    def get_products(product_type=None):
        # Accept plural but convert to singular...
        if product_type and product_type.endswith('s'): # urls are pluralised but data is singular!
            product_type = product_type[:-1]
        if product_type in ['release', 'product']:
            product_type = None # We want to get everything out in this case.

        products = fetch_products(product_type)
        return products
