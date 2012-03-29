from helper.database import db

def add_agent(agent):
    db.session.add(agent)
    db.session.commit()
    return agent.agent_id

def link_product_to_agent(agent_id, product_id, agent_type_id):
    from mu.model.entity.product import ProductAgent
    product_agent = ProductAgent(product_id, agent_id, agent_type_id)
    return product_agent.product_agent_id
