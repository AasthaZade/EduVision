from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.auth import auth
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User

from config.dbconnect import DatabaseConnection
db = DatabaseConnection().connection

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    email = request.form.get("email")
    password = request.form.get("password")
    user_data = db.users.find_one({"email": email})

    if user_data and check_password_hash(user_data["password"], password):
        user = User(user_data["_id"], user_data["username"], user_data["email"])
        login_user(user)
        flash("Login successful!", "success")
        return redirect(url_for("dashboard"))  # Adjust as needed

    flash("Invalid email or password", "danger")
    return redirect(url_for("auth.login"))

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "info")
    return redirect(url_for("home.index"))  # Adjust as needed

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    if db.users.find_one({"email": email}):
        flash("Email already registered!", "danger")
        return redirect(url_for("auth.register"))

    hashed_password = generate_password_hash(password)
    user_id = db.users.insert_one({
        "username": username,
        "email": email,
        "password": hashed_password
    }).inserted_id

    user = User(user_id, username, email)
    login_user(user)
    flash("Registration successful!", "success")
    return redirect(url_for("home.index"))  # Adjust as needed
