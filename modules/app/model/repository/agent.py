from helper.database import db

def add_agent(agent):
    # todo: Test if content_owner already exists in the database by searching for the same
    #       unique constraints.
    import pprint
    print 'agent: '
    for constraint in agent.__table__.constraints:
        if isinstance(constraint, db.UniqueConstraint):
            for column in constraint.columns:
                pprint.pprint(column.name)
    # @todo: This should be rewritten into an IsUniqueMixin that can get out a list of columns.
    # Then check to see whether the values inside this list of columns already exists in the database
    # using a where key1 = agent.key1 and key2 = agent.key2 and key3 = agent.key3
    # Use getattr() to help build:
    # http://stackoverflow.com/questions/7604967/sqlalchemy-build-query-filter-dynamically-from-dict
    # todo: Next problem is doing the actual insert, which should be done like so:
    # http://stackoverflow.com/questions/7092396/react-on-uniquekeyviolation-in-sqlalchemy

    db.session.add(agent)
    db.session.flush()
    return agent.agent_id

def link_product_to_agent(agent_id, product_id, agent_type_id):
    from mu.model.entity.product import ProductAgent
    product_agent = ProductAgent(product_id, agent_id, agent_type_id)
    db.session.add(product_agent)
    db.session.flush()
    return product_agent.product_agent_id
