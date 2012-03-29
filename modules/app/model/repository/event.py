from helper.database import db

def add_event(event):
    db.session.add(event)
    db.session.commit()
    return event.event_id
