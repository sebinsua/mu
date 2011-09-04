# This is a circular import which is bad, however we can't get around it if we
# still wish to use the app decorators: 
# http://flask.pocoo.org/docs/patterns/packages/
from .. import app

@app.route("/")
def index():
    return "Index page: "
