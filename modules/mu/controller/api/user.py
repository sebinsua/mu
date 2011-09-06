from flask import Blueprint
user = Blueprint('api/user', __name__)

@user.route("/api/user")
def api_user():
    return "{api: 'user'}"
