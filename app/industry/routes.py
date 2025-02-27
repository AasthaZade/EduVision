from flask import Blueprint, render_template
from flask_login import login_required
from app.industry import industry_bp
from app.auth.decorators import role_required

@industry_bp.route("/dashboard")
@login_required
@role_required(["industry_professional", "supervisor"])
def dashboard():
    return render_template("industry_dashboard.html")