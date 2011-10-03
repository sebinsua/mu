from helper.database import db

from mu.model.entity.event import Event

from datetime import datetime

class Action(db.Model):
    __tablename__ = 'Actions'
    action_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, \
            db.ForeignKey('Events.event_id'))
    description = db.Column(db.Text, nullable=False)

    event = db.relationship('Event', uselist=False, \
            backref=db.backref('Actions', lazy='dynamic', uselist=False))

    def __init__(self, event_id, description):
        self.event_id = event_id
        self.description = description
