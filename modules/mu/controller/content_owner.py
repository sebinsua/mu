from flask import Blueprint
owner_bp = Blueprint('content_owner', __name__)

@owner_bp.route("/label/<label>")
def show_label(label):
    return "Content Owner"

@owner_bp.route("/all/labels")
def show_labels():
    pass
