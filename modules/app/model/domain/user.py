from flask import session

from mu.model.repository.user import *

class UserDomain:
    def register(self, email, username, password, force_login=False):
        from mu.model.entity.user import User
        user = User(username, email, password)

        user_id = add_user(user)
        if force_login:
            self.force_login(user_id)
        return user_id

    def login(self, user_identity, password):
        user = fetch_user_with_identity(user_identity)

        if check_password(password):
            session['uuid'] = user.uuid
            return True
        return False

    def force_login(self, user_id):
        from mu.model.entity.user import User

        user = fetch_user_with_user_id(user_id)
        session['uuid'] = user.uuid

    def logout(self):
        return session.pop('uuid', None)
