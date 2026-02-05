from flask import Flask
from config import Config

flask_app = Flask(__name__)     # Create Flask application
flask_app.config.from_object(Config)    # Tell Flask to read config file and apply it

from app import routes
