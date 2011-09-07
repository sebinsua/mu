# TODO: What do we gain by not using everything directly?
# Is this legacy? When should the db be setup? Will it be helpful to create
# helper methods for myself?

# We need the app object since it contains the config data.
from helper.app import get_app
# Required by some of the models for database access.
from flaskext.sqlalchemy import SQLAlchemy

app = get_app()
db = SQLAlchemy(app)
