from . import app

@app.route("/api/user")
def api_user():
    return "{api: 'user'}"
