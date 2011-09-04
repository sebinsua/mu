from helper.startup import get_app
app = get_app()

from helper.controller import generate_controller_list
__all__ = generate_controller_list(__file__)

# Import all of the controllers that belong to __name__.
__import__(__name__, globals(), locals(), __all__, -1)
