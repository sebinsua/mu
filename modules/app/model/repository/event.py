from helper.database import db

def add_event(event):
    db.session.add(event)
    db.session.commit()
    return event.event_id

def get_event_type_from_product_type_id(product_type_id):
    from mu.model.entity.product import ProductType
    from mu.model.entity.event import EventType

    pt_query = db.session.query(ProductType).filter(ProductType.product_type_id == product_type_id)
    product_type = pt_query.one()

    if product_type.name == 'Event':
        et_query = db.session.query(EventType).filter(EventType.name == 'Performance')
    else:
        et_query = db.session.query(EventType).filter(EventType.name == 'Release')

    event_type = et_query.one()
    return event_type
