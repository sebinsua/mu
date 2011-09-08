from flask import Blueprint
author_bp = Blueprint('content_author', __name__)

@author_bp.route("/artist/<artist>")
def show_artist(artist):
    return "Artist"

@author_bp.route("/all/artists")
def show_artists():
    pass
