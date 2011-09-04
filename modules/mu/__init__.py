from flask import Flask
app = Flask(__name__)

# Load configuration from code and then attempt to load it from the environment
# variable if this has been added on *nix.
app.config.from_object(__name__ + '.config')
try:
    app.config.from_envvar(app.config['OVERRIDE_WITH_ENVVAR'])
except RuntimeError:
    pass

# Import controller will automatically run controller __init__ which imports
# all controllers inside the controllers folder.
import controller
