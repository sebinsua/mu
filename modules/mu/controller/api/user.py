from flask import Blueprint
user_bp = Blueprint('api_user', __name__)

@user_bp.route("/api/user")
def api_user():
    return "{api: 'user'}"
