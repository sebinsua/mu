from flask import Blueprint
user_bp = Blueprint('user', __name__)

@user_bp.route('/user/<username>')
def show_user(username):
    pass

@user_bp.route('/register')
def register_user():
    from mu.model.user import User, db
    # user = User('im.hanz@gmail.com', 'seb', 'password')
    # db.session.add(user)
    # db.session.commit()
    return 'nothing here'
