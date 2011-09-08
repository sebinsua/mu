from flask import Blueprint
event_bp = Blueprint('event', __name__)

@event_bp.route("/artist/<artist>/event/<event>")
def show_event(artist, event):
    return "Event"

@event_bp.route("/all/events")
def show_events():
    pass
