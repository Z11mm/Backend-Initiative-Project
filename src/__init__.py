from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['FLASK_ENV']='development'

    # import routes
    from .routes import homepage

    # register blueprints
    app.register_blueprint(homepage)

    return app