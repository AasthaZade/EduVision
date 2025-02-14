from flask import Blueprint, render_template
from flask_login import login_required
from app.learner import learner_bp

@learner_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("learner_dashboard.html")
