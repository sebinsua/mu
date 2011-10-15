from flask import session

class ProductDomain:
    product_repository = None
    event_repository = None
    agent_repository = None
    content_owner_repository = None

    def __init__(self, product_repository=None, event_repository=None, \
            agent_repository=None, content_owner_repository=None):
        self.product_repository = product_repository
        self.event_repository = event_repository
        self.agent_repository = agent_repository
        self.content_owner_repository = content_owner_repository

    def add_product(self, agent_name, event_release_date, \
            product_title, product_type_id=None, product_status_id=None, \
            product_medium_id=None, content_owner_name=None):
        # event_type_id needs to be set depending on the product_type_id
        event_type = self.event_repository.get_event_type_from_product_type_id(product_type_id)
        event_type_id = event_type.event_type_id

        # Add an Event
        from mu.model.entity.event import Event
        # TODO: Pick the correct release date field depending on the data.
        event = Event(event_type_id, predicted_release_date=event_release_date)
        event_id = self.event_repository.add_event(event)

        # Add a Product
        from mu.model.entity.product import Product
        product = Product(title, event_id, product_type_id, product_status_id, product_medium_id)
        product_id = self.product_repository.add_product(product)

        # Add a ContentAuthor
        from mu.model.entity.agent import Agent
        agent = Agent(agent_name)
        # TODO: musicbrainz_mbid, start_date and end_date can be None or fetched from musicbrainz.
        agent_id = self.agent_repository.add_agent(agent)
        self.agent_repository.link_product_to_agent(agent_id, product_id)

        # Optionally add a ContentOwner
        if content_owner_name:
            from mu.model.entity.content_owner import ContentOwner
            content_owner = ContentOwner(content_owner_name)
            # TODO: start_date, end_date can be none or fetched from musicbrainz.
            content_owner_id = self.content_owner_repository.add_content_owner(content_owner)
            self.content_owner_repository.link_product_to_content_owner(content_owner_id, product_id)

        return product_id

    def get_products(self, product_type=None):
        products = self.product_repository.fetch_products(product_type)
        return products
