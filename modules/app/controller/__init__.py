from helper.controller import generate_controller_list

controllers = generate_controller_list(__file__)

# Import all of the controllers that belong to __name__.
__import__(__name__, globals(), locals(), controllers, -1)

__all__ = controllers
