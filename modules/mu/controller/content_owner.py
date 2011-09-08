from flask import Blueprint
bp = Blueprint('content_owner', __name__)

@bp.route("/label/<label>")
def show_label(label):
    return "Content Owner"

@bp.route("/all/labels")
def show_labels():
    pass
