from helper.database import db
from sqlalchemy.ext.associationproxy import association_proxy

from mu.model.entity.product import Product
from mu.model.entity.service import Service
from mu.model.entity.agent import Agent
from mu.model.entity.event import Event

# Required by the User model.
from datetime import datetime
import uuid
from flaskext.bcrypt import generate_password_hash, check_password_hash
from modules.helper.database import ConstraintsMixin

class User(db.Model, ConstraintsMixin):
    __tablename__ = 'User'
    user_id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.Text, unique=True)
    username = db.Column(db.Text, unique=True)
    password_hash = db.Column(db.String(60))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    gender = db.Column(db.String(1))
    date_of_birth = db.Column(db.Time)
    summary = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    __table_args__ = (db.UniqueConstraint('uuid'), db.UniqueConstraint('email'), db.UniqueConstraint('username'))

    events = association_proxy('UserEvent', 'event')
    products = association_proxy('UserProduct', 'product')
    services = association_proxy('UserService', 'service')
    agents = association_proxy('UserAgent', 'agent')

    def __init__(self, username, email, password, first_name=None,\
                 last_name=None, gender=None, date_of_birth=None, summary=None):
        self.uuid = str(uuid.uuid1())
        self.username = username
        self.email = email.lower()
        self.password_hash = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.summary = summary

    def __repr__(self):
        print '<User %r>' % self.username

    def to_dict(self):
        from sqlalchemy.orm import class_mapper

        return dict((col.name, getattr(self, col.name))
        for col in class_mapper(self.__class__).mapped_table.c)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class UserAgent(db.Model):
    __tablename__ = 'UserAgent'
    user_agent_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('Agent.agent_id'), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    user = db.relationship('User', uselist=False,\
        backref=db.backref('UserAgent', lazy='dynamic'))
    agent = db.relationship('Agent', uselist=False,\
        backref=db.backref('UserAgent', lazy='dynamic'))

    def __init__(self, user_id, agent_id):
        self.user_id = user_id
        self.agent_id = agent_id


class UserEvent(db.Model):
    __tablename__ = 'UserEvent'
    user_event_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('Event.event_id'), nullable=False)
    start_release_date = db.Column(db.DateTime)
    end_release_date = db.Column(db.DateTime)
    textual_release_date = db.Column(db.PickleType)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    user = db.relationship('User', uselist=False,\
        backref=db.backref('UserEvent', lazy='dynamic'))
    event = db.relationship('Event', uselist=False,\
        backref=db.backref('UserEvent', lazy='dynamic'))

    def __init__(self, user_id, event_id, start_release_date, end_release_date,
                 textual_release_date):
        self.user_id = user_id
        self.event_id = event_id
        self.start_release_date = start_release_date
        self.end_release_date = end_release_date
        self.textual_release_date = textual_release_date


class UserProduct(db.Model):
    __tablename__ = 'UserProduct'
    user_product_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.product_id'), nullable=False)
    weight = db.Column(db.Integer, nullable=False, default=50)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    user = db.relationship('User', uselist=False,\
        backref=db.backref('UserProduct', lazy='dynamic'))
    product = db.relationship('Product', uselist=False,\
        backref=db.backref('UserProduct', lazy='dynamic'))

    def __init__(self, user_id, product_id, weight=None):
        self.user_id = user_id
        self.product_id = product_id
        self.weight = weight


class UserService(db.Model):
    __tablename__ = 'UserService'
    user_service_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('Service.service_id'), nullable=False)
    weight = db.Column(db.Integer, nullable=False, default=50)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    user = db.relationship('User', uselist=False,\
        backref=db.backref('UserService', lazy='dynamic'))
    service = db.relationship('Service', uselist=False,\
        backref=db.backref('UserService', lazy='dynamic'))

    def __init__(self, user_id, service_id, weight=None):
        self.user_id = user_id
        self.service_id = service_id
        self.weight = weight
