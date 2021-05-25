from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo
from .utils.custom_validators import Unique
from .models import User

class SignupForm(FlaskForm):
    username = StringField(u'Username', [InputRequired()])
    email = StringField(
        u'Email',
        [InputRequired(), Email(), Unique(User, User.email, message='This email address already exists.')])
    password = PasswordField(
        u'Password',
        [InputRequired(),
        Length(min=8),
        EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField(u'Confirm Password', [InputRequired()])
    submit = SubmitField(u'Submit')
