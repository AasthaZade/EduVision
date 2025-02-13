import os
from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
from config.dbconnect import DatabaseConnection
from app.models import User
db = DatabaseConnection().connection

load_dotenv()
login_manager = LoginManager()


secret_key = os.getenv("SECRET_KEY")

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = secret_key

    #Blueprints
    from app.home import home_bp
    from app.auth import auth

    app.register_blueprint(home_bp)
    app.register_blueprint(auth, url_prefix='/auth')


    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    @login_manager.user_loader

    def load_user(user_id):
        user_data = db.users.find_one({"_id": user_id})
        if user_data:
            return User(user_data["_id"], user_data["username"], user_data["email"])
        return None
    
    return app