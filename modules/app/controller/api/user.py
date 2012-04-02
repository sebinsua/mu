from flask import Blueprint

bp = Blueprint('api_user', __name__)

@bp.route("/api/user")
def api_user():
    return "{api: 'user'}"
