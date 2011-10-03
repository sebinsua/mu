from helper.database import db
from sqlalchemy.ext.associationproxy import association_proxy

from datetime import datetime

class Agent(db.Model):
    __tablename__ = 'Agents'
    agent_id = db.Column(db.Integer, primary_key=True)
    agent_type_id = db.Column(db.Integer)
    musicbrainz_mbid = db.Column(db.String(36))
    name = db.Column(db.Text, nullable=False)
    sort_name = db.Column(db.String(50))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    events = association_proxy('AgentEvents', 'Events')

    def __init__(self, name, agent_typei_id=None, musicbrainz_mbid=None):
        self.musicbrainz_mbid = musicbrainz_mbid
        self.name = name
        self.sort_name = name[:50]

class AgentEvent(db.Model):
    agent_event_id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.Integer, \
            db.ForeignKey('Agents.agent_id'), nullable=False)
    event_id = db.Column(db.Integer, \
            db.ForeignKey('Events.event_id'), nullable=False)
    agent_type_id = db.Column(db.Integer, \
            db.ForeignKey('AgentTypes.agent_type_id'))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    agent = db.relationship('Agent', uselist=False, \
            backref=db.backref('AgentEvents', lazy='dynamic'))
    event = db.relationship('Event', uselist=False, \
            backref=db.backref('AgentEvents', lazy='dynamic'))
    agent_type = db.relationship('AgentType', \
            uselist=False, backref=db.backref('AgentEvents', lazy='dynamic'))

    def __init__(self, agent_id, event_id, agent_type_id=None):
        self.agent_id = agent_id
        self.event_id = event_id
        self.agent_type_id = agent_type_id

class AgentType(db.Model):
    __tablename__ = 'AgentTypes'
    agent_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<AgentType %r>' % self.name
