from helper.database import db, check_if_entity_exists

def add_agent(agent):
    # Test if the agent already exists in the database.
    unique_agent = check_if_entity_exists(agent)
    if unique_agent:
        return unique_agent.agent_id

    db.session.add(agent)
    db.session.flush()
    return agent.agent_id

def link_product_to_agent(agent_id, product_id, agent_type_id):
    from mu.model.entity.product import ProductAgent
    product_agent = ProductAgent(product_id, agent_id, agent_type_id)
    db.session.add(product_agent)
    db.session.flush()
    return product_agent.product_agent_id
