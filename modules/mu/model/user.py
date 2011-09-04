from helper.database import db

# Required by the User model.
import uuid
from flaskext.bcrypt import generate_password_hash

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.Text, unique=True)
    username = db.Column(db.Text, unique=True)
    password_hash = db.Column(db.String(60))
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    gender = db.Column(db.String(1))
    date_of_birth = db.Column(db.Time)
    summary = db.Column(db.Text)
    created = db.Column(db.Time, nullable=False, default='now')

    def __init__(self, email, username, password):
        self.uuid = str(uuid.uuid1())
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
