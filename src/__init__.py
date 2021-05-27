"""Initialize application"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')

    # initialize plugins
    db.init_app(app)
    login_manager.init_app(app)
    
    with app.app_context():
        # import routes
        from .home import views

        db.create_all()

        # register blueprints
        app.register_blueprint(views.homepage)

        return app