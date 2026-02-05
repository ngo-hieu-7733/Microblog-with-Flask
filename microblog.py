import sqlalchemy as sa
import sqlalchemy.orm as so
from app import flask_app, db
from app.models import User, Post

# The shell_context_processor decorator allows developers 
# to pre-load commonly used objects into the Flask shell environment.
@flask_app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'soo': so, 'db': db, 'User': User, 'Post': Post}
