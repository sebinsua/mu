from helper.database import db
from mu.model.entity.user import User

def add_user(self, user):
    db.session.add(user)
    db.session.commit()
    return user.user_id

def fetch_user_with_identity(self, user_identity):
    query = db.session.query(User).filter(db.or_(User.username == user_identity, \
                                                 User.email == user_identity))
    user = query.one()
    return user

def fetch_user_with_user_id(self, user_id):
    query = db.session.query(User).filter(User.user_id == user_id)
    user = query.one()
    return user
