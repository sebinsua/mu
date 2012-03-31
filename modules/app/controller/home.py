from flask import Blueprint, session, render_template
bp = Blueprint('home', __name__)

@bp.route("/")
def show_home():
    # Getting out the username proves that you are logged in... ;)
    from mu.model.domain.user import UserDomain
    username = UserDomain.username_of_session()

    return render_template("home.html", username=username)
