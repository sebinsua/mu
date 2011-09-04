from . import app

@app.route('/add/user')
def add_user():
    from mu.model.user import User, db
    user = User('im.hanz@gmail.com', 'seb', 'password')
    db.session.add(user)
    db.session.commit()
    return 'something else'
