from sqlalchemy.orm.exc import NoResultFound

from helper.database import db
from mu.model.entity.user import User

def add_user(user):
    db.session.add(user)
    db.session.flush()
    return user.user_id

def fetch_user_with_identity(user_identity):
    query = db.session.query(User).filter(db.or_(User.username == user_identity, \
                                                 User.email == user_identity))
    try:
        user = query.one()
        return user
    except NoResultFound, e:
        return None

def fetch_user_with_user_id(user_id):
    query = db.session.query(User).filter(User.user_id == user_id)

    try:
        user = query.one()
        return user
    except NoResultFound, e:
        return None

def fetch_user_with_uuid(uuid):
    query = db.session.query(User).filter(User.uuid == uuid)

    try:
        user = query.one()
        return user
    except NoResultFound, e:
        return None
