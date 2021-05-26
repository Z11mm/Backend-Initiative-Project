from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from .utils.custom_validators import Unique
from .models import User

class SignupForm(FlaskForm):
    """Sign up for a user account"""
    username = StringField(u'Username', [DataRequired()])
    email = StringField(
        u'Email',
        [DataRequired(), Email(message='Not a valid email address.'), Unique(User, User.email, message='This email address already exists.')])
    password = PasswordField(
        u'Password',
        [DataRequired(message='Please enter a password.'),
        Length(min=8),
        EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField(u'Confirm Password', [DataRequired()])
    submit = SubmitField(u'Submit')
