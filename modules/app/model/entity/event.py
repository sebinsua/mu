from helper.database import db

from datetime import datetime

class Event(db.Model):
    __tablename__ = 'Event'
    event_id = db.Column(db.Integer, primary_key=True)
    event_type_id = db.Column(db.Integer, db.ForeignKey('EventType.event_type_id'), nullable=False)
    predicted_start_release_date = db.Column(db.DateTime)
    predicted_end_release_date = db.Column(db.DateTime)
    predicted_textual_release_date = db.Column(db.PickleType)
    certainty = db.Column(db.Integer)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    event_type = db.relationship('EventType', uselist=False, \
            backref=db.backref('Event', lazy='dynamic'))

    def __init__(self, event_type_id, certainty=100, predicted_textual_release_date=None, \
            predicted_start_release_date=None, predicted_end_release_date=None):
        self.event_type_id = event_type_id
        self.certainty = certainty
        self.predicted_start_release_date = predicted_start_release_date
        self.predicted_end_release_date = predicted_end_release_date
        self.predicted_textual_release_date = predicted_textual_release_date

class EventType(db.Model):
    __tablename__ = 'EventType'
    event_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name
