from helper.app import create_app
app = create_app(__name__)

@app.context_processor
def inject_user():
    # note: At some point this could be placed in a helper module and passed to specific blueprints.
    from mu.model.domain.user import UserDomain
    user = UserDomain.user_of_session()
    if user:
        return dict(user=user.to_dict())
    return dict()

from helper.controller import register_controller_blueprints
# "import controller" calls initialise which runs some special code that
# automatically loads each of the python files inside the controller folder.
import controller as controllers
register_controller_blueprints(app, controllers)
