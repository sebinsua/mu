from flask import Blueprint
release_bp = Blueprint('release', __name__)

@release_bp.route("/artist/<artist>/<release_type>/<release>")
def show_release(artist, release_type, release):
    return "Release"

@release_bp.route("/all/releases")
def show_releases():
    pass
