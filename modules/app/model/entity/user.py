from helper.database import db
from sqlalchemy.ext.associationproxy import association_proxy

# Required by the User model.
from datetime import datetime
import uuid
from flaskext.bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'Users'
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

    events = association_proxy('UserEvents', 'Events')
    agents = association_proxy('UserAgents', 'Agents')

    def __init__(self, username, email, password, first_name=None, \
            last_name=None, gender=None, date_of_birth=None, summary=None):
        self.uuid = str(uuid.uuid1())
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.summary = summary

    def __repr__(self):
        print '<User %r>' % self.username

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class UserAgent(db.Model):
    __tablename__ = 'UserAgents'
    user_agent_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False,
            db.ForeignKey('Users.user_id'))
    agent_id = db.Column(db.Integer, nullable=False, \
            db.ForeignKey('Agents.agent_id'))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    user = db.relationship('User', uselist=False, \
            backref=db.backref('UserAgents', lazy='dynamic'))
    content_author = db.relationship('Agent', uselist=False, \
            backref=db.backref('UserAgents', lazy='dynamic'))

    def __init__(self, user_id, agent_id):
        self.user_id = user_id
        self.agent_id = agent_id

class UserEvent(db.Model):
    __tablename__ = 'UserEvents'
    user_event_id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, \
            db.ForeignKey('Users.user_id'), nullable=False)
    event_id= db.Column(db.Integer, \
            db.ForeignKey('Events.event_id'), nullable=False)
    certainty = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    user = db.relationship('User', uselist=False, \
            backref=db.backref('UserEvents', lazy='dynamic'))
    event = db.relationship('Event', uselist=False, \
            backref=db.backref('UserEvents', lazy='dynamic'))

    def __init__(self, user_id, event_id, user_event_status_id=None):
        self.user_id = user_id
        self.event_id = event_id
        self.user_event_status_id = user_event_status_id
