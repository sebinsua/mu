from flask import Blueprint, session
bp = Blueprint('home', __name__)

@bp.route("/")
def show_home():
    return "Index page"
