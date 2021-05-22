from flask import Blueprint,render_template

homepage = Blueprint('views', __name__, url_prefix='/', template_folder='templates', static_folder='static')

@homepage.route('/')
def home():
    print('working')
    return render_template('index.html')