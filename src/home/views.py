from flask import Blueprint,render_template

homepage = Blueprint('views', __name__, url_prefix='/', template_folder='templates', static_folder='static')

@homepage.route('/')
def home():
    return render_template('index.html')

@homepage.route('/signup')
def add_user():
    return render_template('signup.html')