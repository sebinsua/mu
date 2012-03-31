from flask import session

from mu.model.repository.user import *

class UserDomain:
    @staticmethod
    def register(email, username, password, force_login=False):
        from mu.model.entity.user import User
        user = User(username, email, password)

        user_id = add_user(user)

        from helper.database import db
        db.session.commit()

        if force_login:
            UserDomain.force_login(user_id)
        return user_id

    @staticmethod
    def login(user_identity, password):
        user = fetch_user_with_identity(user_identity)

        if user is not None and user.check_password(password):
            session['uuid'] = user.uuid
            return True
        return False

    @staticmethod
    def force_login(user_id):
        from mu.model.entity.user import User

        user = fetch_user_with_user_id(user_id)
        session['uuid'] = user.uuid

    @staticmethod
    def logout():
        return session.pop('uuid', None)

    @staticmethod
    def username_of_session():
        username = None
        if session.has_key('uuid'):
            uuid = session['uuid']
            from mu.model.repository.user import fetch_user_with_uuid
            user = fetch_user_with_uuid(uuid)
            username = user.username if user else None
        return username
