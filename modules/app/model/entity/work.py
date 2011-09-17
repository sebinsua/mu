from helper.database import db

from datetime import datetime

class Work(db.Model):
    __tablename__ = 'works'
    work_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    sort_title = db.Column(db.String(50))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, title):
        self.title = title
        self.sort_title = title # TODO: Get a substring of this.
