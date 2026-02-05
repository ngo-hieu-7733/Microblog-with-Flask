"""
    Include all the configuration
"""

import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    FLASK_APP = os.environ.get("FLASK_APP") or "the-first-file-run"