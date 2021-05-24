from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')

    # initialize database
    db.init_app(app)

    with app.app_context():
        # import routes
        from .home import views

        # register blueprints
        app.register_blueprint(views.homepage)

    return app