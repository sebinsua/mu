from flask import Blueprint
user = Blueprint('user', __name__)

@user.route('/add/user')
def add_user():
    from mu.model.user import User, db
    # user = User('im.hanz@gmail.com', 'seb', 'password')
    # db.session.add(user)
    # db.session.commit()
    return 'nothing here'
