from flask import Blueprint
bp = Blueprint('release', __name__)

@bp.route("/artist/<artist>/<release_type>/<release>")
def show_release(artist, release_type, release):
    return "Release"

@bp.route("/all/releases")
def show_releases():
    pass

@bp.route("/artist/<artist>/add/<release_type>")
def add_release_to_artist(artist, release_type):
    return "Add release to artist"
