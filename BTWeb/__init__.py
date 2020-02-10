import os
from flask import Flask
from BTWeb.main.routes import main


def create_app(test_config=None):
    app = Flask(__name__)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    app.register_blueprint(main)
    return app
