from helper.database import db

def add_agent(agent):
    db.session.add(agent)
    db.session.commit()
    return agent.agent_id

def link_product_to_agent(agent_id, product_id):
    from mu.model.entity.agent import AgentProduct
    agent_product = AgentProduct(agent_id, product_id)
    # TODO: What about the content author product type!
    return agent_product.agent_product_id
