from flask import Blueprint
bp = Blueprint('home', __name__)

@bp.route("/")
def show_home():
    return "Index page: "
