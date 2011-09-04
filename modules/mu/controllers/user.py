# This is a circular import which is bad, however we can't get around it if we
# still wish to use the app decorators: 
# http://flask.pocoo.org/docs/patterns/packages/
from .. import app

@app.route('/add/user')
def add_user():
    from mu.models.user import User, db
    user = User('im.hanz@gmail.com', 'seb', 'password')
    db.session.add(user)
    db.session.commit()
    return 'something else'
