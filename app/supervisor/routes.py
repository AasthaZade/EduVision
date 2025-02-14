from flask import Blueprint, render_template
from flask_login import login_required
from app.supervisor import supervisor_bp

@supervisor_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("supervisor_dashboard.html")
