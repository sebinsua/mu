from flask import Blueprint
bp = Blueprint('event', __name__)

@bp.route("/artist/<artist>/event/<event>")
def show_event(artist, event):
    return "Event"

@bp.route("/all/events")
def show_events():
    pass
