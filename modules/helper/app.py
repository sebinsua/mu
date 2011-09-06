import os
from importlib import import_module

def create_app(name):
    from flask import Flask
    app = Flask(name)

    # Load configuration from code and then attempt to load it from the environment
    # variable if this has been added on *nix.
    app.config.from_object(name + '.config')
    try:
        app.config.from_envvar(app.config['OVERRIDE_WITH_ENVVAR'], silent=True)
    except RuntimeError:
        pass

    return app

def load_app():
    return get_app()

def get_app():
    f = open(os.getcwd() + '/APPLICATION_NAME')
    APPLICATION_NAME = f.read().strip();

    module = import_module(APPLICATION_NAME)
    return module.app
