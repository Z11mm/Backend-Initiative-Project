# Handle views for the homepage
from flask import Blueprint,render_template,redirect, url_for, request
from datetime import datetime as dt

from flask.globals import request

from ..models import db, User
from ..forms import SignupForm, SigninForm

homepage = Blueprint('views', __name__, url_prefix='/', template_folder='templates', static_folder='static')

@homepage.route('/')
def home():
    return render_template('index.html')

@homepage.route('/signup', methods=['GET', 'POST'])
def add_user():
    form = SignupForm()
    print(form.errors)
    if form.is_submitted():
        print('submitted')
    if form.validate():
        print('valid')
    print(form.errors)
    if request.method == 'POST' and form.validate_on_submit():
        username_input = form.username.data
        email_input = form.email.data
        password_input = form.password.data

        new_user = User(
            username = username_input,
            email = email_input,
            password = password_input,
            date_joined = dt.utcnow()
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding new user'
    else:
        users = User.query.order_by(User.date_joined).all()
        return render_template('signup.html', users=users, form=form)

@homepage.route('/signin', methods=['GET','POST'])
def login_user():
    form = SigninForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        email_input = form.email.data
        password_input = form.password.data
    return render_template('signin.html')