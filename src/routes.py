from flask import Blueprint,render_template

homepage = Blueprint('routes', __name__, url_prefix='/')

@homepage.route('/')
def home():
    return "<h1>Home</h1>"