import os
from flask import Flask
from dotenv import load_dotenv
load_dotenv()

secret_key = os.getenv("SECRET_KEY")

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = secret_key

    #Blueprints
    from app.home import home_bp

    app.register_blueprint(home_bp)

    return app