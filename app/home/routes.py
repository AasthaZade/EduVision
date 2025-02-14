from flask import render_template
from flask_login import login_required
from app.home import home_bp
from app.auth.decorators import role_required

@home_bp.route("/", methods=["GET"])
@home_bp.route("/index", methods=["GET"])
def index():
    return render_template("index.html")