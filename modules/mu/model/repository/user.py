from helper.database import db

class UserRepository:
    def add_user(self, user):
        db.session.add(user)
        db.session.commit()
        return user.user_id
