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

def get_app_name():
    try:
        f = open(os.getcwd() + '/APPLICATION_NAME')
        APPLICATION_NAME = f.read().strip();
    except IOError:
        pass

    if not APPLICATION_NAME:
        APPLICATION_NAME = 'app'

    return APPLICATION_NAME

def get_app():
    APPLICATION_NAME = get_app_name()
    try:
        module = import_module(APPLICATION_NAME)
        return module.app
    except ImportError:
        APPLICATION_NAME = 'app'
        module = import_module(APPLICATION_NAME)
        return module.app

    # This next line should never be run.
    return False
