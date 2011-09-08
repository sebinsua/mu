from flask import Blueprint
bp = Blueprint('content_author', __name__)

@bp.route("/artist/<artist>")
def show_artist(artist):
    return "Artist"

@bp.route("/all/artists")
def show_artists():
    pass
