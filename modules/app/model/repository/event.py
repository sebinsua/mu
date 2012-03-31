from helper.database import db

def add_event(event):
    db.session.add(event)
    db.session.flush()
    return event.event_id
