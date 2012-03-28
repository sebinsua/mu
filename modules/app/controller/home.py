from flask import Blueprint, session, render_template
bp = Blueprint('home', __name__)

@bp.route("/")
def show_home():
    # Getting out the username proves that you are logged in... ;)
    username = None
    if session.has_key('uuid'):
        uuid = session['uuid']
        from mu.model.repository.user import fetch_user_with_uuid
        user = fetch_user_with_uuid(uuid)
        username = user.username

    return render_template("home.html", username=username)
