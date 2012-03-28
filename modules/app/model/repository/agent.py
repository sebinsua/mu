from helper.database import db

def add_agent(agent):
    db.session.add(agent)
    db.session.commit()
    return agent.agent_id

def link_event_to_agent(agent_id, event_id, agent_type_id):
    from mu.model.entity.agent import AgentEvent
    agent_event = AgentEvent(agent_id, event_id, agent_type_id)
    # TODO: What about the content author product type!
    return agent_event.agent_event_id
