from helper.database import db
from sqlalchemy.ext.associationproxy import association_proxy

from mu.model.entity.event import Event
from mu.model.entity.work import Work
from mu.model.entity.agent import Agent, AgentType

from datetime import datetime

class Service(db.Model):
    __tablename__ = 'Service'
    service_id = db.Column(db.Integer, primary_key=True)
    work_id = db.Column(db.Integer, db.ForeignKey('Work.work_id'))
    service_type_id = db.Column(db.Integer, db.ForeignKey('ServiceType.service_type_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('Event.event_id'), nullable=False)
    title = db.Column(db.Text, nullable=False)
    sort_title = db.Column(db.String(50))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    work = db.relationship('Work', uselist=False,\
        backref=db.backref('Service', lazy='dynamic'))
    service_type = db.relationship('ServiceType', uselist=False,\
        backref=db.backref('Service', lazy='dynamic'))
    event = db.relationship('Event', uselist=False,\
        backref=db.backref('Service', lazy='dynamic', uselist=False))

    agents = association_proxy('ServiceAgent', 'agent')

    def __init__(self, title, event_id, service_type_id=None, work_id=None):
        self.work_id = work_id
        self.service_type_id = service_type_id
        self.event_id = event_id
        self.title = title
        self.sort_title = title[:50]


class ServiceAgent(db.Model):
    __tablename__ = 'ServiceAgent'
    service_agent_id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('Service.service_id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('Agent.agent_id'), nullable=False)
    agent_order = db.Column(db.Integer)
    agent_type_id = db.Column(db.Integer, db.ForeignKey('AgentType.agent_type_id'))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    service = db.relationship('Service', uselist=False,\
        backref=db.backref('ServiceAgent', lazy='dynamic'))
    agent = db.relationship('Agent', uselist=False,\
        backref=db.backref('ServiceAgent', lazy='dynamic'))
    agent_type = db.relationship('AgentType', uselist=False,\
        backref=db.backref('ServiceAgent', lazy='dynamic'))

    def __init__(self, service_id, agent_id, agent_type_id, agent_order=None):
        self.service_id = service_id
        self.agent_id = agent_id
        self.agent_type_id = agent_type_id
        self.agent_order = agent_order


class ServiceType(db.Model):
    __tablename__ = 'ServiceType'
    service_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<ServiceType %r>' % self.name

    def __str__(self):
        return self.name
