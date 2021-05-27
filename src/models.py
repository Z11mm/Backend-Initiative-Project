from datetime import datetime
from . import db
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from flask import current_app

pw_bcrypt = Bcrypt(current_app)
class User(db.Model):
    """Data model for user accounts"""

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username!r}>'

