from flask import Blueprint, render_template
from flask_login import login_required
from app.industry import industry_bp

@industry_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("industry_dashboard.html")
