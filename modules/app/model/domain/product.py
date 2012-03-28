from flask import session

from mu.model.repository.event import *
from mu.model.repository.product import *
from mu.model.repository.agent import *
from mu.model.repository.content_owner import *

class ProductDomain:
    def add_product(self, agent_name, event_release_date, \
            product_title, product_type_id=None, product_status_id=None, \
            product_medium_id=None, content_owner_name=None):
        # event_type_id needs to be set depending on the product_type_id
        event_type = get_event_type_from_product_type_id(product_type_id)
        event_type_id = event_type.event_type_id

        # Add an Event
        from mu.model.entity.event import Event
        # TODO: Pick the correct release date field depending on the data.
        event = Event(event_type_id, predicted_textual_release_date=event_release_date)
        event_id = add_event(event)

        # Add a Product
        from mu.model.entity.product import Product
        product = Product(product_title, event_id, product_type_id, product_status_id, product_medium_id)
        product_id = add_product(product)

        # Add a ContentAuthor
        from mu.model.entity.agent import Agent, AgentType
        agent_type_id = AgentType.query.filter_by(name = 'Artist').one().agent_type_id
        agent = Agent(agent_name, agent_type_id)
        # TODO: musicbrainz_mbid, start_date and end_date can be None or fetched from musicbrainz.
        agent_id = add_agent(agent)
        # TODO: For sure the database can be improved again... This is weird.
        link_event_to_agent(agent_id, event_id, agent_type_id)

        # Optionally add a ContentOwner
        if content_owner_name:
            from mu.model.entity.content_owner import ContentOwner
            content_owner = ContentOwner(content_owner_name)
            # TODO: start_date, end_date can be none or fetched from musicbrainz.
            content_owner_id = add_content_owner(content_owner)
            link_product_to_content_owner(content_owner_id, product_id)

        # TODO; We need to create first, and then push objects into repository
        # which should use transactions to make sure that everything gets done
        # at once.

        return product_id

    def get_products(self, product_type=None):
        products = fetch_products(product_type)
        return products
