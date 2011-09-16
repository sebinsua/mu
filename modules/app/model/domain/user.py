from flask import session

class UserDomain:
    user_repository = None

    def __init__(self, user_repository=None):
        self.user_repository = user_repository

    def register(self, form_data, force_login=False):
        from mu.model.entity.user import User

        email = form_data.get('email')
        username = form_data.get('username', default=email)
        password = form_data.get('password')
        user = User(username, email, password)

        user_id = self.user_repository.add_user(user)
        if force_login:
            self.force_login(user_id)
        return user_id

    def login(self, form_data):
        user_identity = form_data.get('user_identity')
        password = form_data.get('password')

        user = self.user_repository.fetch_user_with_identity(user_identity)

        if user.check_password(password):
            session['uuid'] = user.uuid
            return True
        return False

    def force_login(self, user_id):
        from mu.model.entity.user import User

        user = self.user_repository.fetch_user_with_user_id(user_id)
        session['uuid'] = user.uuid

    def logout(self):
        return session.pop('uuid', None)
