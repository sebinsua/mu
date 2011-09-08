from flask import Blueprint
home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def show_home():
    return "Index page: "
