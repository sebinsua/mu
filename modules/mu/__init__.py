from helper.app import create_app
app = create_app(__name__)

from helper.controller import register_controller_blueprints
# "import controller" calls initialise which runs some special code that
# automatically loads each of the classes inside the controller folder.
import controller
register_controller_blueprints(app, controller)
