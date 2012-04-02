from helper.database import db, ConstraintsMixin

from datetime import datetime

class Agent(db.Model, ConstraintsMixin):
    __tablename__ = 'Agent'
    agent_id = db.Column(db.Integer, primary_key=True)
    agent_type_id = db.Column(db.Integer, db.ForeignKey('AgentType.agent_type_id'), nullable=False)
    musicbrainz_mbid = db.Column(db.String(36))
    name = db.Column(db.Text, nullable=False)
    sort_name = db.Column(db.String(50))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    __table_args__ = ( db.UniqueConstraint('name'), )

    agent_type = db.relationship('AgentType', uselist=False,
        backref=db.backref('Agent', lazy='dynamic'))

    def __init__(self, name, agent_type_id=None, musicbrainz_mbid=None):
        self.musicbrainz_mbid = musicbrainz_mbid
        self.name = name
        self.sort_name = name[:50]
        self.agent_type_id = agent_type_id

    def __str__(self):
        return self.name


class AgentType(db.Model):
    __tablename__ = 'AgentType'
    agent_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<AgentType %r>' % self.name

    def __str__(self):
        return self.name
