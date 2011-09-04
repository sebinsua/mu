import os
from importlib import import_module

def get_app():
    f = open(os.getcwd() + '/APPLICATION_NAME')
    APPLICATION_NAME = f.read().strip();

    mu = import_module(APPLICATION_NAME)
    return mu.app
