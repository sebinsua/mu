from flask import Blueprint
bp = Blueprint('user', __name__)

@bp.route('/user/<username>')
def show_user(username):
    pass

@bp.route('/register')
def register_user():
    from mu.model.user import User, db
    # user = User('im.hanz@gmail.com', 'seb', 'password')
    # db.session.add(user)
    # db.session.commit()
    return 'nothing here'
