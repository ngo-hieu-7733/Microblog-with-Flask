"""
    Initialize flask app, app configuration, and all flask extensions here
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

flask_app = Flask(__name__)     # Create Flask application

flask_app.config.from_object(Config)    # Tell Flask to read config file and apply it

db = SQLAlchemy(flask_app)      # Database instance
migrate = Migrate(flask_app, db)        # DB Migration instance

from app import routes, models
