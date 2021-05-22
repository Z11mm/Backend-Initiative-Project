from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['FLASK_ENV'] = 'development'

    # import routes
    from .home import views

    # register blueprints
    app.register_blueprint(views.homepage)

    return app