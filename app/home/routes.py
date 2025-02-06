from flask import render_template
from app.home import home_bp

@home_bp.route("/", methods=["GET"])
@home_bp.route("/index", methods=["GET"])
def index():
    return render_template("index.html")