# We need the app object since it contains the config data.
from .. import app
# Required by the models for database access.
from flaskext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
