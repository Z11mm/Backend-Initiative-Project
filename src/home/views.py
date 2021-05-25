from flask import Blueprint,render_template,request,redirect
from datetime import datetime as dt

from ..models import db, User

homepage = Blueprint('views', __name__, url_prefix='/', template_folder='templates', static_folder='static')

@homepage.route('/')
def home():
    return render_template('index.html')

@homepage.route('/signup', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username_input = request.form['username']
        email_input = request.form['email']
        password_input = request.form['password']

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
        return render_template('signup.html', users=users)

@homepage.route('/signin')
def login_user():
    return render_template('signin.html')