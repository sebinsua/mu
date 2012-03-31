from helper.database import db

from datetime import datetime

class Event(db.Model):
    __tablename__ = 'Event'
    event_id = db.Column(db.Integer, primary_key=True)
    predicted_start_release_date = db.Column(db.DateTime)
    predicted_end_release_date = db.Column(db.DateTime)
    predicted_textual_release_date = db.Column(db.PickleType)
    certainty = db.Column(db.Integer)

    def __init__(self, certainty=100, predicted_textual_release_date=None, \
            predicted_start_release_date=None, predicted_end_release_date=None):
        self.certainty = certainty
        self.predicted_start_release_date = predicted_start_release_date
        self.predicted_end_release_date = predicted_end_release_date
        self.predicted_textual_release_date = predicted_textual_release_date
