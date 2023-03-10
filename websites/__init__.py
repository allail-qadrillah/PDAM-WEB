from flask import Flask

app = Flask(__name__)


def create_app():
    app.config['SECRET_KEY'] = 'ASDASDAW'

    from .user_views import user_views
    from .admin_views import admin_views

    app.register_blueprint(admin_views, url_prefix='/')
    app.register_blueprint(user_views, url_prefix='/')

    return app
