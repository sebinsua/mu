from helper.database import db

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

class UserContentAuthor(db.Model):
    __tablename__ = 'UserContentAuthors'
    user_content_author_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False,
            db.ForeignKey('Users.user_id'))
    content_author_id = db.Column(db.Integer, nullable=False, \
            db.ForeignKey('ContentAuthors.content_author_id'))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    user = db.relationship('User', \
            backref=db.backref('UserContentAuthors', lazy='dynamic'))
    content_author = db.relationship('ContentAuthor', \
            backref=db.backref('UserContentAuthors', lazy='dynamic'))

    def __init__(self, user_id, content_author_id):
        self.user_id = user_id
        self.content_author_id = content_author_id

class UserEventStatus(db.Model):
    __tablename__ = 'UserEventStatuses'
    user_event_status_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, user_event_status_id, name):
        self.user_event_status_id = user_event_status_id
        self.name = name

class UserEvent(db.Model):
    __tablename__ = 'UserEvents'
    user_event_id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, \
            db.ForeignKey('Users.user_id'), nullable=False)
    event_id= db.Column(db.Integer, \
            db.ForeignKey('Events.event_id'), nullable=False)
    user_event_status_id = db.Column(db.Integer, \
            db.ForeignKey('UserEventStatuses.user_event_status_id'))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    user = db.relationship('User', \
            backref=db.backref('UserEvents', lazy='dynamic'))
    event = db.relationship('Event', \
            backref=db.backref('UserEvents', lazy='dynamic'))
    user_event_status = db.relationship('UserEventStatus', \
            backref=db.backref('UserEvents', lazy='dynamic'))

    def __init__(self, user_id, event_id, user_event_status_id=None):
        self.user_id = user_id
        self.event_id = event_id
        self.user_event_status_id = user_event_status_id
