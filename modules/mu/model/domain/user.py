import sys

class UserDomain:
    def register(self, form_data):
        print >> sys.stderr, str(form_data)
        from mu.model.entity.user import User
        from mu.model.repository.user import UserRepository

        email = form_data.get('email')
        username = form_data.get('username', default=email)
        password = form_data.get('password')
        user = User(username, email, password)

        user_repository = UserRepository()
        return user_repository.add_user(user)
