from flask import Flask


def create_app():
    # initialize flask
    app = Flask(__name__)

    # config encrypt session and cookies data for data privacy
    # never share this in production environment to anyone
    app.config['SECRET_KEY'] = 'qwertyuiop'

    # Register your blueprints with your flask application
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
