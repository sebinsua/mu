# We need the app object since it contains the config data.
from helper.startup import get_app
# Required by the models for database access.
from flaskext.sqlalchemy import SQLAlchemy

app = get_app()
db = SQLAlchemy(app)
